import argparse
import time
from concurrent.futures import ThreadPoolExecutor, Future
from typing import Callable, List
from datetime import datetime

import tzlocal
from apscheduler.schedulers.background import BackgroundScheduler
from netifaces import interfaces, ifaddresses, AF_INET
from ipaddress import IPv4Interface, IPv4Network, IPv4Address
from pythonping import ping
from pythonping.executor import ResponseList, Response, Message
from scapy.layers.l2 import Ether, ARP, Packet
from scapy.sendrecv import srp
from scapy.plist import SndRcvList, PacketList, QueryAnswer

from sender import get_url, send_data
from settings import CREATE_SESSION_ENDPOINT


def run_pinger(
        count: int,
        timeout: int,
        interval: int,
        threads_amount: int,
        ssid: str,
        nic: str):
    print("pinger started")
    ip_addr: str = get_nic_ip_address(nic=nic)
    net: IPv4Network = get_network(ip_addr=ip_addr)
    management_ips = (
        IPv4Address(ip_addr),
        net.broadcast_address,
        net.network_address,
    )
    print(f"scanning network {net} exclude ips: {management_ips}")

    start_time = time.perf_counter()

    with ThreadPoolExecutor(max_workers=threads_amount) as executor:
        futures: List[Future] = []

        for ip in net:
            if ip in management_ips:
                continue

            ping_params = {
                "target": str(ip),
                "timeout": timeout,
                "interval": interval,
                "count": count,
            }
            func = secure_ping(ping_params)
            futures.append(executor.submit(func))

    all_results: List[ResponseList] = [future.result() for future in futures]
    ok_results: List[ResponseList] = [result for result in all_results if result.success()]
    interval = time.perf_counter() - start_time
    print(f"\n{'='*60}\nfound {len(ok_results)} devices - it takes {interval} secs\n{'='*60}")
    data: List[dict] = prepare_data_to_send(ok_results=ok_results, ssid=ssid)
    url = get_url(endpoint=CREATE_SESSION_ENDPOINT)
    response = send_data(url=url, data=data)
    print(f"endpoint: {url} response: {response}")


def get_nic_ip_address(nic: str):
    print(f"All available interfaces: {interfaces()}\nNIC: {nic}")
    net_iface: dict = ifaddresses(nic)
    af_inet: list[dict] = net_iface.get(AF_INET)
    ip: str = af_inet[0].get("addr")
    print(f"local ip-address: {ip}")
    return ip


def get_network(ip_addr, prefix=24):
    print(f"getting network for: {ip_addr} with prefix: {prefix} bits")
    ip_addr_with_prefix = f"{ip_addr}/{prefix}"
    interface = IPv4Interface(ip_addr_with_prefix)
    return interface.network


def secure_ping(ping_params: dict) -> Callable:
    """
    This function returns a function that executes `pythonping.ping` operation with parameters.

    :param ping_params: Additional parameters for `pythonping` (interval, timeout, ...)
    :return: A callable function that performs `ping` and returns `ResponseList`
    If `OSError` occurs during ping operation the func returns empty `ResponseList`
    """

    def func() -> ResponseList:
        try:
            res: ResponseList = ping(**ping_params)
            print(f"`secure_ping` with params: {ping_params} get result: {res}")
            return res
        except OSError as e:
            print(f"`secure_ping` error {e} with params: {ping_params}")
            return ResponseList()

    return func


def prepare_data_to_send(ok_results: List[ResponseList], ssid: str):
    data_to_send = []

    for results_list in ok_results:
        for result in results_list:
            result: Response
            result_message: Message = result.message

            if not result_message:
                continue

            device_ip: str = result_message.source
            mac_addr = get_mac_addr(ip=device_ip)

            if not mac_addr:
                continue

            device_data = {
                "network_ssid": ssid,
                "device": {
                    "mac_addr": mac_addr,
                    "ipv4": device_ip,
                }
            }

            data_to_send.append(device_data)
            break

    print(f"`data_to_send`: {data_to_send}")
    return data_to_send if data_to_send else [{"network_ssid": ssid}]


def get_mac_addr(ip):
    print(f"getting mac-addr for device with ip: {ip}")
    arp_request: Packet = ARP(pdst=ip)
    broadcast_ethernet_request: Packet = Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_broadcast_request: Packet = broadcast_ethernet_request / arp_request
    data: tuple[SndRcvList, PacketList] = srp(x=arp_broadcast_request)

    print(f"SndRcvList: {data[0]}")
    print(f"PacketList: {data[1]}")

    snd_rcv_list = data[0]

    if len(snd_rcv_list) == 0:
        print(f"warning: can not get MAC address for ip: {ip}")
        return None

    query_answer: QueryAnswer = snd_rcv_list[0]
    ether_answer: Ether = query_answer.answer
    mac_addr = ether_answer.hwsrc
    print(f"MAC address for ip: {ip}: {mac_addr}")
    return mac_addr


def parse_arguments():
    parser = argparse.ArgumentParser(description="Pinger script")
    parser.add_argument(
        "--ssid",
        type=str,
        dest="ssid",
        help="Network Service Set Identifier",
        required=True,
    )
    parser.add_argument(
        "--nic",
        type=str,
        dest="nic",
        help="Network Interface Card name",
        required=True,
    )
    return parser.parse_args()


def main():
    parser_args = parse_arguments()
    print(f"`parser` input arguments: {parser_args}")

    pinger_params = {
        "count": 3,
        "timeout": 2,
        "interval": 1,
        "threads_amount": 100,
        "ssid": parser_args.ssid,
        "nic": parser_args.nic,
    }

    scheduler_params = {
        "func": run_pinger,
        "kwargs": pinger_params,
        "trigger": "interval",
        "seconds": 120,
        "next_run_time": datetime.now()
    }

    print("creating scheduler")
    scheduler = BackgroundScheduler(timezone=tzlocal.get_localzone())

    print("adding job to the scheduler")
    scheduler.add_job(**scheduler_params)

    print("starting the scheduler")
    scheduler.start()

    # Blocking Loop
    try:
        while True:
            time.sleep(3)
    except (KeyboardInterrupt, SystemExit) as e:
        print("shutting down the scheduler")
        scheduler.shutdown()
        raise e


if __name__ == "__main__":
    main()


# TODO: register network before start send data

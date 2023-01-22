from common import commands_descr
from utils import stub, get_calculation_data
from calculator import calc


def command_dialog():
    while True:
        print("Select command:")
        [print(f"`{letter}`: {descr}") for letter, descr in commands_descr.items()]

        command = input("-> ").lower()
        if command not in commands_descr:
            print(f"Unknown command: `{command}`")
            continue

        return command


def calculator_dialog(command):
    res, err = None, None

    sub_dialog_mapper = {
        "c": get_calculation_data
    }

    sub_dialog = sub_dialog_mapper.get(command, stub)
    calc_data, err = sub_dialog()
    if not err:
        data_to_send = (calc_data["a"], calc_data["b"], calc_data["op"], command)
        res = calc.send(data_to_send)
    next(calc)
    return res, err


def main():
    while True:
        print("=" * 20)
        command = command_dialog()
        res, err = calculator_dialog(command)
        if err:
            print(f"ERROR: {err}\n")
            continue
        print(f"Result: {res}\n")


main()

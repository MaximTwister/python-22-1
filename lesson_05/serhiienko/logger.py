COLOR = {
    "success": "\33[32m",
    "error": "\033[91m",
    "info": "\33[34m",
}


def logger(message, case):
    if case not in COLOR:
        print(COLOR.get("error") + f"Error - not current type")
        return

    if case == "error":
        print(COLOR[case] + f"Error - {message}")
        return

    if case == "success":
        print(COLOR[case] + f"Success - {message}")
        return

    if case == "info":
        print(COLOR[case] + f"Information - {message}")
        return

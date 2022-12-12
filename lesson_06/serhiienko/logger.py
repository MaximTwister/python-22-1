from typing import Optional

COLOR = {
    "error": "\033[91m",
    "info": "\33[34m",
}


def logger(message: str, case: str = "info") -> Optional[None]:
    if case == "error":
        print(COLOR[case] + f"Error - {message}")
        return

    if case == "info":
        print(COLOR[case] + f"Information - {message}")
        return

from typing import Optional
import os
import random


def create_files_list(extensions: list[str], files_amount: int) -> list[str]:
    list_files_names = []

    for extension in extensions:
        for index in range(files_amount):
            list_files_names.append(f"{random.random()}.{extension}")

    return list_files_names


def create_files(dir_name: str, files: list[str]) -> Optional[str]:
    err = None

    if not os.path.isdir(dir_name):
        os.mkdir(dir_name)

    try:
        for file in files:
            current_file = open(f"{dir_name}/{file}", 'w')
            current_file.write("")
            current_file.close()
    except Exception:
        err = "Something bad"

    return err


def delete_files_by_extension(dir_name: str, extension: str) -> Optional[str]:
    error = None

    try:
        for file in os.listdir(dir_name):
            if file.endswith(f".{extension}"):
                os.remove(os.path.join(dir_name, file))
    except FileNotFoundError as e:
        error = f"No such file or directory: {e.filename}"

    return error



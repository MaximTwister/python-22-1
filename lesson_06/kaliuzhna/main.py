import constants
import random
from typing import Optional
import os

from constants import (
    EXTENSIONS,
    FILES_AMOUNT,
    FILENAME_LENGTH,
    WORKING_DIR,
    EMPTY_STRING,
)


def create_files_list(extensions: list[str], files_amount: int, sym: int) -> tuple[list[str], Optional[str]]:
    err = None
    files_list = []

    try:
        rn = [x for x in range(10 ** (sym - 1), 10 ** sym)]
        random.shuffle(rn)
        for extension in extensions:
            for r in range(files_amount):
                files_list.append(str(rn[r]) + "." + extension)
    except ValueError:
        err = 'A ValueError occured!'
    except Exception as e:
        err = f"Unexpected {e}, {type(e)=}"

    return files_list, err


def create_files(working_dir: str, files_list: list[str, ...]) -> [Optional[str]]:
    err = None

    try:
        os.chdir(working_dir)
        print(f"My working directory: {os.getcwd()}")
        [os.system(f"echo {EMPTY_STRING} > {f}") for f in files_list]
        print(f"files in directory: {os.listdir()}")

    except FileExistsError as e:
        err = f"{e}"  # попытка создания файла или директории, которая уже существует.
    except FileNotFoundError as m:
        err = f"{m}"  # файл или директория не существует.
    except InterruptedError as p:
        err = f"{p}"  # системный вызов прерван входящим сигналом.
    except IsADirectoryError as v:
        err = f"{v}"  # ожидался файл, но это директория.
    except NotADirectoryError as r:
        err = f"{r}"  # ожидалась директория, но это файл.
    except PermissionError as g:
        print(f"{g}")  # не хватает прав доступа.
    except ProcessLookupError as k:
        print(f"{k}")  # указанного процесса не существует.
    except TimeoutError as w:
        print(f"{w}")  # закончилось время ожидания."
    return err


def main():
    file_names, err = create_files_list(EXTENSIONS, FILES_AMOUNT, FILENAME_LENGTH)

    if err:
        print("Oops. error during names creation: {err}")
        return
    print(f"File-names amount: {len(file_names)}\n{file_names}")

    err = create_files(WORKING_DIR, file_names, )

    if err:
        print("Oops. error during files creation: {err}")
        return


main()  # Entrypoint

import constant
import random
from typing import Optional
import os


files_list = []
def create_files_list(extensions: list[str], files_amount: int = 20, sym=5) -> tuple[list[str], None]:

    err = None
    try:
        rn = [x for x in range(10 ** (sym - 1), 10 ** sym)]
        random.shuffle(rn)
        for elem in extensions:
            for r in range(1, (files_amount + 1)):
                files_list.append(str(rn[r]) + "." + elem)
    except ValueError:
        print('A ValueError occured!')
    except Exception as e:
        print(f"Unexpected {e}, {type(e)=}")
    else:
        print('No exception')
    return files_list, err
()


def create_files(dir:[str], files_list: [list[str], None]) -> [Optional[str]]:
    res = None
    err = None
    try:
        os.chdir(dir)
        print(f"My work directory: {os.getcwd()}")
        [os.system(f"echo {constant.EMPTY_STRING} > {f}") for f in files_list]
        print(f"files in directory: {os.listdir()}")
    except FileExistsError as e:
        print(f"{e}") # попытка создания файла или директории, которая уже существует.
    except FileNotFoundError as m:
        print(f"{m}") #- файл или директория не существует.
    except InterruptedError as p:
        print(f"{p}") #- системный вызов прерван входящим сигналом.
    except IsADirectoryError as v:
        print(f"{v}") # ожидался файл, но это директория.
    except NotADirectoryError as r:
        print(f"{r}") #- ожидалась директория, но это файл.
    except PermissionError as g:
        print(f"{g}") # не хватает прав доступа.
    except ProcessLookupError as k:
        print(f"{k}") # #указанного процесса не существует.
    except TimeoutError as w:
        print(f"{w}") #закончилось время ожидания."
    return res, err
()


def main():
    if (type(constant.EXTENSIONS) is list and constant.EXTENSIONS
        and [isinstance(elem, str) for elem in constant.EXTENSIONS]
        and (type(constant.FILES_AMOUNT) is int and constant.FILES_AMOUNT > 0)
        and (type(constant.SYMB) is int and constant.SYMB > 0)
        and (constant.FILES_AMOUNT <= (9 * 10 ** (constant.SYMB - 1)))):
        files_list, err = create_files_list(constant.EXTENSIONS, constant.FILES_AMOUNT, constant.SYMB)
        if err:
            print(err)
        else:
            print(f"Files list: {files_list}")
    else:
        print("error: not supported argument type")


DIR = "/Users/Пользователь/test"
files = tuple(files_list)
print(files)

res, err = create_files(DIR, files)


main()



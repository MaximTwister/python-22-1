import os
import platform
from typing import Optional
import random


OS_slash_sym = "\\"  # default slash symbol for path variable if your OS is Windows
FILES_AMOUNT = 20
EXTENSIONS = ["txt", "mp3", "pdf", "docx", "py", "tmp"]
EMPTY_STRING = ""


pc_user_name = str(os.getlogin())  # get pc user name
print(f"Your PC USER NAME is : {pc_user_name}")


default_path = ''.join(("C:", OS_slash_sym, "Users", OS_slash_sym, os.getlogin(), OS_slash_sym, 'Documents'))


if platform.system() != 'Windows':
    print(f"Your OS is {platform.system()} not Windows OS! This program is written for Windows OS!")
    OS_slash_sym = "/"
else:
    print(f"Your OS is {platform.system()}! That's OK!")


def create_new_folder(path: str):
    error = None
    print("Your files will be saved to the default directory \"С:Users\<your username>\<new folder>\".")
    try:
        new_folder_name = str(input("Please enter new folder name to creat it in current default directory :"))
        new_pass = os.path.join(default_path, new_folder_name)
        os.mkdir(new_pass)
        print("New folder created successfully!")
        os.chdir(path)
    except OSError as e:
        return f'error during new folder creations: {e}'
    except Exception:
        return f'Unexpected error during new folder creations'
    return new_pass


new_pass = create_new_folder(default_path)


def create_files_list(extensions: list[str], files_amount: int) -> list[str] | str:
    error = None
    try:
        files_to_create_list = []
        for ext in range(len(extensions)):
            for amount in range(files_amount):
                file_name = str(random.randint(10000, 99999))
                file_extensions = str(extensions[ext])
                files_to_create_list.append(file_name + "." + file_extensions)
    except ValueError as e:
        return f'error during list creations: {e}. Not a proper <files_amount>! Try it again'
    except OverflowError as e:
        print(e)
    except OSError as e:
        return f'error during list creations: {e}'
    return files_to_create_list


def create_files(files: [list[str], None], ) -> [Optional[str]]:
    error = None
    try:
        os.chdir(new_pass)
        print(f"My work directory: {os.getcwd()}")
        [os.system(f"echo {EMPTY_STRING} > {f}") for f in files]
        print(f"files in directory: {os.listdir(new_pass)}")
    except PermissionError as per:
        print(f'{per} - you do not have permission to create files in this directory')
    except FileExistsError as fxt:
        print(f"{fxt}")
    return


file_list = create_files_list(extensions=EXTENSIONS, files_amount=FILES_AMOUNT)
print(file_list)
create_files(file_list)


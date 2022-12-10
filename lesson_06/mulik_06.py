import os
from typing import Optional
import random


FILES_AMOUNT = 20
EXTENSIONS = ["txt", "mp3", "pdf", "docx", "py", "tmp"]
EMPTY_STRING = ""


# Create files_to_create => [20 * txt; 20 * mp3; ...]
def create_files_list(extensions: list[str, ...], files_amount: int) -> list[str, ...]:
    res = []
    for ext in extensions:
        for i in range(files_amount):
            r = random.randint(10000, 999999)
            res.append(str(r) + '.' + ext)
    return res


# Optional[None] - error

def create_files(dir: str, files: list[str, ...]) -> Optional[str]:
    os.chdir(dir)
    [os.system(f"echo {EMPTY_STRING} > {f}") for f in files]
    return


# Optional[None] - error
def delete_files_by_extension(dir: str, extension: str) -> Optional[None]:
    os.chdir(dir)
    files = os.listdir()
    for file_name in files:
        if file_name.endswith(extension):
            os.remove(file_name)
    return

r = create_files('tmp', create_files_list(EXTENSIONS, FILES_AMOUNT))
print(r)

delete_files_by_extension('tmp', 'mp3')

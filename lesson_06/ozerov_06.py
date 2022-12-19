import os
import random

test_dir = 'C:/Users/Маленький Мук/Desktop/123'
FILES_AMOUNT = 20
EXTENSIONS = ["txt", "mp3", "pdf", "docx", "py", "tmp"]
EMPTY_STRING = ""


def create_files_list(extensions: list[str, ...], files_amount: int) -> list[str, ...]:
    new = []
    for e in extensions:
        for i in range(files_amount):
            r = random.randint(1000, 9999)
            new.append(str(r) + '.' + e)
    return new


os.chdir(test_dir)
print(os.getcwd())
[os.system(f'echo {EMPTY_STRING} > {f}') for f in create_files_list(extensions=EXTENSIONS, files_amount=FILES_AMOUNT)]
print(os.listdir())

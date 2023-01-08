from pathlib import Path
import random

FILES_AMOUNT = 20
EXTENSIONS = ["txt", "mp3", "pdf", "docx", "py", "tmp"]

list_files = []

def create_files_list(extensions, files_amount):
    for j in extensions:
        for _ in range(20):
            new_file = str(random.random()) + "." + j
            list_files.append(new_file)

def create_files(dir_p, file_list):
    for i in file_list:
        file_path = dir_p.joinpath(i)
        if dir_p.is_dir():
                with open(file_path, "a") as f:
                    f.close()
    
dir_path = Path("C:\\Users\\Yaroslav\\Desktop\\dev\\Python\\python-22-1\\python-22-1\\lesson_06\\dir")
create_files_list(EXTENSIONS, FILES_AMOUNT)
create_files(dir_path, list_files)
print(list_files)
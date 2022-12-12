import os
from files_methodos import (
    create_files_list,
    create_files,
    delete_files_by_extension,
)
from logger import logger


FILES_AMOUNT = 20
EXTENSIONS = ["txt", "mp3", "pdf", "docx", "py", "tmp"]


def main():
    dir_name = "random-files"
    path_to_dir = f"{os.getcwd()}/{dir_name}"

    logger("The program has started")
    files = create_files_list(EXTENSIONS, FILES_AMOUNT)

    creation_error = create_files(path_to_dir, files)

    if creation_error:
        logger(creation_error, "error")
    else:
        logger("Created files")

    extension = "txt"
    deletion_error = delete_files_by_extension(path_to_dir, extension)

    if deletion_error:
        logger(deletion_error, "error")
    else:
        logger(f"Files have been deleted .{extension}")

    logger("Program ended")


main()

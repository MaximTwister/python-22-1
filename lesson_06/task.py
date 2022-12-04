from typing import Optional


FILES_AMOUNT = 20
EXTENSIONS = ["txt", "mp3", "pdf", "docx", "py", "tmp"]


# Create files_to_create => [20 * txt; 20 * mp3; ...]
def create_files_list(extensions: list[str, ...], files_amount: int) -> list[str, ...]:
    # NOTE: use random library to generate names => 23456.txt
    pass


# Optional[None] - error
def create_files(dir: str, files: list[str, ...]) -> Optional[str]:
    # create all `files` in `dir` folder
    pass


# Optional[None] - error
# (*) def delete_files_by_extension(dir: str, extension: str) -> Optional[None]

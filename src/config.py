import os

from dotenv import load_dotenv

load_dotenv()


root_directory = os.getcwd()

files_dir_path = os.path.join(root_directory, "files")

file_dir_name = os.getenv("FILE_DIR_NAME", "raw")
PATH_FILE_DIR = os.path.join(files_dir_path, file_dir_name)

save_file_dir_name = os.getenv("SAVE_FILE_DIR_NAME", "processed")
PATH_SAVE_FILE_DIR = os.path.join(files_dir_path, save_file_dir_name)

MAIL = os.getenv("MAIL", "example@domain.com")

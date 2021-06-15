import os

from dotenv import load_dotenv

load_dotenv()

HOME_DIR = os.getenv('HOME_DIR')

SAVE_PATH = os.getenv('SAVE_PATH')

MAIL = os.getenv('MAIL')

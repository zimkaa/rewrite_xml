import os
import xml.etree.ElementTree as ET  # noqa: N817

from loguru import logger

import src.config as config
from src.my_time import my_timer


def process(path: str, save_path_dir: str) -> None:
    """
    From folder get XML and rewrite
    """
    for element_name in os.listdir(path):
        path_name = os.path.join(path, element_name)
        if os.path.isdir(path_name):
            process(path_name, save_path_dir)
        else:
            change_xml(path_name, element_name, save_path_dir)


def change_xml(path: str, file_name: str, save_path_dir: str) -> None:
    """
    Add to XML e-mail
    """
    tree = ET.parse(path)
    element = tree.getroot()[0][-2]
    element.set("value", config.MAIL)
    full_path = os.path.join(save_path_dir, file_name)
    tree.write(full_path, encoding="WINDOWS-1251")


def counting_files(path: str) -> None:
    """
    Number of files
    """
    logger.success(f"Created {len(os.listdir(path))} files")


@my_timer
def main(path: str = config.PATH_FILE_DIR, save_path_dir: str = config.PATH_SAVE_FILE_DIR) -> None:
    process(path, save_path_dir)
    counting_files(save_path_dir)

# coding: cp1251

from loguru import logger
import os

import xml.etree.ElementTree as ElT

import config
from my_time import my_timer


def get_path_name(path: str) -> None:
    """
    From folder get XML and rewrite
    """
    for element_name in os.listdir(path):
        path_name = os.path.join(path, element_name)
        if os.path.isdir(path_name):
            path_name = get_path_name(path_name)
        else:
            cange_xml(path_name, element_name)


def cange_xml(path: str, file_name: str) -> None:
    """
    Add to XML mail
    """
    tree = ElT.parse(path)
    element = tree.getroot()[0][-2]
    element.set("value", config.MAIL)
    save_path = os.path.join(config.SAVE_PATH, file_name)
    tree.write(save_path, encoding="WINDOWS-1251")


def counting_the_files(path: str) -> None:
    """
    Number of files
    """
    logger.info(f"Created {len(os.listdir(path))} files")


@my_timer
def main():
    get_path_name(config.HOME_DIR)
    counting_the_files(config.SAVE_PATH)


if __name__ == "__main__":
    main()

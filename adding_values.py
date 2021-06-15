# coding: cp1251

from time import perf_counter
from loguru import logger
import os

import xml.etree.ElementTree as ElT

import config


HOME_DIR = "C:\\Projects\\Project_rewrite_XML\\vor\\xml"
SAVE_PATH = "C:\\Projects\\Project_rewrite_XML\\vor\\xml_new"
MAIL = "Tatyana@example.ru"


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


def main():
    start = perf_counter()

    get_path_name(config.HOME_DIR)

    counting_the_files(config.SAVE_PATH)

    stop = perf_counter() - start
    logger.info(f"execution time {stop}")


if __name__ == "__main__":
    main()

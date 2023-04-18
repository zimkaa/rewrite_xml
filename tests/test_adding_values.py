import os
import xml.etree.ElementTree as ET  # noqa: N817

import pytest

from src import main
from src.config import MAIL


root_directory = os.getcwd()

files_dir_path = os.path.join(root_directory, "tests", "files")

PATH_FILE_DIR = os.path.join(files_dir_path, "raw")
PATH_SAVE_FILE_DIR = os.path.join(files_dir_path, "processed")


@pytest.fixture()
def clear_folder():
    yield
    for root, _, files in os.walk(PATH_SAVE_FILE_DIR):
        for file in files:  # noqa: VNE002
            os.unlink(os.path.join(root, file))


def test_add_value(clear_folder):
    main(PATH_FILE_DIR, PATH_SAVE_FILE_DIR)

    assert len(os.listdir(PATH_SAVE_FILE_DIR)) == 1

    for element_name in os.listdir(PATH_SAVE_FILE_DIR):
        path_name = os.path.join(PATH_SAVE_FILE_DIR, element_name)
        tree = ET.parse(path_name)
        element = tree.getroot()[0][-2]
        assert element.get("value") == MAIL

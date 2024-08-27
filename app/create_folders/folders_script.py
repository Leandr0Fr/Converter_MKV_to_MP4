import os

from ..constants.folders_path import *


def dir_folders() -> list[str]:
    return [p.name for p in VIDEOS_PATH.iterdir() if p.is_dir()]


def exists_basics_folders(folders: list[str]) -> tuple[bool, bool]:
    return INPUT_FOLDER in folders, OUTPUT_FOLDER in folders


def create_folders() -> None:
    folders = dir_folders()
    exists_input, exists_output = exists_basics_folders(folders)

    if not exists_input:
        path_complete = os.path.join(VIDEOS_PATH, INPUT_FOLDER)
        try:
            os.makedirs(path_complete, exist_ok=True)
        except Exception as e:
            print(e)

    if not exists_output:
        path_complete = os.path.join(VIDEOS_PATH, OUTPUT_FOLDER)
        try:
            os.makedirs(path_complete, exist_ok=True)
        except Exception as e:
            print(e)

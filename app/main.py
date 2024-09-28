import os
import sys

from .ffmpeg.converter import convert_files
from .messages.prints import *


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None

    if path and is_valid_path(path):
        convert_files(path)
    else:
        print_no_parameter()


def is_valid_path(path):
    return os.path.exists(path)


if __name__ == "__main__":
    main()

import os
import threading
import time
from pathlib import Path

import ffmpeg

from .constants.folders_path import INPUT_PATH, OUTPUT_PATH
from .messages.prints import *
from .utils.time import get_hours_minutes_seconds, get_local_time

path_videos = Path(os.path.expanduser("~\\Videos"))


def convert_files():
    files = os.listdir(INPUT_PATH)

    print_num_files_found(len(files))
    for file in files:
        dir_file = os.path.join(INPUT_PATH, file)
        if dir_file.lower().endswith(".mkv"):
            th_convert_to_mp4 = threading.Thread(target=convert_to_mp4, args=(dir_file.strip(),))
            th_convert_to_mp4.start()
            timer(th_convert_to_mp4)


def convert_to_mp4(mkv_file: str):
    basename = os.path.basename(mkv_file)
    name, _ = os.path.splitext(mkv_file)
    out_name = os.path.join(OUTPUT_PATH, os.path.basename(name) + ".mp4")
    try:
        print_conversion_start(basename)
        ffmpeg.input(mkv_file).output(out_name, crf=23, preset="superfast").run(
            quiet=True, overwrite_output=True
        )
        print_conversion_finished(basename, out_name)
    except ffmpeg.Error as e:
        print_error_occurred(e)


def timer(th_convert_to_mp4):
    start_time = time.time()
    print_timer_start(get_local_time())

    while th_convert_to_mp4.is_alive():
        elapsed_time = time.time() - start_time
        hours, minutes, seconds = get_hours_minutes_seconds(elapsed_time)
        print_elapsed_time(hours, minutes, seconds)
        time.sleep(0.1)

    elapsed_time = time.time() - start_time
    hours, minutes, seconds = get_hours_minutes_seconds(elapsed_time)
    print_conversion_finished_time(hours, minutes, seconds)
    print_timer_end(get_local_time())


def main():
    convert_files()


if __name__ == "__main__":
    main()

import os
import threading
import time

import ffmpeg

from ..messages.prints import *
from ..utils.time import get_hours_minutes_seconds, get_local_time


def convert_files(path: str):
    files = os.listdir(path)
    for file in files:
        dir_file = os.path.join(path, file)
        if dir_file.lower().endswith(".mkv"):
            th_convert_to_mp4 = threading.Thread(
                target=convert_to,
                args=(
                    dir_file.strip(),
                    path,
                ),
            )
            th_convert_to_mp4.start()
            timer(th_convert_to_mp4)


def convert_to(mkv_file: str, files: str) -> None:
    basename = os.path.basename(mkv_file)
    name, _ = os.path.splitext(mkv_file)
    out_name = os.path.join(files, os.path.basename(name) + ".mp4")
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

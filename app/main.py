import os
import threading
import time
from datetime import datetime

import ffmpeg
from dotenv import load_dotenv

from .messages.prints import *


def convert_files():
    dir_input_files = os.getenv("DIR_INPUT_FILES")
    files = os.listdir(dir_input_files)

    print_num_files_found(len(files))
    for file in files:
        dir_file = os.path.join(dir_input_files, file)
        if dir_file.lower().endswith(".mkv"):
            th_convert_to_mp4 = threading.Thread(target=convert_to_mp4, args=(dir_file.strip(),))
            th_convert_to_mp4.start()
            timer(th_convert_to_mp4)


def convert_to_mp4(mkv_file: str):
    basename = os.path.basename(mkv_file)
    name, _ = os.path.splitext(mkv_file)
    output_folder = os.getenv("DIR_OUTPUT_FILES")
    out_name = os.path.join(output_folder, os.path.basename(name) + ".mp4")
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


def get_hours_minutes_seconds(time: float):
    hours, rem = divmod(time, 3600)
    minutes, seconds = divmod(rem, 60)
    return hours, minutes, seconds


def get_local_time() -> str:
    local_time = datetime.now()
    return local_time.strftime("%H:%M:%S")


def main():
    load_dotenv()
    convert_files()


if __name__ == "__main__":
    main()

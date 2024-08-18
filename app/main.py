import os
import threading
import time

import ffmpeg
from colorama import Fore
from dotenv import load_dotenv


def convert_files():
    dir_input_files = os.getenv("DIR_INPUT_FILES")
    for file in os.listdir(dir_input_files):
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
        print(f"{Fore.YELLOW} Converting {basename} to .mp4")
        ffmpeg.input(mkv_file).output(out_name).run(quiet=True, overwrite_output=True)
        print(f"{Fore.GREEN}Finished converting {basename} to {out_name}")
    except ffmpeg.Error as e:
        print(f"{Fore.RED}Error occurred: {e}")


def timer(th_convert_to_mp4):
    start_time = time.time()

    while th_convert_to_mp4.is_alive():
        elapsed_time = time.time() - start_time
        print(f"Time: {elapsed_time:.2f}", end="\r")
        time.sleep(0.1)

    elapsed_time = time.time() - start_time
    print(f"Conversion finished! elapsed time: {elapsed_time:.2f}")


def main():
    load_dotenv()
    convert_files()


if __name__ == "__main__":
    main()

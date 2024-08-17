import os

import ffmpeg
from dotenv import load_dotenv


def convert_files():
    dir_input_files = os.getenv("DIR_INPUT_FILES")
    for file in os.listdir(dir_input_files):
        dir_file = os.path.join(dir_input_files, file)
        if dir_file.lower().endswith(".mkv"):
            convert_to_mp4(dir_file.strip())


def convert_to_mp4(mkv_file: str):
    name, _ = os.path.splitext(mkv_file)
    output_folder = os.getenv("DIR_OUTPUT_FILES")
    out_name = os.path.join(output_folder, os.path.basename(name) + ".mp4")
    try:
        print(f"Converting {name} to .mp4")
        ffmpeg.input(mkv_file).output(out_name).run(quiet=True, overwrite_output=True)
        print(f"Finished converting {mkv_file} to {out_name}")
    except ffmpeg.Error as e:
        print(f"Error occurred: {e}")


def main():
    load_dotenv()
    convert_files()


if __name__ == "__main__":
    main()

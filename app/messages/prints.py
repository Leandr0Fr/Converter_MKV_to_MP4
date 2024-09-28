from colorama import Fore


def print_conversion_start(basename: str) -> None:
    print(f"{Fore.YELLOW} Converting {basename} to .mp4")


def print_conversion_finished(basename: str, out_name: str) -> None:
    print(f" {Fore.GREEN} Finished! {basename} to {out_name}")


def print_error_occurred(error: str):
    print(f" {Fore.RED}Error occurred: {error}")


def print_timer_start(local_time: float) -> None:
    print(f" {Fore.LIGHTCYAN_EX}Started at: {local_time}")


def print_elapsed_time(hours: float, minutes: float, seconds: float) -> None:
    print(f" {Fore.YELLOW}Time: {int(hours):02}:{int(minutes):02}:{int(seconds):02}", end="\r")


def print_conversion_finished_time(hours: float, minutes: float, seconds: float) -> None:
    print(
        f" {Fore.GREEN}Conversion finished! Elapsed time: {int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    )


def print_timer_end(local_time: str) -> None:
    print(f"{Fore.LIGHTCYAN_EX} Finished at: {local_time}\n")


def print_no_parameter() -> None:
    print(f"{Fore.LIGHTCYAN_EX} Please provide an argument.")

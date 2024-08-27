import sys

from ..ffmpeg.converter import convert
from ..utils.console import clear_console
from .prints import *


def menu() -> None:
    print_tittle()
    print_options_menu()
    user_input = int(input("Ingrese su opción: "))
    clear_console()
    if user_input == 1:
        converter_menu()
    elif user_input == 2:
        print("reduce")
    elif user_input == 3:
        print("audio")
    elif user_input == 4:
        print("view")
    elif user_input == 0:
        sys.exit()
    else:
        default_menu()


def default_menu() -> None:
    clear_console()
    print_error()
    menu()


def converter_menu() -> None:
    print_options_converter()
    user_input = int(input("Ingrese su opción: "))
    if user_input >= 1 and 7 <= user_input:
        convert(user_input)
    elif user_input == 0:
        sys.exit()
    else:
        default_converter()


def default_converter() -> None:
    clear_console()
    print_error()
    converter_menu()

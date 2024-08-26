import sys

from ..utils.console import clear_console
from .prints import *


def menu():
    print_tittle()
    print_options_menu()
    user_input = int(input("Ingrese su opción: "))
    if user_input == 1:
        print("converter")
    elif user_input == 2:
        print("reduce")
    elif user_input == 3:
        print("audio")
    elif user_input == 4:
        print("view")
    elif user_input == 0:
        sys.exit()
    else:
        default()


def default():
    clear_console()
    print_error()
    menu()

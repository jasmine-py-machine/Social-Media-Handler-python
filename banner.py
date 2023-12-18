from colorama import Fore,Back,Style
import shutil
def banner(info:str):
    print(f"{Fore.GREEN}")
    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄".center(shutil.get_terminal_size().columns))
    print("█████░█░▄▄▀██░▄▄▄░██░▄▀▄░█▄░▄██░▀██░██░▄▄▄████░▄▄▀█░▄▄▀██░▄▄▀██░██░██░▄▄▀█▄░▄".center(shutil.get_terminal_size().columns))
    print("█████░█░▀▀░██▄▄▄▀▀██░█░█░██░███░█░█░██░▄▄▄████░▄▄▀█░▀▀░██░▀▀▄██░▄▄░██░██░██░█".center(shutil.get_terminal_size().columns))
    print("██░▀▀░█░██░██░▀▀▀░██░███░█▀░▀██░██▄░██░▀▀▀████░▀▀░█░██░██░██░██░██░██░▀▀░█▀░▀".center(shutil.get_terminal_size().columns))
    print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀".center(shutil.get_terminal_size().columns))
    print(Fore.RESET)
    print(info.rjust(shutil.get_terminal_size().columns-30)," ")
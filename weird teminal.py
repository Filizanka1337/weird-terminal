import os
import platform
import webbrowser
import pyautogui
import time
import subprocess

def print_green(text):
    print("\033[92m" + text + "\033[0m")

def install_package(package):
    print_green(f"Installing {package}...")
    subprocess.check_call(["pip", "install", package])

def check_dependencies():
    try:
        import pyautogui
    except ImportError:
        install_package("pyautogui")

def parrot():
    os.system("curl parrot.live")

def clear_terminal():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def execute_command(command):
    if command == "exit":
        return False
    elif command == "parrot":
        parrot()
    elif command == "clear":
        clear_terminal()
    elif command == "tweaker-1":
        run_tweaker_command()
    elif command == "matrix":
        run_matrix_command()
    elif command == "smh-coll":
        run_smh_coll_command()
    elif command == "starwars":
        run_starwars_command()
    elif command == "ponk":
        run_ponk_command()
    elif command == "antivirus":
        run_antivirus_command()
    elif command == "a-z":
        run_a_to_z_command()
    elif command == "pacman":
        run_pacman_command()
    elif command == "windows-watermark":
        run_windows_watermark_command()
    elif command == "heart":
        run_heart_command()
    else:
        print(f"Unknown command: {command}")
    return True

def run_tweaker_command():
    print_green("Executing tweaker-1 command...")
    # Dodaj swoje polecenia związane z komendą tweaker-1

def run_matrix_command():
    print_green("Executing matrix command...")
    duration = int(input("Enter the duration in seconds: "))
    print_green("Welcome to the Matrix!")
    print_green("Follow the white rabbit.")
    time.sleep(1)
    clear_terminal()
    for _ in range(duration):
        print_green("".join(["".join(["0" if i % 2 == 0 else "1" for i in range(80)]) for _ in range(24)]))
        time.sleep(1)
        clear_terminal()

def run_smh_coll_command():
    print_green("Executing smh-coll command...")
    os.system("start cmd /k telnet telehack.com")

def run_starwars_command():
    print_green("Executing starwars command...")
    os.system("start cmd /k telnet telehack.com")
    time.sleep(2)
    pyautogui.typewrite("starwars")
    pyautogui.press("enter")

def run_ponk_command():
    print_green("Executing ponk command...")
    os.system("start cmd /k telnet telehack.com")
    time.sleep(2)
    pyautogui.typewrite("pong")
    pyautogui.press("enter")

def run_antivirus_command():
    print_green("Executing antivirus command...")
    if platform.system() == "Windows":
        os.system("start mrt")
    else:
        print("The 'antivirus' command is only available on Windows.")

def run_a_to_z_command():
    print_green("Executing a-z command...")
    webbrowser.open("https://www.play-games.com/game/15722/az.html")

def run_pacman_command():
    print_green("Executing pacman command...")
    webbrowser.open("https://pacman.cc/")

def run_windows_watermark_command():
    print_green("Executing windows-watermark command...")
    if platform.system() == "Windows":
        os.system("powershell -command \"Start-Process cmd -ArgumentList '/c bcdedit -set TESTSIGNING OFF' -Verb RunAs\"")
    else:
        print("The 'windows-watermark' command is only available on Windows.")

def run_heart_command():
    print_green("Executing heart command...")
    duration = int(input("Enter the duration in seconds: "))
    print_green("Get ready for a heart show!")
    time.sleep(1)
    clear_terminal()
    colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m", "\033[95m", "\033[96m"]
    for _ in range(duration):
        for color in colors:
            print(color + "♥", end="")
        print("\033[0m")
        time.sleep(0.5)
        clear_terminal()

def check_dependencies_and_run():
    check_dependencies()
    clear_terminal()
    os.system("color")  # Ustawienie koloru na zielony w systemie Windows

    commands = ["exit", "parrot", "clear", "tweaker-1", "matrix", "smh-coll", "starwars", "ponk", "antivirus", "a-z", "pacman", "windows-watermark", "heart"]

    print_green("Welcome!")
    print_green("Enter 'exit' to exit.")
    print_green("Available commands:")
    for cmd in commands:
        print_green(cmd)

    while True:
        command = input("Enter a command: ")
        if not execute_command(command):
            break

    print_green("Goodbye!")

check_dependencies_and_run()

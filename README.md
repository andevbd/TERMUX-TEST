<div align="center">

# ⚡ UNIVERSAL PACKAGE MANAGER v4.0

![Python Version](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white)
![Termux](https://img.shields.io/badge/Termux-Android-orange?logo=android&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-10%2B-0078D6?logo=windows&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-All%20Distros-FCC624?logo=linux&logoColor=white)
![macOS](https://img.shields.io/badge/macOS-10.15%2B-000000?logo=apple&logoColor=white)
![VPS](https://img.shields.io/badge/VPS-Cloud%20Ready-4285F4?logo=googlecloud&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?logo=opensourceinitiative&logoColor=white)
![Size](https://img.shields.io/badge/Size-48KB-lightgrey)
![Downloads](https://img.shields.io/badge/Downloads-10K%2B-brightgreen)

**One Tool. All Platforms. Zero Hassle.**

[![Run on Repl.it](https://repl.it/badge/github/andevbd/TERMUX-TEST)](https://repl.it/github/andevbd/TERMUX-TEST)
[![Open in GitHub Codespaces](https://img.shields.io/badge/Open%20in-Codespaces-181717?logo=github)](https://github.com/codespaces/new?repo=andevbd/TERMUX-TEST)

</div>

---

## 📑 সূচিপত্র

- [📖 ভূমিকা](#-ভূমিকা)
- [🎯 সাপোর্টেড প্ল্যাটফর্ম](#-সাপোর্টেড-প্ল্যাটফর্ম)
- [📥 ইনস্টলেশন গাইড](#-ইনস্টলেশন-গাইড)
  - [📱 Termux (Android)](#-termux-android)
  - [🐧 Linux](#-linux)
  - [🪟 Windows](#-windows)
  - [🍎 macOS](#-macos)
  - [☁️ VPS/Cloud](#️-vpscloud)
  - [🍓 Raspberry Pi](#-raspberry-pi)
  - [🐳 Docker](#-docker)
- [🎮 ব্যবহার](#-ব্যবহার)
- [📸 আউটপুট উদাহরণ](#-আউটপুট-উদাহরণ)
- [🛠️ প্যাকেজ তালিকা](#️-প্যাকেজ-তালিকা)
- [🔧 ট্রাবলশুটিং](#-ট্রাবলশুটিং)
- [❓ FAQ](#-faq)
- [📞 যোগাযোগ](#-যোগাযোগ)

---

## 📖 ভূমিকা

**Universal Package Manager** একটি আধুনিক, দ্রুত এবং ক্রস-প্ল্যাটফর্ম প্যাকেজ ম্যানেজার যা যেকোনো ডিভাইসে কাজ করে।

### ✨ বৈশিষ্ট্যসমূহ

| বৈশিষ্ট্য | বর্ণনা |
|-----------|---------|
| 🎨 **বিউটিফুল UI** | কালারফুল আউটপুট, প্রোগ্রেস বার |
| 🚀 **দ্রুতগতি** | সমান্তরাল ডাউনলোড |
| 🔧 **অটো ডিপেন্ডেন্সি** | দরকারি প্যাকেজ নিজেই ইন্সটল করে |
| 💾 **হালকা** | মাত্র 48KB |
| 🌍 **ক্রস-প্ল্যাটফর্ম** | Termux, Linux, Windows, macOS, VPS |
| 📦 **বিশাল রিপোজিটরি** | 3000+ প্যাকেজ |

---

## 🎯 সাপোর্টেড প্ল্যাটফর্ম

| প্ল্যাটফর্ম | ভার্সন | স্ট্যাটাস |
|--------------|---------|-----------|
| 📱 Termux | Latest | ✅ |
| 🐧 Ubuntu | 20.04, 22.04, 24.04 | ✅ |
| 🐧 Debian | 11, 12 | ✅ |
| 🐧 Kali Linux | 2024.x | ✅ |
| 🐧 Arch Linux | Latest | ✅ |
| 🐧 Fedora | 38, 39, 40 | ✅ |
| 🪟 Windows 10 | 22H2 | ✅ |
| 🪟 Windows 11 | 23H2+ | ✅ |
| 🍎 macOS | Ventura, Sonoma | ✅ |
| ☁️ DigitalOcean | Ubuntu 22.04 | ✅ |
| ☁️ AWS EC2 | Ubuntu 22.04 | ✅ |
| ☁️ Google Cloud | Debian 12 | ✅ |
| 🍓 Raspberry Pi | Bookworm | ✅ |
| 🐳 Docker | Latest | ✅ |

---

## 📥 ইনস্টলেশন গাইড

### 📱 Termux (Android)

```bash
# Termux আপডেট করুন
pkg update && pkg upgrade -y

# Python ও টুলস ইনস্টল করুন
pkg install python python-pip curl wget git -y

# পদ্ধতি ১: ওয়ান-লাইনার
curl -sSL https://raw.githubusercontent.com/andevbd/TERMUX-TEST/main/tst.py | python

# পদ্ধতি ২: গিট ক্লোন
git clone https://github.com/andevbd/TERMUX-TEST.git
cd TERMUX-TEST
python tst.py

# পদ্ধতি ৩: গ্লোবাল ইনস্টল
cp tst.py $PREFIX/bin/pkg-manager
chmod +x $PREFIX/bin/pkg-manager
pkg-manager

# স্টোরেজ পারমিশন (যদি দরকার হয়)
termux-setup-storage


---

🐧 Linux

Ubuntu / Debian / Kali / Linux Mint / Pop!_OS

```bash
# সিস্টেম আপডেট
sudo apt update && sudo apt upgrade -y

# Python ও টুলস
sudo apt install python3 python3-pip curl wget git -y

# পদ্ধতি ১: ওয়ান-লাইনার
curl -sSL https://raw.githubusercontent.com/andevbd/TERMUX-TEST/main/tst.py | python3

# পদ্ধতি ২: গিট ক্লোন
git clone https://github.com/andevbd/TERMUX-TEST.git
cd TERMUX-TEST
python3 tst.py

# পদ্ধতি ৩: গ্লোবাল ইনস্টল
sudo cp tst.py /usr/local/bin/pkg-manager
sudo chmod +x /usr/local/bin/pkg-manager
pkg-manager
```

Arch Linux / Manjaro

```bash
sudo pacman -Syu
sudo pacman -S python python-pip curl wget git
curl -sSL https://raw.githubusercontent.com/andevbd/TERMUX-TEST/main/tst.py | python
```

Fedora / RHEL / CentOS

```bash
sudo dnf update -y
sudo dnf install python3 python3-pip curl wget git -y
curl -sSL https://raw.githubusercontent.com/andevbd/TERMUX-TEST/main/tst.py | python3
```

---

🪟 Windows

পূর্বশর্ত: Python ইনস্টল করুন (python.org থেকে)

পদ্ধতি ১: পাওয়ারশেল (এডমিন)

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Invoke-Expression (Invoke-WebRequest -Uri "https://raw.githubusercontent.com/andevbd/TERMUX-TEST/main/tst.py" -UseBasicParsing).Content
```

পদ্ধতি ২: কমান্ড প্রম্পট (এডমিন)

```cmd
curl -O https://raw.githubusercontent.com/andevbd/TERMUX-TEST/main/tst.py
python tst.py
```

পদ্ধতি ৩: গিট ব্যাশ

```bash
git clone https://github.com/andevbd/TERMUX-TEST.git
cd TERMUX-TEST
python tst.py
```

পদ্ধতি ৪: ব্যাচ ফাইল তৈরি

```batch
@echo off
echo Starting Universal Package Manager...
python "%~dp0tst.py"
pause
```

---

🍎 macOS

Intel Mac এবং Apple Silicon (M1/M2/M3)

```bash
# হোমব্রু ইনস্টল করুন (যদি না থাকে)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Python ও টুলস
brew install python@3.11 curl wget git

# পদ্ধতি ১: ওয়ান-লাইনার
curl -sSL https://raw.githubusercontent.com/andevbd/TERMUX-TEST/main/tst.py | python3

# পদ্ধতি ২: গিট ক্লোন
git clone https://github.com/andevbd/TERMUX-TEST.git
cd TERMUX-TEST
python3 tst.py

# পদ্ধতি ৩: গ্লোবাল ইনস্টল
sudo cp tst.py /usr/local/bin/pkg-manager
sudo chmod +x /usr/local/bin/pkg-manager
pkg-manager

# Xcode Command Line Tools (যদি দরকার হয়)
xcode-select --install
```

---

☁️ VPS/Cloud

সকল VPS প্রোভাইডারের জন্য (DigitalOcean, AWS, GCP, Linode, Vultr)

```bash
# SSH দিয়ে কানেক্ট করুন
ssh root@your-vps-ip

# সিস্টেম আপডেট
sudo apt update && sudo apt upgrade -y

# Python ও টুলস
sudo apt install python3 python3-pip curl wget git -y

# ডাউনলোড ও রান
cd /opt
sudo git clone https://github.com/andevbd/TERMUX-TEST.git
cd TERMUX-TEST
sudo python3 tst.py
```

ব্যাকগ্রাউন্ডে রান করানো (ডিসকানেক্ট後ও চলবে)

```bash
# পদ্ধতি ১: nohup
nohup python3 tst.py > output.log 2>&1 &
tail -f output.log  # লগ দেখতে

# পদ্ধতি ২: screen
screen -S pkg-manager
python3 tst.py
# Ctrl+A, D প্রেস করুন (ডিটাচ)
screen -r pkg-manager  # রিঅ্যাটাচ করতে

# পদ্ধতি ৩: tmux
tmux new -s pkg-manager
python3 tst.py
# Ctrl+B, D প্রেস করুন (ডিটাচ)
tmux attach -t pkg-manager  # রিঅ্যাটাচ করতে
```

সিস্টেমড সার্ভিস (অটোস্টার্ট)

```bash
sudo nano /etc/systemd/system/pkg-manager.service
```

```ini
[Unit]
Description=Universal Package Manager
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/TERMUX-TEST
ExecStart=/usr/bin/python3 /opt/TERMUX-TEST/tst.py
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable pkg-manager
sudo systemctl start pkg-manager
sudo systemctl status pkg-manager
```

---

🍓 Raspberry Pi

```bash
# সিস্টেম আপডেট
sudo apt update && sudo apt upgrade -y

# Python ও টুলস
sudo apt install python3 python3-pip curl wget git -y

# ক্লোন ও রান
git clone https://github.com/andevbd/TERMUX-TEST.git
cd TERMUX-TEST
python3 tst.py
```

---

🐳 Docker

Dockerfile

```dockerfile
FROM python:3.11-slim

RUN apt update && apt install -y \
    curl wget git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/andevbd/TERMUX-TEST.git /app
WORKDIR /app

CMD ["python", "tst.py"]
```

বিল্ড ও রান

```bash
# ইমেজ বিল্ড
docker build -t pkg-manager .

# কন্টেইনার রান (ইন্টারএক্টিভ)
docker run -it pkg-manager

# ব্যাকগ্রাউন্ডে রান
docker run -d --name pkg-manager pkg-manager

# লগ দেখতে
docker logs -f pkg-manager
```

ডকার কম্পোজ

```yaml
# docker-compose.yml
version: '3.8'
services:
  pkg-manager:
    build: .
    container_name: pkg-manager
    stdin_open: true
    tty: true
    restart: unless-stopped
```

```bash
docker-compose up -d
docker-compose logs -f
```

---

🎮 ব্যবহার

```bash
# টুল রান করুন
python tst.py

# গ্লোবাল ইনস্টল করলে
pkg-manager
```

কীবোর্ড শর্টকাট

শর্টকাট কাজ
Ctrl+C বন্ধ করুন
Enter কন্টিনিউ

আর্গুমেন্টস

```bash
python tst.py --force-update   # ফোর্স আপডেট
python tst.py --no-update      # আপডেট চেক স্কিপ
python tst.py --debug          # ডিবাগ মোড
python tst.py --help           # হেল্প
```

---

📸 আউটপুট উদাহরণ

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║      ████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗                   ║
║      ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║╚██╗██╔╝                   ║
║         ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║ ╚███╔╝                    ║
║         ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║ ██╔██╗                    ║
║         ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗                    ║
║         ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝                    ║
║                                                                              ║
║                    UNIVERSAL PACKAGE MANAGER v4.0                            ║
║                    [✓] System Ready                                          ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────────┐
│ ▶ SYSTEM INITIALIZATION                                                     │
└─────────────────────────────────────────────────────────────────────────────┘

  [✓] Python version: 3.11.2
  [✓] Architecture: x86_64
  [✓] Internet: Connected

┌─────────────────────────────────────────────────────────────────────────────┐
│ ▶ PACKAGE MANAGEMENT                                                        │
└─────────────────────────────────────────────────────────────────────────────┘

  [>] Checking repositories...
  [✓] Found 24 new packages

  📦 [1/24] python3-core_3.11.2_amd64.deb
     ├── Size: 45.3 MB
     ├── Progress: [████████████████████████████░░░░░░░░] 67.2% (12s)
     └── Status: ✓ Downloaded

  [✓] All packages installed successfully!
```

---

🛠️ প্যাকেজ তালিকা

ক্যাটাগরি প্যাকেজসমূহ
📝 ডেভেলপমেন্ট python, nodejs, ruby, golang, rust, openjdk, php
🔧 টুলস git, curl, wget, vim, nano, htop, tree, ffmpeg
🗄️ ডাটাবেস mysql, postgresql, redis, mongodb, sqlite3
🌐 ওয়েব nginx, apache2, apache-tomcat
🔒 সিকিউরিটি openssl, nmap, wireshark, hydra

---

🔧 ট্রাবলশুটিং

❌ 'python' কমান্ড কাজ করছে না

```bash
# Windows: Python PATH চেক করুন
where python

# Linux/macOS: python3 ব্যবহার করুন
python3 tst.py

# Termux: Python ইনস্টল করুন
pkg install python
```

❌ পারমিশন ডিনাইড

```bash
chmod +x tst.py
sudo python3 tst.py
```

❌ নেটওয়ার্ক এরর

```bash
ping google.com
export HTTP_PROXY=http://proxy:8080
```

---

❓ FAQ

📱 Termux এ কাজ করে?
হ্যাঁ, F-Droid থেকে Termux ইনস্টল করুন।

🪟 Windows 7 এ কাজ করবে?
Windows 10+ রেকমেন্ডেড।

🍓 Raspberry Pi Zero তে?
হ্যাঁ, কিন্তু ধীর গতিতে। Pi 3/4/5 ভালো।

☁️ ফ্রি VPS এ কাজ করবে?
হ্যাঁ, AWS Free Tier, GCP Free Tier সব কাজ করে।

🔒 এটা কি নিরাপদ?
হ্যাঁ, কোড ওপেন সোর্স।

---

📞 যোগাযোগ

প্ল্যাটফর্ম লিংক
🐙 GitHub github.com/andevbd
💬 টেলিগ্রাম @andevbd
✉️ ইমেইল andevbd@gmail.com

---

📜 লাইসেন্স

```
MIT License

Copyright (c) 2024 andevbd

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

<div align="center">

⭐ Star এই রিপোজিটরিটি যদি উপকারে আসে!

⬆️ Back to Top

</div>
```

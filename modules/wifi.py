import os
import subprocess
import qrcode
import socket
import requests
from tabulate import tabulate

# ================================
# RAJA ASCII BANNER
# ================================
def banner():
    print("\n" + "=" * 45)
    print("        🔥 RAJA-X WIFI SCANNER 🔥")
    print("=" * 45 + "\n")

# ================================
# GET CONNECTED WIFI NAME
# ================================
def get_wifi_name():
    try:
        result = subprocess.check_output("netsh wlan show interfaces", shell=True).decode()
        for line in result.split("\n"):
            if "SSID" in line and "BSSID" not in line:
                return line.split(":")[1].strip()
    except:
        pass
    return "Unknown"

# ================================
# GET WIFI PASSWORD
# ================================
def get_wifi_password(wifi):
    try:
        cmd = f'netsh wlan show profile name="{wifi}" key=clear'
        result = subprocess.check_output(cmd, shell=True).decode()

        for line in result.split("\n"):
            if "Key Content" in line:
                return line.split(":")[1].strip()
    except:
        pass
    return None

# ================================
# LOCAL IP
# ================================
def local_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "Unknown"

# ================================
# PUBLIC IP
# ================================
def public_ip():
    try:
        return requests.get("https://api64.ipify.org").text
    except:
        return "Unknown"

# ================================
# GATEWAY
# ================================
def get_gateway():
    try:
        out = subprocess.check_output("ipconfig", shell=True).decode()
        for line in out.split("\n"):
            if "Default Gateway" in line and ":" in line:
                return line.split(":")[1].strip()
    except:
        pass
    return "Unknown"

# ================================
# SCAN DEVICES (PING SWEEP)
# ================================
def scan_devices(gateway_ip):
    print("\n🔎 Scanning Devices... (3–6 sec)\n")
    base = gateway_ip.rsplit(".", 1)[0] + "."
    found = []

    for i in range(1, 20):
        ip = base + str(i)
        output = subprocess.call(f"ping -n 1 -w 200 {ip}", stdout=subprocess.DEVNULL)
        if output == 0:
            found.append(ip)

    return found

# ================================
# SMALL & CLEAN TERMINAL QR CODE
# ================================
def print_terminal_qr(text):
    qr = qrcode.QRCode(version=1, box_size=1, border=1)
    qr.add_data(text)
    qr.make()

    matrix = qr.get_matrix()
    print("\n")
    for row in matrix:
        print("".join(["██" if cell else "  " for cell in row]))
    print("\n        🔥 RAJA-X WIFI QR 🔥\n")

# ================================
# MAIN PROGRAM
# ================================
banner()

wifi = get_wifi_name()
password = get_wifi_password(wifi)
local = local_ip()
public = public_ip()
gateway = get_gateway()

print("📶 WiFi Name:", wifi)
print("🔑 Password :", password if password else "❌ Not Found")
print("💻 Local IP :", local)
print("🌍 Public IP:", public)
print("🌐 Gateway  :", gateway)

# QR CODE CONNECT TEXT
wifi_qr = f"WIFI:T:WPA;S:{wifi};P:{password};;;"

print("\n📲 WIFI QR (Scan to Connect)")
print_terminal_qr(wifi_qr)

# SCAN DEVICES
if gateway != "Unknown":
    devices = scan_devices(gateway)
    print("📡 Devices Found:")
    print(tabulate([[i + 1, ip] for i, ip in enumerate(devices)],
                   ["No.", "IP"], tablefmt="grid"))
else:
    print("❌ Gateway not found — cannot scan.\n")

print("\n🔥 SCAN COMPLETE — RAJA-X TOOLKIT READY 🔥\n")

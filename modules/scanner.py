import subprocess
import platform
import shutil
import os

print("====================================")
print("        Universal Nmap Scanner")
print("  Works on Windows / Linux / Termux ")
print("====================================")

site = input("Enter website or IP: ")

print("\nScanning... Please wait...\n")

try:
    system_os = platform.system().lower()

    # -------------------------------------
    # WINDOWS LOGIC
    # -------------------------------------
    if system_os == "windows":
        # Try to find nmap from PATH
        nmap_path = shutil.which("nmap.exe")

        # If not in PATH, try default installation directory
        if not nmap_path:
            default_path = r"C:\Program Files (x86)\Nmap\nmap.exe"
            if os.path.exists(default_path):
                nmap_path = default_path
            else:
                raise FileNotFoundError

        nmap_cmd = [nmap_path, site]

    # -------------------------------------
    # LINUX / TERMUX LOGIC
    # -------------------------------------
    else:
        nmap_path = shutil.which("nmap")
        if not nmap_path:
            raise FileNotFoundError

        nmap_cmd = [nmap_path, site]

    # -------------------------------------
    # RUNNING NMAP
    # -------------------------------------
    result = subprocess.run(nmap_cmd, capture_output=True, text=True)

    print("====================================")
    print("             SCAN RESULT")
    print("====================================\n")

    print(result.stdout)

except FileNotFoundError:
    print("❌ ERROR: Nmap not installed or not found!")
    print("\nInstall Nmap according to your device:\n")
    print("✔ Windows: Install from https://nmap.org/download.html")
    print("✔ Termux : pkg install nmap")
    print("✔ Linux  : sudo apt install nmap")

except Exception as e:
    print("\n❌ Unexpected Error:", e)

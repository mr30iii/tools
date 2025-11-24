import platform
import psutil
import socket
import os
import subprocess

def get_battery():
    try:
        batt = psutil.sensors_battery()
        if batt:
            return f"{batt.percent}% ({'Charging' if batt.power_plugged else 'Not Charging'})"
        else:
            return "Battery info not available"
    except:
        return "Battery info not supported"

def get_android_props():
    props = {}
    commands = {
        "Model": "getprop ro.product.model",
        "Brand": "getprop ro.product.brand",
        "Android": "getprop ro.build.version.release",
        "CPU ABI": "getprop ro.product.cpu.abi"
    }

    for key, cmd in commands.items():
        try:
            result = subprocess.check_output(cmd.split()).decode().strip()
            props[key] = result if result else "N/A"
        except:
            props[key] = "N/A"

    return props

print("\n========== DEVICE INFORMATION ==========\n")
print(f"System: {platform.system()}")
print(f"OS Version: {platform.version()}")
print(f"Machine: {platform.machine()}")
print(f"Processor: {platform.processor()}\n")

print("========== HARDWARE ==========")
print(f"CPU Cores: {psutil.cpu_count(logical=True)}")
print(f"RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")
print(f"Storage: {round(psutil.disk_usage('/').total / (1024**3), 2)} GB\n")

print("========== NETWORK ==========")
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print(f"Hostname: {hostname}")
print(f"Local IP: {ip}\n")

print("========== BATTERY ==========")
print(f"Battery: {get_battery()}\n")

print("========== ANDROID (If Running on Android) ==========")
android = get_android_props()
for key, value in android.items():
    print(f"{key}: {value}")

print("\n=========================================\n")


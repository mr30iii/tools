import requests
import json
import sys

print("\n🔥 RAJA-X ADVANCED IP LOOKUP TOOL 🔥\n")

ip = input("🌐 Enter IP Address: ")

url = f"http://ip-api.com/json/{ip}?fields=66846719"

try:
    res = requests.get(url, timeout=5)
    data = res.json()

    if data["status"] != "success":
        print("\n❌ Invalid IP or Lookup Failed!")
        sys.exit()

    print("\n===============================")
    print("      📍 IP INFORMATION")
    print("===============================\n")

    print(f"IP Address:        {data.get('query')}")
    print(f"Country:           {data.get('country')} ({data.get('countryCode')})")
    print(f"Region:            {data.get('regionName')}")
    print(f"City:              {data.get('city')}")
    print(f"ZIP:               {data.get('zip')}")
    print(f"Timezone:          {data.get('timezone')}")
    print(f"ISP:               {data.get('isp')}")
    print(f"Organization:      {data.get('org')}")
    print(f"AS:                {data.get('as')}")
    print(f"Mobile Network:    {data.get('mobile')}")
    print(f"Proxy / VPN:       {data.get('proxy')}")
    print(f"Hosting:           {data.get('hosting')}")

    lat = data.get("lat")
    lon = data.get("lon")

    print(f"Latitude:          {lat}")
    print(f"Longitude:         {lon}")

    print("\n📌 Google Maps Link:")
    print(f"https://www.google.com/maps?q={lat},{lon}")

    print("\n===============================")
    print("       ✔ Lookup Complete")
    print("===============================\n")

except Exception as e:
    print("\n❌ Error occurred!")
    print("Reason:", e)

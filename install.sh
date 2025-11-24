#!/bin/bash

clear
echo -e "\e[32m[+] Installing RAJA-X-TOOL...\e[0m"

pkg update -y
pkg upgrade -y
pkg install python git bash openssl wget curl -y

pip install requests

chmod +x raja-x-tool.sh
chmod +x modules/*

echo -e "\e[32m[+] Installation Complete!"
echo -e "Run tool using: \e[33m./raja-x-tool.sh\e[0m"

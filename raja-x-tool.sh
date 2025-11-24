#!/bin/bash

RED='\033[1;31m'
GREEN='\033[1;32m'
CYAN='\033[1;36m'
NC='\033[0m'

MODULE_DIR="modules"

print_header() {
    clear
    echo -e "${CYAN}"
    echo "═══════════════════════════════════════"
    echo
    echo "        🔥 RAJA-X TOOLS LAUNCHER 🔥"
    echo "═══════════════════════════════════════"
    echo -e "${NC}"
}

detect_python() {
    if command -v python3 >/dev/null 2>&1; then
        echo "python3"
    elif command -v python >/dev/null 2>&1; then
        echo "python"
    else
        echo "python" # fallback - will error if not installed
    fi
}

while true; do
    # build list of python modules
    mapfile -t py_files < <(ls -1 "$MODULE_DIR"/*.py 2>/dev/null || true)

    print_header

    if [ ${#py_files[@]} -eq 0 ]; then
        echo "No Python modules found in '$MODULE_DIR'."
        echo "Make sure the folder contains .py files."
        echo
        read -p "Press Enter to refresh or Ctrl+C to exit..."
        continue
    fi

    echo -e "Available Python Modules:\n"
    for i in "${!py_files[@]}"; do
        idx=$((i+1))
        base=$(basename "${py_files[$i]}")
        echo -e "[${idx}] ${base}"
    done
    echo -e "[0] Exit\n"

    read -p "Enter Choice (number): " ch

    if [[ "$ch" =~ ^0+$ ]]; then
        exit 0
    fi

    if ! [[ "$ch" =~ ^[0-9]+$ ]]; then
        echo "Invalid input. Enter a number."; sleep 1; continue
    fi

    sel_index=$((ch-1))
    selected_file="${py_files[$sel_index]}"

    if [ -z "$selected_file" ]; then
        echo "Invalid Option!"; sleep 1; continue
    fi

    # show file content and run commands
    print_header
    echo "===== Module: $(basename "$selected_file") =====\n"
    echo "--- File content (first 400 lines) ---\n"
    sed -n '1,400p' "$selected_file" || true

    echo -e "\n--- Recommended Run Commands ---"
    echo "Linux / Termux   : python3 $selected_file"
    echo "Windows (PowerShell): python $selected_file"

    read -p "Run this module now? (y/N): " run_now
    run_now=${run_now:-N}

    if [[ "$run_now" =~ ^[Yy]$ ]]; then
        PYCMD=$(detect_python)
        echo "Running: $PYCMD \"$selected_file\""
        echo
        # run with same terminal so user sees output
        "$PYCMD" "$selected_file"
        echo
        echo "--- Module finished ---"
    fi

    read -p "Press Enter to return to menu..."
done

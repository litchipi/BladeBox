#!/bin/bash

tmpdir=$(mktemp -d)
cd $tmpdir

# Python3
if ! python3 --version 2>/dev/null
then
    echo "[*] Installing python3"
    sudo apt install python3
fi

# Bers3rk
if ! python3 -c "import berserk" 2>/dev/null
then
    echo "[*] Installing Bers3rk"
    git clone https://github.com/litchipi/Bers3rk
    cd ./Bers3rk
    sudo python3 ./setup.py install
    cd ..
fi

echo "[*] Installation complete"

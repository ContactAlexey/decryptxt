#!/bin/bash
set -e

chmod +x decryptxt.py
sudo cp decryptxt.py /usr/local/bin/decryptxt
sudo chmod +x /usr/local/bin/decryptxt

echo "decryptxt installed successfully."

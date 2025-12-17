#!/bin/bash

# Exit if any error occurs
set -e

# Make sure the scripts have execute permissions
chmod +x descryptxt.py

# Copy the scripts to /usr/local/bin without the .py extension
sudo cp descryptxt.py /usr/local/bin/descryptxt

# Make sure they can be executed from anywhere
sudo chmod +x /usr/local/bin/descryptxt

echo "descryptxt installed successfully. You can use them with the command 'descryptxt'."

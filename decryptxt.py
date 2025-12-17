#!/usr/bin/env python3

import os
import sys

def decrypt_file(file_name):
    file_path = os.path.abspath(file_name)

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    parts = content.split()
    if len(parts) < 2:
        raise ValueError("Invalid encrypted file.")

    # The last number is n_encryption
    n_encryption = int(parts[-1])
    numbers = parts[:-1]

    result = []
    for number in numbers:
        try:
            decimal_value = int(number) // n_encryption
            char = chr(decimal_value)
            result.append(char)
        except:
            raise ValueError(f"Could not decrypt value: {number}")

    decrypted_text = "".join(result)

    output_path = os.path.join(os.path.dirname(file_path), "decrypted_message.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(decrypted_text)

    return output_path

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: descryptxt <encrypted_file>")
        sys.exit(1)

    try:
        output = decrypt_file(sys.argv[1])
        print(f"Decryption completed: {output}")
    except Exception as e:
        print(f"Error: {e}")

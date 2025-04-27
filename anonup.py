#!/usr/bin/env python3

import argparse
import requests
import sys

def upload_file(file_path):
    url = 'https://www.anonfile.la/process/upload_chunk'

    headers = {
        'Host': 'www.anonfile.la',
        'Accept-Language': 'pt-BR,pt;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Origin': 'https://www.anonfile.la',
        'Referer': 'https://www.anonfile.la/',
    }

    try:
        with open(file_path, 'rb') as f:
            file_content = f.read()
    except FileNotFoundError:
        print(f"[!] Arquivo '{file_path}' não encontrado.")
        sys.exit(1)

    files = {
        'chunk': ('blob', file_content, 'application/octet-stream'),
    }

    data = {
        'chunk_index': '0',
        'total_chunks': '1',
        'file_id': 'Scr1pt by D4mCl0v3r',
        'file_name': file_path.split('/')[-1],
        'file_size': str(len(file_content)),
    }

    response = requests.post(url, headers=headers, files=files, data=data)

    if response.status_code == 200:
        result = response.json()
        if result.get('success'):
            print(f"[+] Uploaded")
            print(f"[+] Link: {result.get('url')}")
        else:
            print("[!] Error in upload:", result.get('message'))
    else:
        print(f"[!] HTTP error {response.status_code}")

def main():
    parser = argparse.ArgumentParser(
        description="Anonfile.la uploader - Made by DamClover@proton.me",
        epilog="e.g. python3 anon.py file.txt"
    )
    parser.add_argument('file', help='File to upload')

    args = parser.parse_args()

    upload_file(args.file)

if __name__ == "__main__":
    main()

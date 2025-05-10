#!/usr/bin/env python3

from bs4 import BeautifulSoup
import argparse
import requests
import sys

def upload_anonymous(file_path, use_tor=False):
    url = 'https://anonymousfiles.org/'
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    } if use_tor else None

    try:
        with open(file_path, 'rb') as f:
            files = {
                'file': (file_path, f),
            }
            data = {
                'upload_nonce_field': '0200b150b0',
                '_wp_http_referer': '/',
            }

            res = requests.post(url, data=data, files=files, proxies=proxies)
            soup = BeautifulSoup(res.text, 'html.parser')
            down_link = soup.find('link', rel='canonical')

            if res.status_code in [200, 302]:
                if down_link:
                    link = down_link.get('href')
                    if use_tor:
                        print("\n[+] Uploaded in anonymousfiles.org using Tor Proxy")
                        print(f"[+] Link: {link}")
                    else:
                        print("\n[+] Uploaded in anonymousfiles.org")
                        print(f"[+] Link: {link}")
                else:
                    print("[!] Error: No download link found in the response.")
            else:
                print(f"[!] Failed upload with status code: {res.status_code}")

    except FileNotFoundError:
        print(f"[!] File '{file_path}' not found.")
        sys.exit(1)

def upload_anonup(file_path, use_tor=False):
    url = 'https://www.anonfile.la/process/upload_chunk'
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    } if use_tor else None

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
        print(f"[!] File '{file_path}' not found.")
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

    response = requests.post(url, headers=headers, files=files, data=data, proxies=proxies)

    if response.status_code == 200:
        result = response.json()
        if result.get('success'):
            if use_tor:
                print("\n[+] Uploaded in anonymousfiles.org using Tor Proxy")
                print(f"[+] Link: {result.get('url')}")
            else:
                print("\n[+] Uploaded in anonymousfiles.org")
                print(f"[+] Link: {result.get('url')}")
        else:
            print("[!] Error in upload:", result.get('message'))
    else:
        print(f"[!] HTTP error {response.status_code}")

def main():
    parser = argparse.ArgumentParser(
        description="Anonymous uploader - Made by DamClover@proton.me",
        epilog="e.g. python3 anon.py file.txt -s 2 --tor"
    )
    parser.add_argument('file', help='File to upload')
    parser.add_argument('-s', '--system', type=int, choices=[1, 2], help='System to upload (e.g. 1: anonfile.la, 2: anonymousfiles.org)')
    parser.add_argument('--tor', action='store_true', help='Use Tor proxy for more anonymity (enable tor on your system)')

    args = parser.parse_args()

    if args.system == 1:
        upload_anonup(args.file, args.tor)
        
    elif args.system == 2:
        upload_anonymous(args.file, args.tor)
        
    else:
        upload_anonup(args.file, args.tor)

if __name__ == "__main__":
    main()

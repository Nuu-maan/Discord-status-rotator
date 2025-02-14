import requests
import json
import time
import threading
from data.logger import NovaLogger

from colorama import Fore, Style


banner = f"""
{Fore.CYAN}
                        █████▒██▓ ██▓     ██▓   ▓██   ██▓
                        ▓██   ▒▓██▒▓██▒    ▓██▒    ▒██  ██▒
                        ▒████ ░▒██▒▒██░    ▒██░     ▒██ ██░
                        ░▓█▒  ░░██░▒██░    ▒██░     ░ ▐██▓░
                        ░▒█░   ░██░░██████▒░██████▒ ░ ██▒▓░
                        ▒ ░   ░▓  ░ ▒░▓  ░░ ▒░▓  ░  ██▒▒▒ 
                        ░      ▒ ░░ ░ ▒  ░░ ░ ▒  ░▓██ ░▒░ 
                        ░ ░    ▒ ░  ░ ░     ░ ░   ▒ ▒ ░░  
                                ░      ░  ░    ░  ░░ ░     
                                                ░ ░     

                        {Fore.LIGHTCYAN_EX}https://discord.gg/api{Style.RESET_ALL}
"""




def load_tokens(file_path):
    tokens = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            if line.count(':') >= 2:
                tokens.append(line.split(':')[-1])
            else:
                tokens.append(line)
    return tokens

def load_proxies(file_path):
    proxies = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            if '@' in line and (':' in line or ';' in line):
                auth, hostport = line.split('@', 1)
                host, port = hostport.replace(';', ':').split(':', 1)
                proxy_url = f"http://{auth}@{host}:{port}"
                proxies.append({'http': proxy_url, 'https': proxy_url})
    return proxies

def load_statuses(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def update_status(token, proxy, status):
    headers = {
        'authorization': token,
        'content-type': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36'
    }
    try:
        response = requests.patch(
            'https://discord.com/api/v9/users/@me/settings', 
            headers=headers,
            json={'custom_status': {'text': status}},
            proxies=proxy,
            timeout=10
        )
        if response.status_code == 200:
            NovaLogger.win(f"Status updated: {status[:20]}...")
        else:
            NovaLogger.fail(f"Failed to update status: {response.status_code}", response=response.text)
    except requests.exceptions.RequestException as e:
        NovaLogger.fail(f"Connection error: {str(e)[:50]}")

def status_worker(token, proxy, statuses, interval):
    while True:
        for status in statuses:
            update_status(token, proxy, status)
            time.sleep(interval)

def main():
    NovaLogger.config(log_file="status_rotator.log")
    NovaLogger.note("Starting Discord Status Rotator")

    with open('config.json') as f:
        config = json.load(f)
        interval = config.get('interval', 60)
        proxyless = config.get('proxyless', False)

    tokens = load_tokens('input/token.txt')
    proxies = load_proxies('input/proxies.txt') if not proxyless else []
    statuses = load_statuses('input/statuses.txt')

    if not tokens or not statuses:
        NovaLogger.fail("Missing tokens or statuses!")
        return

    for idx, token in enumerate(tokens):
        proxy = proxies[idx % len(proxies)] if proxies and not proxyless else None
        threading.Thread(
            target=status_worker,
            args=(token, proxy, statuses, interval),
            daemon=True
        ).start()
        NovaLogger.event(f"Started account #{idx+1}")

    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        NovaLogger.note("Stopping all threads...")
    finally:
        NovaLogger.close()

if __name__ == '__main__':
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)
    main()
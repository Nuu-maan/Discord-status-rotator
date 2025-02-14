# Discord Status Rotator

A Python script to automatically rotate custom statuses on multiple Discord accounts.

![Banner](https://i.imgur.com/your-image.png) <!-- Replace with an actual image if needed -->

## Features
- Rotate custom statuses on multiple Discord accounts.
- Supports proxies for account security.
- Configurable update interval.
- Multi-threaded for concurrent status updates.
- Logs all events for debugging and monitoring.

## Requirements
- Python 3.7 or higher.
- Discord tokens for the accounts you want to use.
- (Optional) Proxies if you want to use them.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/discord-status-rotator.git
   cd discord-status-rotator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Setup input files:
   - Add your Discord tokens to `input/tokens.txt` (one token per line).
   - (Optional) Add proxies to `input/proxies.txt` (one proxy per line in the format `username:password@host:port`).
   - Add custom statuses to `input/statuses.txt` (one status per line).

4. Configure the script by editing `config.json`:
   ```json
   {
       "interval": 60,
       "proxyless": false
   }
   ```
   - `interval`: Time in seconds between status updates.
   - `proxyless`: Set to `true` if you don't want to use proxies.

## Usage
Run the script:
```bash
python main.py
```
- The script will display a banner and start rotating statuses for all tokens.
- Press `Ctrl+C` to stop the script.

## Logs
All logs are saved in `status_rotator.log`.

## Understanding the Code
### Key Functionalities
- **Imports**: Uses `requests`, `json`, `time`, `threading`, `colorama`, and a custom `NovaLogger` for structured logging.
- **Multi-threading**: Each token runs in its own thread for concurrent status updates.
- **Error Handling**: Logs failures and retries API requests when needed.
- **Graceful Shutdown**: Handles `Ctrl+C` to stop threads safely.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Disclaimer
This script is for educational purposes only. Use it responsibly and at your own risk. The developers are not responsible for any misuse or damage caused by this script.
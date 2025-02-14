# Discord Status Rotator

A Python script to automatically rotate custom statuses on multiple Discord accounts.

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
   git clone https://github.com/Nuu-maan/Discord-status-rotator.git
   cd discord-status-rotator
   ```

### Understanding the Code

The provided Python script is a **Discord Status Rotator**. It allows users to automatically rotate custom statuses on multiple Discord accounts. Here's a breakdown of its functionality:

1. **Imports**:
   - `requests`: For making HTTP requests to the Discord API.
   - `json`: For parsing the configuration file (`config.json`).
   - `time` and `threading`: For managing intervals and running tasks concurrently.
   - `NovaLogger`: A custom logging utility for logging events, errors, and successes.
   - `colorama`: For adding colored text to the console output.

2. **Banner**:
   - A visually appealing ASCII art banner is displayed when the script starts.

3. **Functions**:
   - `load_tokens`: Loads Discord tokens from a file (`input/token.txt`).
   - `load_proxies`: Loads proxies from a file (`input/proxies.txt`) if `proxyless` is disabled in the config.
   - `load_statuses`: Loads custom statuses from a file (`input/statuses.txt`).
   - `update_status`: Updates the custom status of a Discord account using the Discord API.
   - `status_worker`: Continuously rotates statuses for a given token at a specified interval.
   - `main`: The main function that initializes the script, loads configurations, and starts threads for each token.

4. **Configuration**:
   - The script reads a `config.json` file for settings like `interval` (time between status updates) and `proxyless` (whether to use proxies or not).

5. **Threading**:
   - Each Discord token runs in its own thread, allowing multiple accounts to update their statuses simultaneously.

6. **Error Handling**:
   - The script logs errors (e.g., failed API requests) and successes (e.g., updated statuses) using `NovaLogger`.

7. **Graceful Shutdown**:
   - The script can be stopped using `Ctrl+C`, and it will log the shutdown process.


## Logs
All logs are saved in `status_rotator.log`.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Disclaimer
This script is for educational purposes only. Use it responsibly and at your own risk. The developers are not responsible for any misuse or damage caused by this script.
```

---

### `requirements.txt`

```plaintext
requests>=2.26.0
colorama>=0.4.4
```

---

### `LICENSE`

This project is licensed under the MIT License. See LICENSE for details.


## Disclaimer
This script is for educational purposes only. Use it responsibly and at your own risk. The developers are not responsible for any misuse or damage caused by this script.


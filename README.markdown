# Keylogger Script README

## Overview
This Python script is a keylogger that captures keystrokes, logs them to a file, and periodically sends the log via email. It is designed to run on Windows systems and includes functionality to hide the console window and add itself to the startup folder for persistence.

**Note**: This script is provided for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Ensure you have explicit permission from the system owner before deploying this script.

## Features
- **Keystroke Logging**: Captures all keystrokes, including special keys, and logs them with timestamps to a file.
- **Email Reporting**: Sends the log file content to a specified email address at regular intervals (default: 15 minutes).
- **Stealth Mode**: Hides the console window on Windows systems to run discreetly.
- **Persistence**: Copies itself to the Windows startup folder to run on system boot.
- **Error Handling**: Silently handles errors to ensure continuous operation.

## Requirements
- **Python 3.x** installed on the system.
- Python libraries:
  - `pynput` (for capturing keystrokes)
  - `smtplib` (for sending emails)
  - `pywin32` (for hiding the console window on Windows)
- A Gmail account with an **App Password** for email functionality (due to Gmail's security settings).
- Windows operating system (for console hiding and startup folder functionality).

### Installation
1. Install required Python libraries:
   ```bash
   pip install pynput pywin32
   ```
2. Ensure you have a Gmail App Password:
   - Go to your Google Account settings.
   - Enable 2-Step Verification.
   - Generate an App Password for the script (see [Google Support](https://support.google.com/accounts/answer/185833) for details).

## Configuration
Edit the following variables in the script to customize its behavior:
- `email_address`: The Gmail address used to send logs (e.g., `parthk.cse21@sbjit.edu.in`).
- `email_password`: The Gmail App Password (not your regular Gmail password).
- `recipient`: The email address to receive logs (can be the same as `email_address`).
- `interval`: Time interval (in seconds) between email reports (default: `900` seconds or 15 minutes).
- `log_file`: Path to the log file (default: `C:\Users\<username>\AppData\Roaming\winlog.txt`).
- `startup_path`: Path to the startup folder for persistence (default: Windows startup folder).

## Usage
1. Save the script with a `.pyw` extension (e.g., `keylogger.pyw`) to run without a visible console window.
2. Configure the script with your email credentials and desired settings.
3. Run the script:
   ```bash
   python keylogger.pyw
   ```
4. The script will:
   - Log all keystrokes to the specified `log_file`.
   - Send the log file content via email every `interval` seconds.
   - Copy itself to the startup folder for persistence (runs on system boot).
   - Hide the console window (on Windows).

## File Structure
- **Log File**: Stored at `C:\Users\<username>\AppData\Roaming\winlog.txt` (configurable).
- **Startup File**: Copied to `C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\keylogger.pyw` (configurable).

## Notes
- **Security**: Ensure the Gmail App Password is kept secure and not hardcoded in production environments.
- **Permissions**: Running this script requires administrative privileges for copying to the startup folder.
- **Error Handling**: The script silently ignores errors (e.g., email sending failures or file copy issues) to maintain stealth.
- **Platform**: The console-hiding feature is Windows-specific. On other platforms, this feature is skipped.

## Disclaimer
This script is intended for educational and ethical purposes only, such as testing system security with explicit consent. Unauthorized use of keyloggers to monitor or collect data without permission is illegal and violates privacy laws. The author is not responsible for any misuse of this script.


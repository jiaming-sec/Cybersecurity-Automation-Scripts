import re
import os
import smtplib
import time
import logging
from email.mime.text import MIMEText
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Configure logging
logging.basicConfig(
    filename="log_monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define log file paths
LOG_FILE_PATH = "logs/system.log"
ALERT_LOG_PATH = "logs/alert_logs.log"

# Define regex patterns for suspicious events
FAILED_LOGIN_PATTERN = re.compile(r"Failed password for (?:invalid user )?(\w+) from (\d+\.\d+\.\d+\.\d+)")
SUDO_COMMAND_PATTERN = re.compile(r"sudo: (.*?) : command not allowed")

# Email settings for alerting
EMAIL_SENDER = "your_email@example.com"
EMAIL_RECEIVER = "security_team@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"
SMTP_PASSWORD = "your_email_password"

def send_alert_email(subject, message):
    """Send an email alert for suspicious log activity."""
    try:
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        logging.info("Alert email sent successfully.")
    except Exception as e:
        logging.error(f"Error sending email: {e}")

class LogFileHandler(FileSystemEventHandler):
    """Watch for changes in the log file and analyze new entries."""
    def on_modified(self, event):
        if event.src_path == LOG_FILE_PATH:
            analyze_logs()
def analyze_logs():
    """Analyze logs for suspicious activity."""
    if not os.path.exists(LOG_FILE_PATH):
        logging.warning("Log file not found!")
        return

    with open(LOG_FILE_PATH, 'r') as log_file:
        logs = log_file.readlines()

    alerts = []

    for line in logs[-10:]:  # Process only the last 10 lines to reduce redundant processing
        failed_login_match = FAILED_LOGIN_PATTERN.search(line)
        sudo_command_match = SUDO_COMMAND_PATTERN.search(line)

        if failed_login_match:
            user, ip = failed_login_match.groups()
            alert_msg = f"Suspicious failed login attempt by {user} from {ip}"
            alerts.append(alert_msg)

        if sudo_command_match:
            cmd = sudo_command_match.group(1)
            alert_msg = f"Unauthorized sudo command detected: {cmd}"
            alerts.append(alert_msg)

    if alerts:
        with open(ALERT_LOG_PATH, 'a') as alert_log:
            for alert in alerts:
                alert_log.write(alert + "\n")
        logging.info("Security events detected and logged.")
        send_alert_email("Security Alert - Suspicious Activity Detected", "\n".join(alerts))
    else:
        logging.info("No suspicious activity detected.")

def monitor_logs():
    """Monitor log file for real-time changes."""
    observer = Observer()
    event_handler = LogFileHandler()
    observer.schedule(event_handler, path=os.path.dirname(LOG_FILE_PATH) or '.', recursive=False)
    observer.start()
    logging.info("Starting real-time log monitoring...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    logging.info("Log monitoring stopped.")
    
if __name__ == "__main__":
    monitor_logs()

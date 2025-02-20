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

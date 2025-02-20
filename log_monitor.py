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

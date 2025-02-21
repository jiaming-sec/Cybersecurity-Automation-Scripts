import re
import os
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="log_parser.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define log file path
LOG_FILE_PATH = "logs/system.log"
PARSED_LOG_PATH = "logs/parsed_logs.json"

# Define regex patterns for log parsing
GENERAL_LOG_PATTERN = re.compile(r"(\w+ \d+ \d+:\d+:\d+) (\w+) (.*)")
FAILED_LOGIN_PATTERN = re.compile(r"Failed password for (?:invalid user )?(\w+) from (\d+\.\d+\.\d+\.\d+)")
ERROR_PATTERN = re.compile(r"error|failure|denied", re.IGNORECASE)

def parse_logs():
    """Parses logs and extracts key security events."""
    if not os.path.exists(LOG_FILE_PATH):
        logging.warning("Log file not found!")
        return
        
parsed_entries = []
    
    with open(LOG_FILE_PATH, 'r') as log_file:
        logs = log_file.readlines()
    
    for line in logs:
        general_match = GENERAL_LOG_PATTERN.search(line)
        failed_login_match = FAILED_LOGIN_PATTERN.search(line)
        error_match = ERROR_PATTERN.search(line)

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

        log_entry = {}
        
        if general_match:
            timestamp, source, message = general_match.groups()
            log_entry = {
                "timestamp": timestamp,
                "source": source,
                "message": message,
                "category": "General"
            }

        if failed_login_match:
            user, ip = failed_login_match.groups()
            log_entry["category"] = "Failed Login"
            log_entry["username"] = user
            log_entry["ip_address"] = ip
        
        if error_match:
            log_entry["category"] = "Error"
        
        if log_entry:
            parsed_entries.append(log_entry)
    
    with open(PARSED_LOG_PATH, 'w') as json_file:
        json.dump(parsed_entries, json_file, indent=4)
    
    logging.info(f"Parsed {len(parsed_entries)} log entries successfully.")
    print(f"Parsed logs saved to {PARSED_LOG_PATH}")

if __name__ == "__main__":
    parse_logs()

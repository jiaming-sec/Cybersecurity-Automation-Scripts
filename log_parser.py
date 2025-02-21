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



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


log_file = "server.log"
ip_addresses = extract_ips(log_file)
print("Extracted IPs:", ip_addresses)


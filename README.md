# Cybersecurity Automation Scripts

This repository contains a collection of Python scripts designed to automate various cybersecurity tasks, enhancing efficiency and accuracy in security operations.

## Features

- **Real-time Log Monitoring:** Automates monitoring and analysis of security logs to detect suspicious activities in real-time.
- **Threat Intelligence Integration:** Checks IP addresses against known blacklists to identify potential threats.
- **Malware Analysis:** Tools to assist in the automated analysis of potential malware files.
- **Windows Event Log Parsing:** Scripts to parse and analyze Windows Event Logs for security events.
- **Email and Slack Notifications:** Alerts security personnel via email or Slack when threats are detected.

## Scripts

1. **`log_monitor.py`** - Monitors specified log files in real-time and alerts on detecting predefined suspicious patterns.
2. **`log_parser.py`** - Parses generic log files to extract and report security-relevant information.
3. **`malware_analysis.py`** - Automates the analysis of files to identify potential malware characteristics.
4. **`parse_windows_logs.py`** - Parses Windows Event Logs to extract and analyze security events.
5. **`security_log_automation.py`** - Automates security log analysis, detects failed login attempts, unauthorized sudo commands, and integrates real-time monitoring.

## Getting Started

### Prerequisites

- Python 3.x installed.
- Required dependencies installed:
  ```bash
  pip install -r requirements.txt
  ```
### Clone the Repository
```bash
git clone https://github.com/jiaming-sec/Cybersecurity-Automation-Scripts.git
cd Cybersecurity-Automation-Scripts
```
### Configure and Run Scripts
- Each script may have configurable parameters (e.g., log file paths, email settings, webhook URLs).
- Open the script in a text editor to review and modify configurations as needed.
- Run the script:
  ```bash
  python script_name.py
  ```

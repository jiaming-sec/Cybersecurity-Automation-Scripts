import re

def monitor_logs(logfile, pattern):
    """
    Monitors a log file for occurrences of a specific pattern.

    Args:
        logfile (str): Path to the log file.
        pattern (str): Regex pattern to detect anomalies.
    """
    try:
        with open(logfile, "r") as file:
            logs = file.readlines()
            for line in logs:
                if re.search(pattern, line):
                    print(f"[ALERT] Suspicious activity detected: {line.strip()}")
    except FileNotFoundError:
        print("[ERROR] Log file not found!")

if __name__ == "__main__":
    monitor_logs("/var/log/syslog", r"(failed|error|unauthorized|denied)")


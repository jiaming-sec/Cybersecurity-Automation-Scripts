# Cybersecurity Automation Scripts

## 📌 Overview
This repository contains **Python automation scripts** designed to assist cybersecurity professionals in **threat detection, incident response, log analysis, and compliance monitoring**. These scripts help security teams automate repetitive tasks and enhance operational efficiency.

## 🚀 Features
- 🔍 **Threat Detection** - Automated log scanning, anomaly detection, and SIEM integrations.
- 🛡️ **Incident Response** - Scripts for malware analysis, sandboxing, and forensic automation.
- 📜 **Log Analysis** - Parsing logs from different sources such as Windows Event Logs, Syslogs, and Firewall logs.
- 🔑 **Access Control & IAM Auditing** - Detecting privilege escalations and misconfigurations.
- 📊 **Compliance & Security Checks** - Automate security baseline checks against NIST, CIS, and ISO 27001.

---

## 📂 Directory Structure
```
Cybersecurity-Automation-Scripts/
│── threat_detection/
│   ├── log_monitor.py      # Monitors logs for anomalies
│   ├── firewall_monitor.py # Detects suspicious firewall activity
│── incident_response/
│   ├── malware_analysis.py # Automates VirusTotal scans
│   ├── sandbox_analysis.py # Runs malware in a sandboxed environment
│── log_analysis/
│   ├── parse_windows_logs.py # Extracts critical events from Windows Event Logs
│   ├── siem_log_parser.py    # Parses SIEM logs for security events
│── access_control/
│   ├── iam_audit.py         # Detects privilege escalation attempts
│── compliance/
│   ├── nist_checker.py      # Checks system configurations against NIST guidelines
│── requirements.txt         # Python dependencies
│── README.md                # Documentation
```
---

## ⚙️ Installation
### Prerequisites
- Python 3.8+
- Required dependencies (install via `pip`):
  ```sh
  pip install -r requirements.txt
  ```

---

## 📖 Usage
Each script is standalone and can be executed individually. Below are some examples:

### 🔍 Log Monitoring
```sh
python threat_detection/log_monitor.py --logfile /var/log/syslog
```

### 🛡️ Malware Analysis (Using VirusTotal API)
```sh
python incident_response/malware_analysis.py --file sample.exe --api-key YOUR_VIRUSTOTAL_API_KEY
```

### 📜 Windows Event Log Analysis
```sh
python log_analysis/parse_windows_logs.py --event-id 4625

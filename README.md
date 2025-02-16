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
# 🛠 Cybersecurity Automation Scripts  

🚀 **A collection of Python & PowerShell scripts for security operations.**  
Automate log analysis, threat intelligence lookups, and forensic investigations.  

---

## 🔍 Featured Scripts:
✅ **Log Parsing & IOC Extraction**  
- Extract malicious indicators from logs (IP, hashes, domains).  
- Automate threat detection using **Sigma rules & YARA**.

✅ **Threat Intelligence Automation**  
- Integrate with **VirusTotal, Shodan, and AbuseIPDB**.  
- Lookup IOCs from SIEM alerts automatically.

✅ **SIEM & Firewall Automation**  
- Query **Splunk logs** with API calls.  
- Automate **Palo Alto firewall rule verification**.
  
---

## 🛠 Technologies Used:
- **Languages:** Python, PowerShell, Bash  
- **SIEM:** Splunk, ElasticSearch, Graylog  
- **Threat Intel APIs:** VirusTotal, Shodan, AbuseIPDB  
- **EDR/XDR:** CrowdStrike, Carbon Black  

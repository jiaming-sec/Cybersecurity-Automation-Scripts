# Cybersecurity Automation Scripts

![GitHub stars](https://img.shields.io/github/stars/jiaming-sec/Cybersecurity-Automation-Scripts?style=social)
![GitHub forks](https://img.shields.io/github/forks/jiaming-sec/Cybersecurity-Automation-Scripts?style=social)
![GitHub issues](https://img.shields.io/github/issues/jiaming-sec/Cybersecurity-Automation-Scripts)
![GitHub license](https://img.shields.io/github/license/jiaming-sec/Cybersecurity-Automation-Scripts)

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
```

---

## 🛠 Contributing
We welcome contributions! If you’d like to enhance existing scripts or add new cybersecurity automation tools:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-new-script`)
3. Commit your changes (`git commit -m "Added new automation script"`)
4. Push to your branch (`git push origin feature-new-script`)
5. Open a Pull Request

---

## 📜 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 📝 TODOs
- [ ] Implement Splunk API log ingestion
- [ ] Develop an automated security baseline scanner for cloud environments
- [ ] Add more unit tests for critical scripts

---

## 🤝 Connect
👩‍💻 **Jiaming Qu**  
🔗 [GitHub](https://github.com/jiaming-sec) | [LinkedIn](https://www.linkedin.com/in/jiaming-qu/)

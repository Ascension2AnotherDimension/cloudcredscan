# cloudcredscan
CloudCredScan is a Python tool that scans AWS cloud resources and code repos for exposed credentials like API keys, AWS secrets, and tokens. It detects misconfigurations using regex and generates easy-to-read reports to help prevent cloud security breaches.

# 🔐 CloudCredScan

**CloudCredScan** is a lightweight Python tool that scans your AWS cloud resources and local code repositories for exposed credentials, secrets, and tokens. It's built for security engineers, cloud practitioners, and DevOps teams who want to catch misconfigurations before attackers do.

---

## 🚀 Features

- ✅ Scan AWS S3 buckets and EC2 user data for exposed secrets
- ✅ Detect AWS keys, database credentials, Slack tokens, and more using custom regex
- ✅ Generate clean CLI and HTML reports
- ✅ Optional test mode with dummy data
- ✅ Auto-remediation option (delete or quarantine flagged objects)

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **boto3** (AWS SDK for Python)
- **re** (for pattern matching)
- **argparse** (CLI)
- Optional: **Jinja2**, **BeautifulSoup** for HTML reports

---

## 📦 Installation

```bash
git clone https://github.com/ascension2anotherdimension/cloudcredscan.git
cd cloudcredscan
pip install -r requirements.txt

☁️ AWS Permissions

Make sure your AWS credentials are configured and have appropriate read permissions for:
	•	s3:ListBucket, s3:GetObject
	•	ec2:DescribeInstances, ec2:GetUserData

🧪 Usage
python scan.py --mode s3 --bucket your-bucket-name
python scan.py --mode ec2
python scan.py --mode local --path ./your/codebase
You can also customize patterns in regex_patterns.py to tailor your scans.

📊 Output
	•	Command-line alerts (highlighted by severity)
	•	Optional: /reports/scan_report.html with detailed summary

⸻

🧠 Why CloudCredScan?

Credential leaks are one of the top causes of cloud security incidents. This tool helps you identify risks early, with flexible scanning logic and real cloud integration.

⸻

📄 License

MIT License — feel free to use and improve.

⸻

✍️ Author

Built by @ascension2anotherdimension

---

Let me know when you want help building the actual scripts (`scan.py`, `aws_scanner.py`, etc.). I can get you started with a working AWS S3 scanner this week.


🛡️ Website Vulnerability Scanner

📌 Overview

This Python script scans a website for potential security vulnerabilities. It checks for missing security headers, outdated software versions, and insecure form implementations. Additionally, it crawls the website recursively to find more vulnerabilities.

🚀 Features

🔍 Security Header Check: Identifies missing HTTP security headers.

📌 Outdated Software Detection: Detects old and potentially vulnerable server-side software.

⚠️ Insecure Forms Analysis: Finds forms with missing action attributes or using insecure GET methods.

🌐 Website Crawling: Recursively scans web pages within the same domain for security risks.

📊 Detailed Report: Provides a summary of detected vulnerabilities.

🛠️ Prerequisites

Python 3.x

Required Python Libraries:

pip install requests beautifulsoup4

📥 Installation

Clone this repository or copy the script to your local machine:

git clone https://github.com/your-repo/vulnerability-scanner.git
cd vulnerability-scanner

Install dependencies:

pip install -r requirements.txt

🏗️ Usage

Run the script:

python vulnerability_scanner.py

Enter the target URL when prompted:

Please enter the target URL: https://example.com

Review the generated security report:

VULNERABILITY SCAN REPORT FOR https://example.com:
- Missing HTTP Security Headers: Strict-Transport-Security, X-Content-Type-Options
- Outdated Software Detected: Apache 2.4.6, PHP 5.6
- Form using GET instead of POST

If you wish to scan another website, type yes when prompted.

🔄 Example Output

VULNERABILITY SCAN REPORT FOR https://example.com:
- Missing HTTP Security Headers: Strict-Transport-Security, X-Content-Type-Options
- Outdated Software Detected: Apache 2.4.6, PHP 5.6
- Form using GET instead of POST

🛑 Error Handling

If the target website is unreachable, an error message is displayed:

Failed to access https://example.com: Connection timeout

📜 License

This script is provided under the MIT License.

👨‍💻 Author

Bibek Dhimal


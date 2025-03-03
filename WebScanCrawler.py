import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def check_security_headers(headers):
    """Check for missing security headers."""
    required_headers = ["Strict-Transport-Security", "X-Content-Type-Options"]
    missing_headers = [h for h in required_headers if h not in headers]
    return missing_headers

def check_outdated_software(headers):
    """Detect outdated software versions from headers."""
    outdated_versions = []
    server_header = headers.get("Server", "")
    powered_by = headers.get("X-Powered-By", "")
    
    if "Apache/2.4.6" in server_header:
        outdated_versions.append("Apache 2.4.6")
    if "PHP/5.6" in powered_by:
        outdated_versions.append("PHP 5.6")
    
    return outdated_versions

def check_insecure_forms(soup):
    """Identify forms with missing action attributes or insecure GET methods."""
    issues = []
    for form in soup.find_all("form"):
        action = form.get("action")
        method = form.get("method", "GET").upper()
        
        if not action:
            issues.append("Form with missing action attribute")
        if method == "GET":
            issues.append("Form using GET instead of POST")
    return issues

def crawl_website(url, visited=set(), max_depth=2, depth=0):
    """Recursively crawl a website and scan for vulnerabilities."""
    if depth > max_depth or url in visited:
        return []
    
    visited.add(url)
    report = []
    
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Check security headers
        missing_headers = check_security_headers(response.headers)
        if missing_headers:
            report.append(f"Missing HTTP Security Headers: {', '.join(missing_headers)}")
        
        # Check outdated software
        outdated_versions = check_outdated_software(response.headers)
        if outdated_versions:
            report.append(f"Outdated Software Detected: {', '.join(outdated_versions)}")
        
        # Check insecure forms
        form_issues = check_insecure_forms(soup)
        if form_issues:
            report.extend(form_issues)
        
        # Find and crawl links
        for link in soup.find_all("a", href=True):
            next_url = urljoin(url, link["href"])
            if next_url.startswith(url):  # Ensure it's within the same domain
                report.extend(crawl_website(next_url, visited, max_depth, depth + 1))
                
    except requests.RequestException as e:
        report.append(f"Failed to access {url}: {e}")
    
    return report

def generate_report(url):
    """Run the crawler and generate a vulnerability scan report."""
    print(f"VULNERABILITY SCAN REPORT FOR {url}:")
    report = crawl_website(url)
    if report:
        for issue in report:
            print(f"- {issue}")
    else:
        print("No vulnerabilities found.")

# Example usage
if __name__ == "__main__":
    while True:
        target_url = input("Please enter the target URL: ")
        generate_report(target_url)

        # Ask if the user wants to scan more websites
        scan_more = input("Do you want to scan another website? (yes/no): ").strip().lower()
        if scan_more != "yes":
            print("Exiting the scan process.")
            break
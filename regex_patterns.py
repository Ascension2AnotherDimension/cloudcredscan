# regex_patterns.py

credential_patterns = {
    # AWS Access Key ID
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    
    # AWS Secret Access Key (base64-like 40 chars)
    "AWS Secret Key": r"(?<![A-Z0-9])[A-Za-z0-9/+=]{40}(?![A-Z0-9])",
    
    # Slack Token (starts with xoxb- or xoxp- followed by digits and letters)
    "Slack Token": r"xox[baprs]-[0-9a-zA-Z]{10,48}",
    
    # Generic API Key (alphanumeric strings 32-45 chars)
    "API Key": r"(?i)(api[_-]?key|secret)[\"']?\s*[:=]\s*[\"']?[A-Za-z0-9_\-]{32,45}[\"']?",
    
    # Basic Database Password Pattern (looks for 'password' in code)
    "Database Password": r"(?i)password\s*[:=]\s*[\"'].*?[\"']",
    
    # JWT Token (3 parts separated by dots, base64url)
    "JWT Token": r"eyJ[A-Za-z0-9_-]+?\.[A-Za-z0-9._-]+?\.[A-Za-z0-9._-]+",
}

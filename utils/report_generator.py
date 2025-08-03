import os
from datetime import datetime

REPORTS_DIR = "reports"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>CloudCredScan Report - {bucket}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #2c3e50; }}
        table {{ width: 100%; border-collapse: collapse; }}
        th, td {{ padding: 8px 12px; border: 1px solid #ddd; }}
        th {{ background-color: #3498db; color: white; }}
        tr:nth-child(even) {{ background-color: #f2f2f2; }}
        .snippet {{ font-family: monospace; background: #eee; padding: 5px; }}
    </style>
</head>
<body>
    <h1>CloudCredScan Report - {bucket}</h1>
    <p>Scan Date: {date}</p>
    <table>
        <tr>
            <th>File</th>
            <th>Credential Type</th>
            <th>Snippet</th>
        </tr>
        {rows}
    </table>
</body>
</html>
"""

def generate_report(findings, bucket_name):
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)
    rows_html = ""
    for f in findings:
        rows_html += f"""
        <tr>
            <td>{f['key']}</td>
            <td>{f['match']}</td>
            <td class="snippet">{f['snippet']}</td>
        </tr>
        """
    report_html = HTML_TEMPLATE.format(
        bucket=bucket_name,
        date=datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        rows=rows_html
    )
    filename = os.path.join(REPORTS_DIR, f"scan_report_{bucket_name}_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.html")
    with open(filename, "w") as f:
        f.write(report_html)
    print(f"Report saved to {filename}")

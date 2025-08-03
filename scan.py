import argparse
from aws_scanner import scan_s3_bucket
from utils.report_generator import generate_report

def main():
    parser = argparse.ArgumentParser(description="CloudCredScan - Scan AWS S3 buckets for exposed credentials.")
    parser.add_argument("--mode", choices=["s3"], required=True, help="Scan mode: 's3' for AWS S3 buckets.")
    parser.add_argument("--bucket", type=str, help="S3 bucket name to scan.")
    parser.add_argument("--report", action="store_true", help="Generate HTML report.")
    parser.add_argument("--delete", action="store_true", help="Delete flagged objects (use with caution).")
    
    args = parser.parse_args()

    if args.mode == "s3":
        if not args.bucket:
            print("Error: Please provide a bucket name with --bucket")
            return
        
        print(f"🔍 Scanning S3 bucket: {args.bucket}")
        findings = scan_s3_bucket(args.bucket, delete_flag=args.delete)

        if not findings:
            print("✅ No exposed credentials found.")
        else:
            print(f"⚠️ {len(findings)} potentially exposed secrets found.")
            for item in findings:
                print(f" - {item['key']} | Match: {item['match']}")

            if args.report:
                generate_report(findings, args.bucket)
                print("📊 HTML report generated in /reports")

if __name__ == "__main__":
    main()

import requests
import csv
from datetime import datetime

def check_api(url, output_file):
    try:
        response = requests.get(url, timeout=5)
        status = response.status_code

    except requests.exceptions.RequestException:
        status = "FAILED"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write to CSV log
    with open(output_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, url, status])

    # 🚨 Alert logic
    if status != 200:
        print(f"ALERT: API issue detected at {timestamp} (status: {status})")
    else:
        print(f"API OK: {status}")
# log_analyzer.py

from collections import Counter

def analyze_logs(input_file, output_file):
    log_types = []

    try:
        with open(input_file, "r") as file:
            for line in file:
                if "ERROR" in line:
                    log_types.append("ERROR")
                elif "WARNING" in line:
                    log_types.append("WARNING")
                elif "INFO" in line:
                    log_types.append("INFO")

        results = Counter(log_types)

        with open(output_file, "w") as file:
            file.write("Log Analysis Report\n")
            file.write("-------------------\n")

            for log_type, count in results.items():
                file.write(f"{log_type}: {count}\n")

        print("Log analysis completed.")

    except FileNotFoundError:
        print("Log file not found.")
import time
from log_analyzer import analyze_logs
from api_monitor import check_api
from onboarding import onboard_users

def main():
    print("IT Automation Toolkit Running...\n")

    while True:
        print("Running automation cycle...\n")

        analyze_logs("data/system.log", "output/log_report.txt")
        check_api("https://jsonplaceholder.typicode.com/posts", "output/api_status.csv")
        onboard_users("data/users.csv", "output/onboarding_report.txt")

        print("Summary:")
        print("- Logs analyzed")
        print("- API checked")
        print("- Users onboarded")

        print("\nCycle completed. Waiting 60 seconds...\n")

        time.sleep(60)  # runs every 60 seconds

if __name__ == "__main__":
    main()

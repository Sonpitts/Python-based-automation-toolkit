# onboarding.py

import csv
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def onboard_users(input_file, output_file):
    try:
        with open(input_file, "r") as file:
            reader = csv.DictReader(file)

            with open(output_file, "w") as out:
                out.write("User Onboarding Report\n")
                out.write("----------------------\n")

                for row in reader:
                    name = row["name"]
                    department = row["department"]

                    username = name.lower().replace(" ", ".")
                    password = generate_password()

                    out.write(f"Name: {name}\n")
                    out.write(f"Username: {username}\n")
                    out.write(f"Department: {department}\n")
                    out.write(f"Temporary Password: {password}\n\n")

        print("Onboarding completed.")

    except FileNotFoundError:
        print("User file not found.")
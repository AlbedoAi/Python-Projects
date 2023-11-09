#!/usr/bin/env python3

# Author: Shubham Raturi
# Details: This program goes thru a folder to find all files then filter them based on the date provided by the user.
# Resources: https://www.cs.siue.edu/programming-style-guide

import os
from datetime import datetime

#Main function runs on start to call all the other functions
def main():
    folder_to_analyze = input("Enter the folder path to analyze: ") #input of the folder

    if not os.path.exists(folder_to_analyze): #error handling
        print("Folder does not exist.")
    else:
        print("Folder structure:") #prints the files in the folder
        print_folder_structure(folder_to_analyze)

        date_range = input("Enter the date range (YYYY/MM/DD - YYYY/MM/DD): ").split(" - ") #asks for the date to search the folder with
        start_date, end_date = date_range #stores them

        met_files, did_not_meet_files = filter_files_by_date_range(folder_to_analyze, start_date, end_date) #passes the information to the other function

        print("\nFiles that meet the date criteria:") #prints the ones that met the criteria
        for file_path, modified_date in met_files:
            print(f"File: {file_path}\nModified Date: {modified_date}")

        print("\nFiles that don't meet the date criteria:") #prints the ones that did not meet the criteria
        for file_path, modified_date in did_not_meet_files:
            if isinstance(modified_date, datetime):
                print(f"File: {file_path}\nModified Date: {modified_date} (Doesn't meet criteria)")
            else:
                print(f"File: {file_path}\nError: {modified_date} (Doesn't meet criteria)")

# Function to print folder structure
def print_folder_structure(folder_path, indent=""):
    for item in os.listdir(folder_path): #uses the os library to interact with the system and get its details loops until it runs out of the items
        item_path = os.path.join(folder_path, item) #gets the path of the item
        if os.path.isdir(item_path): #prints them based on if they are a file or a dir
            print(indent + f"Folder: {item}")
            print_folder_structure(item_path, indent + "  ")
        else:
            print(indent + f"File: {item}")

# Function to filter and print files within a date range
def filter_files_by_date_range(folder_path, start_date, end_date):
    met_criteria = [] # array to seprate the met and not met files to print later
    did_not_meet_criteria = []

	#sets the date for searching
    start_date = datetime.strptime(start_date, "%Y/%m/%d")
    end_date = datetime.strptime(end_date, "%Y/%m/%d")

	#Uses the path given to loop over the folders and seprate them based on their modified date
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try: #sorts them in the different array of met and non met
                modified_date = datetime.fromtimestamp(os.path.getmtime(file_path))
                if start_date <= modified_date <= end_date:
                    met_criteria.append((file_path, modified_date))
                else:
                    did_not_meet_criteria.append((file_path, modified_date))
            except Exception as e:
                did_not_meet_criteria.append((file_path, str(e)))

	#returns the list to be printed
    return met_criteria, did_not_meet_criteria

main()

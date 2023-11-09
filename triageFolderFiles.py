# Details: This script allows you to triage a certain suspicous folder while analyzing its hash and copying its content to organize them by the same filetype in a different directory.

#!/usr/bin/env python3
import os
import hashlib
import shutil
from prettytable import PrettyTable

# Folders to explore and to export to
source_folder = "/home/albedo/Desktop/lab4/folder0a6"
destination_folder = "/home/albedo/Desktop/lab4/Lab4_FileExt"

# Creates the Lab4_FileExt directory if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Calculates the hash of the files found
def calculate_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, "rb") as file:
        while True:
            data = file.read(65536)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()

# Function to explore the folder and copy similar files to a different folder with respective subfolders
def explore_folder(source, destination):

    # Create a PrettyTable for displaying file details
    table = PrettyTable(["Directory", "Filename", "Hash", "Files with Same Extension"])

    extension_counts = {}  # Track file extension counts for each subfolder
    current_directory = ""  # Track the current directory being processed

    for root, dirs, files in os.walk(source):
        for index, filename in enumerate(files):
            file_path = os.path.join(root, filename)
            file_extension = os.path.splitext(filename)[1][1:]
            file_hash = calculate_hash(file_path)

            # Create a subdirectory for the file extension if it doesn't exist
            extension_folder = os.path.join(destination, file_extension)
            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)

            # Copy the file to the destination folder and rename with its hash
            new_file_path = os.path.join(extension_folder, file_hash)
            shutil.copy(file_path, new_file_path)

            # Determine the relative subfolder
            subfolder = os.path.relpath(root, source)

            if subfolder != current_directory:
                current_directory = subfolder
                # Print the full directory path
                table.add_row([root, "", "", ""])
                last_file_extension = ""

            if index == len(files) - 1 or file_extension != last_file_extension:
                # Add file details to the PrettyTable
                if subfolder not in extension_counts:
                    extension_counts[subfolder] = {}

                if file_extension not in extension_counts[subfolder]:
                    extension_counts[subfolder][file_extension] = 1
                else:
                    extension_counts[subfolder][file_extension] += 1

                extension_info = ", ".join([f"{count} {ext} files" for ext, count in extension_counts[subfolder].items()])
                table.add_row(["", filename, file_hash, extension_info])

            last_file_extension = file_extension

    # Print file details and file counts by extension
    print(table)

# Call the function
explore_folder(source_folder, destination_folder)


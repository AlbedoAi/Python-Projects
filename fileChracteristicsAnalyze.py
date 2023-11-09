#!/usr/bin/env python3

# Author: Shubham Raturi
# Details: This program goes thru a folder to find all files then prints the file in a table with their detailed information.
# Resources: https://www.cs.siue.edu/programming-style-guide

import os
import struct
from pefile import PE
from datetime import datetime
from prettytable import PrettyTable

# creates a table to store the results
table = PrettyTable()
table.field_names = ["File Name", "PEHdrOFF", "PESig", "Machine", "Timestamp", "Characteristics", "OptMagic",
                     "ImageBase", "Entry Point", "Subsystem", "DLL/EXE"]

# functions to convert Machine Type values to the appropriate strings
def get_machine_type(machine):
    machine_dict = {
        0x14C: "IMAGE_FILE_MACHINE_I386",
        0x8664: "IMAGE_FILE_MACHINE_AMD64",
    }
    return machine_dict.get(machine, "Unknown")

def get_subsystem(subsystem):
    subsystem_dict = {
        1: "Native",
        2: "IMAGE_SUBSYSTEM_WINDOWS_GUI",
        3: "IMAGE_SUBSYSTEM_WINDOWS_CUI",
    }
    return subsystem_dict.get(subsystem, "Unknown")

# function to extract specific characteristics from the characteristics field
def extract_characteristics(characteristics):
    characteristic_flags = {
        "IMAGE_FILE_RELOCS_STRIPPED": 0x0001,
        "IMAGE_FILE_EXECUTABLE_IMAGE": 0x0002,
        "IMAGE_FILE_LINE_NUMS_STRIPPED": 0x0004,
        "IMAGE_FILE_LOCAL_SYMS_STRIPPED": 0x0008,
        "IMAGE_FILE_AGGRESSIVE_WS_TRIM": 0x0010,
        "IMAGE_FILE_LARGE_ADDRESS_AWARE": 0x0020,
        "IMAGE_FILE_BYTES_REVERSED_LO": 0x0080,
        "IMAGE_FILE_32BIT_MACHINE": 0x0100,
        "IMAGE_FILE_DEBUG_STRIPPED": 0x0200,
        "IMAGE_FILE_REMOVABLE_RUN_FROM_SWAP": 0x0400,
        "IMAGE_FILE_NET_RUN_FROM_SWAP": 0x0800,
        "IMAGE_FILE_SYSTEM": 0x1000,
        "IMAGE_FILE_DLL": 0x2000,
        "IMAGE_FILE_UP_SYSTEM_ONLY": 0x4000,
        "IMAGE_FILE_BYTES_REVERSED_HI": 0x8000,
    }
    extracted = [flag for flag, value in characteristic_flags.items() if characteristics & value]
    return "\n".join(extracted)

# path containging the files
directory_path = "/home/albedo/Desktop/itsc203/lab3b/expandPE2"

# the extensions for the files
pe_file_extensions = [".exe", ".dll"]

# iterate through files in the directory
for file_name in os.listdir(directory_path):
    if file_name.endswith(tuple(pe_file_extensions)):
        file_path = os.path.join(directory_path, file_name)
        try:
            # create a PE object for the file
            mype = PE(file_path)

            # extract relevant information from the PE file
            dosMagic = hex(mype.DOS_HEADER.e_magic)
            pehdrOffset = mype.DOS_HEADER.e_lfanew

            pesig = "PE"
            machine = get_machine_type(mype.FILE_HEADER.Machine)
            timestamp = datetime.utcfromtimestamp(mype.FILE_HEADER.TimeDateStamp).strftime("%Y-%m-%d %H:%M:%S")
            characteristics = extract_characteristics(mype.FILE_HEADER.Characteristics)
            optMagic = "PE32" if mype.OPTIONAL_HEADER.Magic == 0x10B else "PE32+" if mype.OPTIONAL_HEADER.Magic == 0x20B else "ROM Image"
            addrEntryPt = hex(mype.OPTIONAL_HEADER.AddressOfEntryPoint)
            addrCodebase = hex(mype.OPTIONAL_HEADER.BaseOfCode)
            addrImagebase = hex(mype.OPTIONAL_HEADER.ImageBase)
            subsys = get_subsystem(mype.OPTIONAL_HEADER.Subsystem)

            # determine if it's a DLL or EXE
            dll_or_exe = "DLL" if file_name.endswith(".dll") else "EXE"

            # add information to the table
            table.add_row([file_name, pehdrOffset, pesig, machine, timestamp, characteristics, optMagic,
                           addrImagebase, addrEntryPt, subsys, dll_or_exe])
        except Exception as e:
            print("File unable to be analyzed")
# print the table
print(table)


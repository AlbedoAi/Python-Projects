#If on linux use "#!/usr/bin/python3"

# Author: Shubham Raturi
# Details: To use a dictionary and its values to be inserted into another table via a module and sort the data with its section.
# Resources: https://www.cs.siue.edu/programming-style-guide

from prettytable import PrettyTable

#dictionary with the data
computer_DataDict = {
  "Comp477": ["Gigabyte", 9133.27, "70561924KIQqzw", "68.192.163.42/255.255.240.0"],
  "Comp678": ["Asus", 7264.42, "56024371IQCewb", "198.78.85.109/255.255.248.0"],
  "Comp894": ["Acer", 4564.22, "41928367UHPkxu", "192.167.55.136/255.255.240.0"],
  "Comp592": ["Dell", 9378.82, "20451398MFWusg", "192.167.86.14/255.255.255.128"],
  "Comp397": ["Acer", 8115.08, "74189306HKLvwu", "176.33.145.182/255.255.248.0"],
  "Comp697": ["Asus", 8941.52, "17892534DZOlru", "10.0.252.127/255.255.192.0"],
  "Comp966": ["Dell", 9539.92, "46193287TYIurw", "10.0.222.132/255.255.252.0"],
  "Comp964": ["Dell", 4274.43, "04237918UTSdkj", "200.3.34.67/255.255.192.0"],
  "Comp634": ["Google", 5182.86, "95430287FCQfbk", "68.192.177.108/255.255.192.0"],
  "Comp565": ["Toshiba", 1904.33, "57018243JPYtpu", "192.167.63.98/255.255.240.0"],
  "Comp906": ["Dell", 5228.37, "96134827IHGibu", "176.33.20.163/255.255.192.0"],
  "Comp481": ["Asus", 7790.58, "05793218BRZjgl", "198.78.237.73/255.255.248.0"],
  "Comp370": ["Dell", 9251.70, "89531276LIMqby", "68.192.129.199/255.255.192.0"],
  "Comp703": ["Toshiba", 7520.04, "53179426FUXqjz", "200.3.191.102/255.255.192.0"],
  "Comp493": ["Google", 4621.55, "06514398WINzou", "198.78.59.119/255.255.240.0"]
}
#table made via prettytable with the coloumns
computer_data = PrettyTable(["Computer Name", "Manufacturer", "Asset Tag", "IP Address", "IP Subnet", "Price"])

#This function does the calculation to find the subnet address from the ip address and its mask.
def subnetCalculation(subnet, ip):

    #splits in its octets
    octet_info = subnet.split(".")

    #splits in its octets
    ip_parts = ip.split(".")

    for x in range(len(octet_info)):
        #checking to see wether the octet is 255 in case to modify or not
        if octet_info[x] != '255':
            # does and operation to find the subnet address
            a = bin(int(ip_parts[x]) & int(octet_info[x]))

            #turns it into an address
            ip_parts[x] = str(int(a, 2))
    return('.'.join(ip_parts))

#Iterates over the dictionary for each key and its items
for comp_Name, info in computer_DataDict.items():
    #Sets the variable to their equivalent in the database
    manufacturer = info[0]
    price = info[1]
    asset_tag = info[2]
    ip_Subnet = info[3]

    #splits the ip and the subnets
    ip_info = ip_Subnet.split("/")
    ip_address = ip_info[0]
    subnet_mask = ip_info[1]
    subnet_address = subnetCalculation(subnet_mask, ip_address)

    #adds the data to the rows in the table to be printed out
    computer_data.add_row([comp_Name, manufacturer, asset_tag, ip_address, subnet_address, price])
print(computer_data)

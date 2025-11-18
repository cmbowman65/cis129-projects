"""
CIS188, Lab 11 - Email and IP Address Ping

This program takes a provided CSV file, ip.csv, with a list of IP addresses, reads 
the file, pings each IP address and sends an email to my Pima CC email address 
containing the ping information for each ip address.

Author:  Cliff Bowman

Date:  25 Apr 2025

"""
from ping3 import ping
from pathlib import Path
import ezgmail, csv

# Initialize 
ezgmail.init()
current_dir = Path.cwd()
ip_file = (current_dir / 'ip.csv')

# context manager to open, read and close ip.csv
with open(ip_file, 'r', newline='') as input_file:
    csv_reader = csv.reader(input_file)
    
    next(csv_reader) # skip over header
    
    message_body = "Ping data:\n" # start body of the email message

    # iterate through ip.csv, ping the ip addresses, add output to message body
    for row in csv_reader:
        ip = row[0]
        ping_data = ping(ip)
        if ping_data != None:
            message_body += f"ip: {ip} - time = {ping_data} seconds\n"
        else:
            message_body += f"ip: {ip} - Request timed out\n"

# Send email with the ip addresses and ping data
ezgmail.send('cmbowman@mail.pima.edu', 'Lab 11 Ping Data', message_body)

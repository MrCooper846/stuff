# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 13:46:58 2023

@author: monke
"""

import re
import csv

def extract_emails(text):
    # Use a regular expression to find all names and emails in the text
    pattern = r'([\w\s.,]+)\s*<([\w\.-]+@[\w\.-]+)>'
    matches = re.findall(pattern, text)

    # Write the names and emails to a CSV file
    with open('emails.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Email']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for match in matches:
            writer.writerow({'Name': match[0], 'Email': match[1]})

text = "insert names + emails here"
extract_emails(text)

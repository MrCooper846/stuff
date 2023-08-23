import csv
import re

def extract_universities(text):
    universities = text.strip().split("\n\n")
    return universities

def extract_info(text):
    university = re.search("(.*?)\n", text).group(1)
    match = re.search("T: (.*?)\n", text)
    if match:
        phone_number = match.group(1)
    else:
        phone_number = None
    name = re.search("C: (.*?)\n", text).group(1)
    job_title = None
    email = re.search("E: (.*?)\n", text).group(1)
    return [university, phone_number, name, job_title, email]

def write_to_csv(data):
    with open("universities.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)

universities_text = """Insert list of Uni contacts here"""

universities_list = extract_universities(universities_text)

for university in universities_list:
    write_to_csv(extract_info(university))

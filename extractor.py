import re
import csv

# Read the text file
with open('input_file.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Find all instances of a series of numbers that start with "0.0."
matches = re.findall(r'0\.0\.\d+', text)

# Write the matches to a .csv file
with open('output_file.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Numbers'])
    for match in matches:
        writer.writerow([match])

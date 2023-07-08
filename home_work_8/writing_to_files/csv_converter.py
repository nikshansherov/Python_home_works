"""
The module takes a list of dictionaries and writes it to a csv file
"""

import csv


def create_csv(data, file):
    with open(file, 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()

        for row in data:
            writer.writerow(row)
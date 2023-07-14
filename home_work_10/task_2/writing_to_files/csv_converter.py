"""
The module takes a list of dictionaries and writes it to a csv file
"""

import csv


class CvsConverter:
    def __init__(self, data, file):
        self.data = data
        self.file = file

    def create_csv(data, file):
        with open(file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()

            for row in data:
                writer.writerow(row)

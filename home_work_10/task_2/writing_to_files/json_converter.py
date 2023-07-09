"""
The module accepts a list of dictionaries and writes a json file
"""

import json


class JsonConverter:
    def __init__(self, data, file):
        self.data = data
        self.file = file

    def create_json(data, file):
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

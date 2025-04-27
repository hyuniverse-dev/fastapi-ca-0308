# utils/json_helper.py

import json


class JsonHelper:
    def __init__(self, json_file: str):
        self.json_file = json_file

    def read_json(self):
        try:
            with open(self.json_file, "r", encoding='utf-8') as file:
                read = file.read()
                data = json.loads(read)
                return data
        except FileNotFoundError:
            data = list()
            return data

    def save_json(self, data: list):
        try:
            with open(self.json_file, "w", encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
                return True
        except Exception as e:
            print(e)
            return False

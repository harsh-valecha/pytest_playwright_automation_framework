import csv
import json


class DataUtils:

    @staticmethod
    def read_csv(file_path):
        data = []
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            # Skip the header if necessary
            next(csvreader)
            for row in csvreader:
                data.append(row)
        return data

    @staticmethod
    def read_json(file_path):
        with open(file_path, 'r') as jsonfile:
            data = json.load(jsonfile)
        return data

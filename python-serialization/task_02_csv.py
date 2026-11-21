#!/usr/bin/env python3
import csv
import json

"""Function that converts a csv file to json"""


def convert_csv_to_json(csv_filename):
    """Tries the conversion, returns true if successful."""
    try:
        with open(csv_filename, "r", newline="", encoding="utf-8") as csv_file:
            data = list(csv.DictReader(csv_file))

        with open("data.json", "w") as json_file:
            json.dump(data, json_file)
            return True

    except FileNotFoundError:
        return False

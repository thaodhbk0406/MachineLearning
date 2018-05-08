import json
import csv

with open("train.json") as file:
    data = json.load(file)

with open("data.csv", "w") as file:
    csv_file = csv.writer(file)
    for item in data:
        csv_file.writerow([item['id'], item['sentiment']+ item['text']])
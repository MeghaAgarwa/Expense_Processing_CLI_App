import os
import csv


def read_CSV_from_Folder(folder):
    all_records=[]
    file_list = os.listdir(folder)
    for file in file_list:
        if file.endswith(".csv"):
            path = os.path.join(folder, file)
            with open(path, newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    all_records.append(row)
    return all_records

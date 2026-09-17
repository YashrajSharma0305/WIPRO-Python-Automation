import csv

def read_csv_data(filepath):
    """
    Reads data from a CSV file and returns a list of tuples.
    Skips the header row.
    """
    data_list = []
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            data_list.append(tuple(row))
    return data_list

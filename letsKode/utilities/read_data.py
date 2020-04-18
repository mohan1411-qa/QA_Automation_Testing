import csv
def getCSVDATA(fileName):
    """create the empty rows"""
    row = []

    """Open the CSV file"""
    file_read = open(fileName,'r')

    """iterate the data"""
    reader = csv.reader(file_read)

    """skip the header"""
    next(reader)

    """append the data"""
    for data in reader:
        row.append(data)

    return row
import csv

data = ""

with open("tweets.csv", "r", encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        for elem in row:
            data += elem.encode('ascii', 'ignore').decode('ascii') + " "
        data = data [:-1]
        data += "\n"

with open("tweets.csv", "w", encoding='utf-8') as csvfile:
    csvfile.write(data)
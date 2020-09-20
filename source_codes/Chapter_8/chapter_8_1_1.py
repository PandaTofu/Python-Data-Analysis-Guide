cat examples/example_6_1.csv

import csv

with open('examples/example_6_1.csv') as fo:
    csv_reader = csv.reader(fo)
    for line in csv_reader:
        print(line)

with open('examples/example_6_1.csv') as fo:
    csv_reader = csv.reader(fo)
    rows = list(csv_reader)

data_header, data_values = rows[0], rows[1:]

data_dict = dict(zip(data_header, zip(*data_values)))

data_dict

from pandas import DataFrame

data_df = DataFrame(data_dict)

data_df

with open('examples/example_6_2.csv') as fo:
    csv_reader = csv.reader(fo, delimiter=';', quotechar='\'')
    for line in csv_reader:
        print(line)

with open('examples/example_6_1.csv') as fo:
    reader = csv.DictReader(fo)
    for row in reader:
        print(row)

cat examples/example_6_3.csv

with open('examples/example_6_3.csv') as fo:
    csv_reader = csv.reader(fo, delimiter=' ')
    for line in csv_reader:
        print(line)


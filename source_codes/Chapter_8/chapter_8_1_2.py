import csv

from pandas import Series

s1 = Series([1, 2, 3], index=['x', 'y', 'z'])

with open('export_data.csv', 'w') as fo:
    csv_writer = csv.writer(fo)
    csv_writer.writerow(s1.index)
    csv_writer.writerow(s1)

cat export_data.csv

with open('export_data.csv', 'w') as fo:
    csv_writer = csv.writer(fo, delimiter=';')
    csv_writer.writerow(s1.index)
    csv_writer.writerow(s1)

cat export_data.csv

with open('export_data.csv', 'w') as fo:
    csv_writer = csv.DictWriter(fo, fieldnames=list(s1.index))
    csv_writer.writeheader()
    csv_writer.writerow(s1.to_dict())

cat export_data.csv


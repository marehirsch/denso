import csv
import pandas as pd

command = "G1 X"
name = input("file name: ")

txt_file = name +r".txt"
csv_file = name +r".csv"
with open(txt_file, 'r') as infile, open(csv_file, 'w') as outfile:
         stripped = (line.strip() for line in infile if line.startswith(command))
         lines = (line.split(" ") for line in stripped if line)
         writer = csv.writer(outfile)
         writer.writerows(lines)

# boundaries for columns to keep
begin = 1
end = 3

with open(name +".csv", "r") as file_in:
    with open(name +"_clean.csv", "w") as file_out:

        writer = csv.writer(file_out)

        for row in csv.reader(file_in):
            writer.writerow(row[begin:end])


df = pd.read_csv(name +"_clean.csv", sep='[X]|[Y]|[,]', header=None)
df.to_csv(r'extra_clean.csv',float_format='%.3f',index=False)

X = 1
Y = 3

with open("extra_clean.csv", "r") as file_in:
    with open("super_clean.csv", "w") as file_out:

        writer = csv.writer(file_out)

        for row in csv.reader(file_in):
            writer.writerow({row[X],row[Y]})

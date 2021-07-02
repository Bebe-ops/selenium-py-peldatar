import csv


with open('table_in.csv', encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    with open("table2.csv", "w", encoding="UTF-8") as filtered_file:
        for row in reader:
            filt = row[0:2]
            filt[0] = filt[0].strip()
            filt[1] = filt[1].strip()
            writer = csv.writer(filtered_file)
            writer.writerow(filt)

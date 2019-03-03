import csv
#select .txt file to parse as .csv.
with open('ocrtest2.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
#determine delimiter in quotation marks.
    lines = (line.split(",") for line in stripped if line)
#determine .csv filename
    with open('ocr_to_csv_test.csv', 'w') as out_file:
        writer = csv.writer(out_file)
#specify .csv column headers
        writer.writerow(('name', 'profession', 'address'))
        writer.writerows(lines)

import csv

with open('files_csv_parse_old.csv', 'r') as fr:
    reader = csv.DictReader(fr)
    with open('files_csv_parse_new.csv', 'w') as fw:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(fw, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()
        for line in reader:
            del line['email']
            writer.writerow(line)

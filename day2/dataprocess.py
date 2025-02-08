from csv import writer
from csv import reader


default_text = 'some text'

with open('data.csv','r') as read_obj:
    with open('newdata.csv','w',newline="")as write_obj:
        csv_reader = reader(read_obj)
        csv_writer = writer(write_obj)
        for row in csv_reader:
            row.append(default_text)
            csv_writer.writerow(row)

print("all work done ")            

'''

load the emps.csv file into the memory then read all the data from the file and remove the 

the email colum and remaing data write in another file 

'''

import csv
with open ("emps.csv","r") as fr:
    csv_data=csv.DictReader(fr)
    with open("newemps.csv","w") as fw:
        columns=['fname','lname']
        csvwriter=csv.DictWriter(fw,fieldnames=columns,delimiter=',',lineterminator='\n')
        csvwriter.writeheader()
        for row in csv_data:
            del row['email']
            csvwriter.writerow(row)

print("process done")            
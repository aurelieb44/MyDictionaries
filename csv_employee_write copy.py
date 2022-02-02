import csv

employeepay = open('employeepay.csv','r')

employeepay_file = csv.reader(employeepay, delimiter=',')

outfile = open('emp_details.csv', 'w')

#to skip a line if the file contains a header record
next(employeepay_file)  

outfile.write("ID"+","+"First Name"+","+"Last Name"+","+"Salary"+","+"Bonus"+","+"Total Pay"+"\n")

for record in employeepay_file:
    bonus = round(float(record[3])*float(record[4]),2)
    totalpay = round(float(record[3])+float(record[3])*float(record[4]),2)
    outfile.write(str(record[0])+","+str(record[1])+","+str(record[2])+","+str(record[3])+","+str(bonus)+","+str(totalpay)+"\n")

outfile.close()



    





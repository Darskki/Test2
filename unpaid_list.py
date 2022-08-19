import os
import glob
import csv
import sys

from datetime import datetime, timedelta
from cestaPath import pathFile_inp


## cesta do souboru, ext .csv soubory
path = pathFile_inp
extension = 'csv'
os.chdir(path)
files = glob.glob('*.{}'.format(extension))

unpaidIn = []

## podminka pro soubory
for i in files:
    # print(i)
    with open(i, newline='') as f:

        reader = csv.reader(f, delimiter=';')
        ## delimiter ';' pro lepsi zobrazeni
        try:
            for row in reader:
                # ziskat IsPayed hodnoty sloupce
                isPayed = row[6]
                invoiceDate = row[1]
                invoiceDate = datetime.strptime(invoiceDate, '%Y-%m-%d %H:%M:%S')
                invoiceDate = invoiceDate.strftime('%Y-%m-%d')
                today = datetime.today().strftime('%Y-%m-%d')
                # print(row[6])
                # print(i)

                # pokud je Day dneska
                if invoiceDate == today:
                    unpaidIn.append(i)
                    # if IsPayed equals to 0 append file to list of unpaid invoices
                    if isPayed == 0:
                        print(i + " is unpaid and was added to final list")
                    else:
                        print(i + " is paid")
                else:
                    print(i + " is not today")

        except csv.Error as e:

            sys.exit('file {}, line {}: {}'.format(i, reader.line_num, e))

if unpaidIn == []:
    print("There are no unpaid invoices for today")
    exit()
else:
    print("There are " + str(len(unpaidIn)) + " unpaid invoices for today")





    ## Ulozit + zapsat results pro podminku

# data to be written row-wise in csv file
write_file = "unPaidLIST.csv"
data = unpaidIn

with open(write_file, "wt", encoding="utf-8") as output:
    output.write('\n There are unpaid invoices: \n')
    for line in unpaidIn:
        output.write(line + '\n')

print("\n "">>> All unpaid invoices for today are saved in --> (  unPaidLIST.csv  ) FILE")
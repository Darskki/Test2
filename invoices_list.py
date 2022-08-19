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
madeIn = []

## podminka pro soubory
for i in files:
    # print(i)
    with open(i, newline='') as f:

        reader = csv.reader(f, delimiter=';')
        ## delimiter ';' pro lepsi zobrazeni
        try:
            for row in reader:

                # print(row[1])
                ## row[1] vypise sloupec /rok/mesic/den/hodinu/minutu/vterinu

                invoiceDate = row[1]
                invoiceDate = datetime.strptime(invoiceDate, '%Y-%m-%d %H:%M:%S')
                invoiceDate = invoiceDate
                delta = datetime.now() - timedelta(days=30)
                # print(row[1])
                print(i)
                ## print(i) nacita slozky o par setin rychleji :D
                if invoiceDate > datetime.now():
                    print('invoice is in future')

                else:
                    if invoiceDate > delta:
                        madeIn.append(i)
                        # writer = csv.writer(f, delimiter='|')
                        # writer.writerows(madeIn)
                        print(i + ' >>> invoice was made in last 30 days')


                    else:
                        print('invoice was made after 30 days')



        except csv.Error as e:

            sys.exit('file {}, line {}: {}'.format(i, reader.line_num, e))

if madeIn == []:
    print("There are no unpaid invoices for today")
    exit()
else:
    print("There are " + str(len(madeIn)) + " invoices created in last 30 days.")


    ## Ulozit + zapsat results pro podminku

# data to be written row-wise in csv file
write_file = "invoicesCreatedLastMonth.csv"
data = madeIn

with open(write_file, "wt", encoding="utf-8") as output:
    output.write('These invoices was made in last 30 days: \n')
    for line in madeIn:
        output.write(line + '\n')

print("\n "">>> All Invoices created last month are saved in --> (  invoicesCreatedLastMonth.csv  ) FILE")
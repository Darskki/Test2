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

amountIn = []
amountInVAT = []
vyber = amountIn
vyberVAT = amountInVAT

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
                # print(i)
                ## print(i) nacita slozky o par setin rychleji :D
                if invoiceDate > datetime.now():
                    print('invoice is in future')

                else:
                    if invoiceDate > delta:
                        ## vlozit dalsi podminku na vypis sloupce + soucet
                        pocet = row[3]
                        pocetVAT = row[4]
                        amountIn.append(pocet)
                        print(pocet)

                        amountInVAT.append(pocet)
                        amountInVAT.append(pocetVAT)



                        # print(i + ' >>> Total amount in last 30 days')



                    else:
                        print('invoice was made after 30 days')



        except csv.Error as e:

            sys.exit('file {}, line {}: {}'.format(i, reader.line_num, e))

if amountIn == []:
    print("There is nothing for today")
    exit()
else:
    print("\nTotal invoices is " + str(len(amountIn)) + " in last 30 days.")





## soucet row[4] za posledni mesic
## without VAT

# def _sum(amountIn):
#     sum = 0
#
#     for i in amountIn:
#         sum = sum + int(i)
#
#     return (sum)
#
# ##
#
#
#
# n = len(amountIn)
# ans = _sum(amountIn)
#
# print('Total amount for last month (Without VAT) is: ', ans)
#
#
#     ## Ulozit + zapsat results pro podminku
#
#
#
# write_file = "totalAmount.csv"
# suma = ans
#
# with open(write_file, "wt", encoding="utf-8") as output:
#     output.write('Total amount in last 30 days\n')
#     output.write(str(suma) + '\n')
#
#
#
# print("\n "">>> Total amount for last 30 days with/without VAT is save in  --> (  totalAmount.csv  ) FILE")




## soucet row[4] za posledni mesic
## with VAT

def _sumVAT(amountInVAT):
    sum = 0

    for i in amountInVAT:
        sum = sum + int(i)

    return (sum)

n = len(amountInVAT)
ans = _sumVAT(amountInVAT)

print('Total amount for last month (Without VAT) is: ', ans)


    ## Ulozit + zapsat results pro podminku



write_file = "totalAmountVAT.csv"
sumaVAT = ans

with open(write_file, "wt", encoding="utf-8") as output:
    output.write('Total amount with VAT in last 30 days\n')
    output.write(str(sumaVAT) + '\n')



print("\n "">>> Total amount for last 30 days with/without VAT is save in  --> (  totalAmountVAT.csv  ) FILE")


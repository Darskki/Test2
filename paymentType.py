import os
import glob
import csv

from cestaPath import pathFile_inp


## cesta do souboru, ext .csv soubory
path = pathFile_inp
extension = 'csv'
os.chdir(path)
files = glob.glob('*.{}'.format(extension))

amountIn = []
amountInVAT = []

## podminka pro soubory
for i in files:
    # print(i)
    with open(i, newline='') as f:

        reader = csv.reader(f, delimiter=';')
        ## delimiter ';' pro lepsi zobrazeni
        # try:


'''''
Zde budu pokracovat - if paid = "card" / if paid="pay_by_link" ...
            pocet = row[3]
            pocetVAT = row[4]
            amountIn.append(pocet)
            print(pocet)

            amountInVAT.append(pocet)
             amountInVAT.append(pocetVAT)
'''''

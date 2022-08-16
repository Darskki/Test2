import os
import glob
from cestaPath import pathFile_inp
from datetime import datetime, timedelta
import csv
import sys


path = pathFile_inp
extension = 'csv'
os.chdir(path)
files = glob.glob('*.{}'.format(extension))

# invoiceCreation = 5555555555['Creation'][0]
# invoiceDate = 5555555555['Date'][0]

for i in files:
    # print(i)
    with open(i, newline='') as f:
        #####################################################
        # invoiceDate = datetime.strptime(invoiceDate, '%Y-%m-%d %H:%M:%S')
        # invoiceDate = invoiceDate.strftime('%Y-%m-%d')
        # today = datetime.today().strftime('%Y-%m-%d')
        #####################################################

        reader = csv.reader(f, delimiter=';')
        try:
            for row in reader:
                # invoiceDate = datetime.strptime(invoiceDate, '%Y-%m-%d %H:%M:%S')
                # if invoiceDate < 30:
                    print(row[1])

        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(i, reader.line_num, e))


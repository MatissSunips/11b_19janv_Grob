import csv

def ola(csv1):
        with open(csv1, 'r', encoding='utf-8') as kk:
            kk2 = csv.reader(kk)

            print("Otrās kolonnas dati: ")
            for rinda in kk2:
                if len(rinda) > 1:
                    print(rinda[1])
csv1 = '2uzd.csv'

ola(csv1)


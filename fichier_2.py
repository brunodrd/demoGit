import csv
from melange import former_groupes

with open('nsi.csv', newline='') as fp:
    classe = csv.reader(fp, delimiter=';')
    speNSI = [e[0] for e in classe]
print(speNSI)

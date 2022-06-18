# pcost.py
#
# Exercise 1.27

import sys

def portfolio_cost(filename):
    f=open(filename, 'rt')
    headers=next(f).split(',')
    total=0
    for line in f:
        row = line.split(',')
        total=total+ int(row[1])*float(row[2])
    return 'Total Cost',total

    f.close()

filename=sys.argv[1]
if len(sys.argv) ==2:
    file_name=sys.argv[1]
else:
    filename = 'Data/portfolio.csv'


cost=portfolio_cost(filename)
print(cost)
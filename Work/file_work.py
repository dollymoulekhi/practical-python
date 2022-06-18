f=open('Data/portfolio.csv', 'rt')
headers=next(f).split(',')
print(headers)
for line in f:
    row = line.split(',')
    print(row)

f.close()
# data
# print(data)
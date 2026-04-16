

myData = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

# 1
designations = []
codes = []

my_dict = {}

# 2
for i in myData:
    if i.isdigit():
        codes.append(i)
    else:
        designations.append(i)
    

print(f'destignation: {designations}')
print(f'codes: {codes}')

# 3
operators = dict(zip(designations, codes))

# 4
operators.pop('Katel')
operators.pop('Fonex')

# 5
for key in operators:
    operators[key] = {operators[key]}

operators['O!'].update(['0700', '0500'])
operators['Megacom'].update(['0999', '0555'])
operators['Beeline'].update(['0222', '0777'])


# 6
print(f'operators: {operators}')

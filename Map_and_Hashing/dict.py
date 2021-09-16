locations = {'North America':{'USA':['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India':['Bangalore']}
locations['Asia']['China']=['Shanghai']
locations['Africa'] = {'Egypt':['Cairo']}
print(1)
usa_sorted = sorted(locations['North America']['USA'])
for city in usa_sorted:
    print (city)

print(2)

asia_list = []
for i, j in locations['Asia'].items():
    _asia = j[0] + "-" + i
    asia_list.append(_asia)

asia_sorted = sorted(asia_list)

for item in asia_sorted:
    print(item)
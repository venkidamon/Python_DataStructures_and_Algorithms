x = "1223334.5453453"

y = [a for a in x.split('.') if a]


for b in x.split('.'):
    if b:
        print(b)
print(y)
a = [12,3,6,85,422,1,23]
b = 'bananinha'

i=0

a = [12,3,6,85,422,1,23]
b = 'bananinha'

i = 0

while i < len(a) - 1:
    if a[i] > a[i+1]:
        aux = a[i]
        a[i] = a[i+1]
        a[i+1] = aux
    i += 1

print(a)

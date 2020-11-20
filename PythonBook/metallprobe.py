liste = [('Gold', 0.1234), ('Silber', 23.45), ('Platin', 0.0678)]

for i in liste:
    print(i[0], i[1], end=" // ")

print()
print()

for i in liste:
    print(i[0], i[1], sep='\t\t')

print()
print()

for i in liste:
    print(i[0] + "\t", format(i[1], "4.2f"))

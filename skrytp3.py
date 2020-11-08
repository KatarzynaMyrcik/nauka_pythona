samochody = ['syrena', 'poloneza']

print(samochody[0])
print(samochody[1])

for s in samochody:
    print("samochod to " + s)

print("petla z idx:")
for idx in [0,1]:
    print(samochody[idx])

print("petla numer trzy po indeksie")
print("len:{0}".format(len(samochody)))
print("range: {0}".format(range(4)))

for idx in range (len(samochody)):#len(samochody wyswietla dlugosc tablicy)
    print("{0} {1}".format(idx,samochody[idx]))
#    print("idx: " + " : " + samochody[idx])

#print(samochody[3])

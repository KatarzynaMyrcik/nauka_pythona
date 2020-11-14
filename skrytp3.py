samochody = ['syrena', 'polonez']

# print(samochody[0])
# print(samochody[1])

# for po dowolnej zmiennej przyjmujacej argunemnty listy
#for dowolna_zmienna in samochody:
#    print("samochod to " + dowolna_zmienna)
#    print("egzekucja for-a")

#petla po wygenerowanym autoatycznie numerze indeksu idx
# for idx in [0, 1]:
#     print(samochody[idx], idx)

# petla numer trzy po numerze indeksu
# print("len:{0}".format(len(samochody)))
# print("range: {0}".format(range(4)))

for idx in range(len(samochody)):  # len(samochody wyswietla dlugosc tablicy)
    print("index to {0}, a samochod to: {1}".format(idx, samochody[idx]))
    print("idx: " + samochody[idx])

#print(samochody[3])


#wizualizacja range. O co walsciwie w tym chodzi
# zmienna = range(5)
# print(zmienna[0:2])
# print(zmienna[2])

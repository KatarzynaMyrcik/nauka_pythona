samochod = ['Pasat', 'Reno']
ilosc = [3, 5]

#print(samochod)
#del samochod[0]
print(samochod)

for idx in range(len(samochod)):
    print("idx: {0} : {1}".format(str(idx),samochod[idx]))
    print("{0} ma ilosc drzwi {1}".format(samochod[idx], ilosc[idx]))

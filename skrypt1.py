marka = 'Peugot'
ilosc_drzwi = int(5)
pojemnosc = int(1.3)
zmienna = 'PaKoLaTo'

marka_up = marka.upper()
print("samochod " + marka + " ma " + str(ilosc_drzwi) + " drzwi")
print(marka_up)

#print("pojemnosc po zmianach: " + str(pojemnosc * 2))
poj2 = int(pojemnosc * 2)
pojem = str(poj2)
print("pojemnosc po zmianach: " + pojem)
print("w nazwie " + marka + " jest tyle liter: " + str(len(marka)))


myorder = "chce wyswitlic ilosc drzwi: {1} potem marke: {0} i pojemnosc: {2}"
print (myorder.format(marka, ilosc_drzwi, pojemnosc))

print(zmienna.lower())
marka2 = marka.count('p')
print("ilosc liter p: " + str(marka2))

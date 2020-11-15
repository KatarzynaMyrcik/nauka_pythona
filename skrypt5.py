samochod = 'Kija'
#
# arr = "a,b,c,d,e".split(',')
# print(arr)
# print(type(arr))

lista = (",".join(samochod))
print(lista)
print(type(lista))

arr2 = lista.split(',')
print("wynik dzialania splitu to zmienna nastepujaca zmienna {} typu {}".format(arr2, type(arr2)))

arr3 = ("".join(arr2))
print("wynik dzialania joina z '' to nastepujaca zmienna {} typu {}".format(arr3, type(arr3)))

arr4 = (",".join(arr2))
print("wynik dzialania joina z ',' to nastepujaca zmienna {} typu {}".format(arr4, type(arr4)))


kucyk = 'Rainbow Dash'

print("NOwa zmienna to {1}. Nasz kucyk nazywa sie {0}".format(kucyk, type(kucyk)))
kucyk_split = kucyk.split(' ')
print("Po fukcji split z naszego {}a zostalo tylko {}. Jest to zmienna {}. Split podzielil naszego stringa na dwa argumenty".format(kucyk, kucyk_split, type(kucyk_split)))

kucyk_join = ",".join(kucyk)
print(kucyk_join)
print("Wynik dzialania joina to {}. Jest to zmienna typu {}".format(kucyk_join, type(kucyk_join)))
kucyk_join_split = kucyk_join.split(',')
print("Kiedy zrobimy na powstalym stringu splita to otrzymamay {} w formacie {}".format(kucyk_join_split, type(kucyk_join_split)))
print("Teraz postaramy sie dowrocic ten proces. Uwaga!")
nowy_kucyk = "".join(kucyk_join_split)
print("pierwszy krok to stworzenie stringa {}. Typ zmiennej to {}".format(nowy_kucyk, type(nowy_kucyk)))
nowy_kucyk_finalnie = "".join(nowy_kucyk)
nowy_kucyk_finalnie = nowy_kucyk.split(",")
print("Po kolejnym splicie otrzymujemy {} z typem {}".format(nowy_kucyk_finalnie, type(nowy_kucyk_finalnie)))

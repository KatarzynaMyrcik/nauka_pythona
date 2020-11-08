koszyk_item = ['mleko', 'czekolada', 'sok']
koszyk_ilosc = [2,1,3]
koszyk_cena = [30,40,20]

suma = 0.0
for idx in range(len(koszyk_item)):
    item = koszyk_item[idx]
    ile = koszyk_ilosc[idx]
    cena = koszyk_cena[idx]
    print("{0} {1} {2}".format(item, ile, cena))
    suma = suma + cena

if 'mleko' in koszyk_item and 'czekolada' in koszyk_item:
    print('Hurra! Znizka!')
    suma += suma - (suma * 10)/100


print("wartosc koszyka {0}".format(suma))

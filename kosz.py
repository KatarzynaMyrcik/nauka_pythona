#zakupy
products = {
        1: {'nazwa': 'wuszt', 'cena':5},
        2: {'nazwa': 'hawerfloki', 'cena': 2.5},
        3: {'nazwa': 'zymla', 'cena': 1.3},
        4: {'nazwa': 'farfocle', 'cena': 3},
        5: {'nazwa': 'szpyrka', 'cena':3},
        6: {'nazwa': 'szalot', 'cena': 4.2}
        }

sum = 0.0
i = 0
y = 0
products_buyed = []
quantity = []
list_of_prices = []
list_of_products = []


lista = (input("podaj po przecinku numery produktow, ktore chcesz kupic: 1 - wuszt, 2 - hawerfloki, 3 - zymla, 4 - farfocle, 5 - szpyrka, 6 - szalot: "))
products_buyed_strings = lista.split(',')
print(products_buyed_strings)
for b in products_buyed_strings:
    print(b)
    products_buyed.append(int(b))
    take_quantity = input("podaj ile chcesz kupic {}: ".format(b))
    quantity.append(int(take_quantity))
#potrzebne do znizki co 3ci produkt. tworzy liste pojedynczych produktow
    for q in range(int(take_quantity)):
        list_of_products.append(int(b))
print(list_of_products)

for key in products:
     dict2 = products[key]
     # if key in products_buyed:
     #       sum = sum + dict2['cena'] * quantity[i]  #w tym momencie jest OK
     #       i = i + 1
     #       #potrzebny zeby zrobic obnizke o najtanczy produkt:
     #       list_of_prices.append(dict2['cena'])
     if key in list_of_products:
         sum = sum + dict2['cena']
         i = i + 1
         if i % 3 == 0:
             sum = sum - dict2['cena']
         # potrzebny zeby zrobic obnizke o najtanczy produkt:
         list_of_prices.append(dict2['cena'])

#znika 5 % w przypadku zakupu co najmnije 3 rzeczy lub znizka 10 % jesli suma zakupow przekroczy 500 zl.
# Promocje sie lacza
# if i >= 3:
#     sum = sum * 0.95
#     print("Otrzymales rabat 5 %!")
# elif sum >= 500:
#     sum = sum * 0.9
#     print("Cena Twoich zakupow przekroczyla 500 zl! Dostajesz rabat 10 %!")

# znizka na najtanszy produkt jesli klient kupi co najmniej 2 produkty/
# zamiast sortowania mozna uzyc funkcji min(list_of_prices)
# if i >= 2 or any(y >= 2 for y in quantity):
#       list_of_prices.sort()
#       sum = sum - list_of_prices[0]

print("Musisz zaplacic {}".format(sum))

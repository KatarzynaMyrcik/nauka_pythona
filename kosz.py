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
products_buyed = []
quantity = []
i = 0

lista = (input("podaj po przecinku numery produktow, ktore chcesz kupic: 1 - wuszt, 2 - hawerfloki, 3 - zymla, 4 - farfocle, 5 - szpyrka, 6 - szalot: "))
products_buyed_strings = lista.split(',')
print(products_buyed_strings)
for b in products_buyed_strings:
    print(b)
    products_buyed.append(int(b))
    take_quantity = input("podaj ile chces zkupic {}: ".format(b))
    quantity.append(int(take_quantity))

for key in products:
     dict2 = products[key]
     if key in products_buyed:
           sum = sum + dict2['cena']* quantity[i]  #w tym momencie jest OK
           i = i + 1
print("Musisz zaplacic {}".format(sum))

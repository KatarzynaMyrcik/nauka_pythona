prod = ['wuszt', 'hawerfloki', 'zymla', 'farfocle', 'szpyrka', 'szalot']
ceny = [5, 2.5, 1.4, 2.1, 3, 4.2]

lista = str(input("podaj jakie produty chcesz kupic: 1 - wuszt, 2 - hawerfloki, 3 - zymla, 4 - farfocle, 5 - szpyrka, 6 - szalot: "))
#lista = '1,2,3,4'
print(lista)
lista_zakupow = lista.split(',')
print(lista_zakupow)

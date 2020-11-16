#przeszukiwanie slownika w petli
# produkty = {'S1222': 'sukienka trojkat',
#            'P1222':'spodnie krata',
#            'X212': 'konsola do gier'}
# print(produkty)
# igla = 'X2X'
# produkty['X2X'] = 'igla'
# print(produkty)
# if igla in produkty:
#     print('przedmiot o numerze {} istnieje w zbiorze'.format(igla))
#
# if igla in produkty:
# #    print(igla)
#     print("Znalazlem {0}".format(produkty['X2X']))
# else:
#     print("Brak w magazynie {0}".format(produkty['X2X']))
#

produkty = {
            'SS12': {'nazwa': 'sukienka_trojkat', 'rozmiary': ['s','l','xl']},
            'P12' : {'nazwa': 'spodnie', 'rozmiary': ['s','xl']}
            }

# for p in produkty:
#     print(produkty)
#     print(p)
#
for id in produkty:
    p = produkty[id]
#    print(id)
#    print(p)
    print(p['nazwa'])
#    print(p['rozmiary'])
    rozmiary = p['rozmiary']
    for r in rozmiary:
        print(r)
#print(produkty)


# lista w ktorej kazda linia to slownik
# koszyk = [
#            {'nazwa':'mleko', 'cena':'5.3'},
#            {'nazwa':'kaszanka', 'cena':'4'}
# ]
# print(koszyk)

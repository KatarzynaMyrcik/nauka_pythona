#produkty = {'S1222': 'sukienka trojkat',
#            'P1222':'spodnie krata',
#            'X212': 'konsola do gier'}
#print(produkty)
#igla = 'X2X'
#produkty['X2X'] = 'igla'
#print(produkty)
#if igla in produkty:
#     print('istnieje')
#     print(produkty['p12'])

#if igla in produkty:
#    print("Znalazlem {0}".format(igla))
#else:
#    print("Brak w magazynie {0}".format(igla))
#

produkty = {
            'SS12': {'nazwa': 'sukienka_trojka', 'rozmiary': ['s','l','xl']},
            'P12' : {'nazwa': 'spodnie', 'rozmiary': ['s','xl']}
            }
#for p in products:
#    print(produkty)

for id in produkty:
    p = produkty[id]
#    print(p)
    print(p['nazwa'])
    rozmiary = p['rozmiary']
    print(rozmiary)
#    for r in rozmiary:
#        print(r)

#    print(produkty)


#WyNiK Ma BYC Taki:
#sukienka_trojka
#s
#m
#l
#spodnie
#s
#l

#lista w ktorej kazda linia to slownik
#koszyk = [
#            {'nazwa':'mleko', 'cena':'5.3'}
#            {'nazwa':'kaszanka', ''cena':'4'}
#]

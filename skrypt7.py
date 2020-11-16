#cwiczenia ze slownikiem
samolot = {'name': 'boeing',
            'przebieg': 10000,
            'type': 'pasazerski'}
# print(samolot)
# print(samolot['name'])
# print(samolot['type'])
# print(samolot.get('name'))
#dodanie zmiennej do slownika
#print(samolot['nana'])
print(samolot.get('nanan'))
samolot['silnik'] = 'odrzutowy'
print(samolot)

# #petla po kluczu - key
# for klucz in samolot:
#     print("{0}:{1}".format(klucz, samolot[klucz]))

#petla po kluczu i wartosci
for key, value in samolot.items():
    print("{0}:{1}".format(key, value))

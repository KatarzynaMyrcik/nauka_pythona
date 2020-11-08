samolot = {'name': 'boeing',
            'przebieg': 10000,
            'type': 'pasazerski'}
print(samolot)
#print(samolot['name'])
#print(samolot['type'])
print(samolot.get('name'))
#print(samolot['nana'])
#print(samolot.get('nanan'))
samolot['silnik'] = 'odrzutowy'

#petla po kluczu - key
for klucz in samolot:
    print("{0}:{1}".format(klucz, samolot[klucz]))

#petla po kluczu i wartosci
for key, value in samolot.items():
    print("{0}:{1}".format(key, value))


#for key in samolot:
#    print("{0}:{1}".format(key,samolot[key]))

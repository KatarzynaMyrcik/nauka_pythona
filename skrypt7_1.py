skarpetki = {'lewa_paski': 'paski',
            'prawa_paski': 'paski',
            'lewa_kropki':'kropki',
            'lewa_sloneczka':'sloneczka'}
print(skarpetki)
print(skarpetki['lewa_paski'])

skarpetki['lewa_kwiatki'] = 'kwiatki'
print(skarpetki)


#petla po kluczu
#for key in skarpetki:
#    print("Masz w szafie skarpetke w {0}. Jest to skarpetka {1}".format(skarpetki[key], key))


#petla po kluczy i wartosci:
for key, value in skarpetki.items():
    print("Przyszla pora wyprac skarpetke w {1}. Dokladnie chodzi o te {0}".format(key,value))

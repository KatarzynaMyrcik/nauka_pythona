imie = 'Ala'
#imie2 = 'Petronella'
zwierze = 'kot'
zmienna = 'Pe'
zwierze = input("podaj zwierze ")
print ("{0} ma {1}a".format(imie, zwierze))

#zabawa z funcja format oraz if-em
# ile = int(input("podaj ilsc kotow Ali: "))
# if ile == 1:
#     print("{0} ma {1} {2}a".format(imie, ile, zwierze))
# elif ile > 3 and zwierze == 'kot':
#     print("{0} jest straszan kociara. Ma az {1} {2}ow!".format(imie, ile, zwierze))
# else:
#     print("{0} ma {1} {2}ow".format(imie, ile, zwierze))

#moja metoda na sprawszenie czy wyraz zaczyna sie na Pe
imie2= input("podaj imie")
print(imie2[0:2])
if imie2[0:2] == zmienna:
   print("imie {0} zaczyna sie na Pe".format(imie2))
else:
    print("imie {0} nie zaczyna sie na Pe".format(imie2))

#sprawdzenie czy wyraz zaczyna sie na ko
if zwierze.startswith('ko'):
    print("zwierze zaczyna sie na ko")

#sprawdzenie czy wyraz zawiera ot w nazwie
zwierze_lower = zwierze.lower()
if 'ot' in zwierze_lower:
    print("Zwierze ma ot w nazwie")

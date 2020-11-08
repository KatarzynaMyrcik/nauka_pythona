imie = 'Ala'
imie2 = 'Petronella'
zwierze = 'kot'
zmienna = 'Pe'
#print ("{0} ma {1}a".format(imie, zwierze))

ile = int(input("podaj ilsc kotow Ali: "))
if ile == 1:
    print("{0} ma {1} {2}a".format(imie, ile, zwierze))
elif ile > 3 and zwierze == 'kot':
    print("{0} jest straszan kociara. Ma az {1} {2}ow!".format(imie, ile, zwierze))
else:
    print("{0} ma {1} {2}ow".format(imie, ile, zwierze))

#print(imie2[0:2])
#if imie2[0:2] == zmienna:
#    print("imie zaczyna sie na Pe")
#else:
#    print("imie nie zaczyna sie na Pe")
 if zwierze.startswith('ko'):
     print("zwierze zaczyna sie na ko")

if 'ot' in zwierze:
    print("dziala")

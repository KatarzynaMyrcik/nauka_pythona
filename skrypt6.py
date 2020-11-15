# samochod = ['Pasat', 'Reno']
# ilosc = [3, 5]
# print("DLugosc naszej listy to {}".format(len(samochod)))
# print(samochod)
# del samochod[0]
#
# print(samochod)
# samochod[0] = 'Kombi'
# print(samochod)

# for idx in range(len(samochod)):
#     print("idx to: {0}: {1}".format(str(idx),samochod[idx]))
#     print("{0} ma ilosc drzwi {1}".format(samochod[idx], ilosc[idx]))


#klasyczny sposob na tworzenie listy:
woda = ['mineralna','gazowana','kranowa']
print("Klasyczny sposob na tworzenie listy to wypisanie argumentow w nawiasach kwadratowych. Otrzymamy {} nastepujaca: {}".format(type(woda), woda))
#alternatywny sposob na stworzenie listy
kredki = list(('zolta','zielona','rozowa', 'zlota'))
print("Przy zastasowaniu podwojnych nawiasow otrzymamy {} nastepujaca: {}".format(type(kredki), kredki))
#co  sie dzieje jak mamy pojedyncz nawiasy?
puzzle = ('kucyki','kraina czarow','peppa','mala syrenka')
print("Fukcja list moze przyjmowac tylko jeden argument. Potrzebne sa podwojne nawiasy. \n"
      "Kiedy uzywamy pojedynczych nawiasow otrzymujemy {} nastepujaca: {}".format(type(puzzle), puzzle))

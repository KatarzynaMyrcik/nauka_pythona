kucyki = {
        'cynamonka': {'kolor':'szary', 'rodzaj':'latajacy', 'obecnosc_skrzydel':'tak', 'obecnosc_rogu':'nie', 'moce':['milosc','dobro']},
        'Rarity' : {'kolor':'fioletowy', 'rodzaj':'naziemny', 'obecnosc_skrzydel':'nie', 'obecnosc_rogu':'tak', 'moce':['wdziek','gust']},
        'RainbowDash': {'kolor':'niebieski','rodzaj':'latajacy', 'obecnosc_skrzydel':'tak', 'obecnosc_rogu':'nie', 'moce':['szybkosc','sprawiedliwosc']},
        'AppleJack': {'kolor':'pomaranczowy','rodzaj':'latajacy', 'obecnosc_skrzydel':'tak','obecnosc_rogu':'nie', 'moce':['pracowitosc','przyjacielskosc','sila']}
        }
print(kucyki)

for id in kucyki:
   print(id)
   cechy_kucykow = kucyki[id]
#   print(cechy_kucykow)
#    print(cechy_kucykow['moce'])
   moc = cechy_kucykow['moce']
   for m in moc:
       print(m)

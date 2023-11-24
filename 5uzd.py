"""
Izveidojiet Python programmu, kas atkarībā no pašreizējās stundas izvada atbilstošu sveicienu, izmantojot if priekšrakstu. (labrīt, labdien, labvakar)
"""
def sveiciens(a=int(input("ievadiet pulksteņa laiku!"))):
    if a>6 and a<12:
        print ( f'Labrīt!')
    if a>12 and a<18:
        print ( f'Labdien!')
    if a>18 and a<24:
        print (f'Labvakar!')
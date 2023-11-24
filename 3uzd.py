"""
Izveidojiet Python programmu, kas pārbauda, vai ievadītais skaitlis ir nepāra, izmantojot if priekšrakstu.
"""
a=int(input("Ievadi sakaitli "))
if a%2==0:
    print(f"Jūs, esat ievadījis pāra skaitli!",a)
if a%2==1:
    print(f"Jūs, ievadījāt nepāra skaitli!", a)

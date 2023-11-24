"""
Izveidojiet Python programmu, kas aprēķina lietotāja ievadīta skaitļa faktoriālu, izmantojot for ciklu.
"""

def faktorials(skaitlis):
    rezultats = 1
    for i in range(1, skaitlis + 1):
        rezultats *= i
    return rezultats

# Lietotāja ievade
ievaditais_skaitlis = int(input("Ievadiet skaitli, lai aprēķinātu faktoriālu: "))

# Aprēķina faktoriālu un izvada rezultātu
print(f"Faktoriāls no {ievaditais_skaitlis} ir: {faktorials(ievaditais_skaitlis)}")
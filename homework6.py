#Tapsiriq 6
import random

gizli_eded = random.randint(1, 10)
cehd_sayi = 3

print("1 ilə 10 arasında gizli ədədi tapmağa çalış! (3 cəhdin var)")

for cehd in range(1, cehd_sayi + 1):
    texmin = int(input(f"{cehd}. cəhd: "))

    if texmin == gizli_eded:
        print("Təbriklər!")
        break
    elif texmin < gizli_eded:
        print(" Daha böyük bir ədəd seçin.")
    else:
        print(" Daha kicik bir ədəd seçin.")

if texmin != gizli_eded:
    print(f"Gizli ədəd {gizli_eded} idi.")

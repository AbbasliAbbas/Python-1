#Tapsiriq 3
ededler = []

for i in range(5):
    eded = int(input(f"{i+1}-ci ədədi daxil et: "))
    ededler.append(eded)


fərqli_ededler = set(ededler) 
cem = sum(fərqli_ededler)

print("Daxil edilən ədədlər:", ededler)
print("Fərqli ədədlərin cəmi:", cem)

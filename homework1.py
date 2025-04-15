#Tapsiriq 1
eded1 = float(input("Birinci ededi daxil edin:"))
eded2 = float(input("Ikinci ededi daxil edin:"))
emeliyyat = input("+, -, *, /): ")


if emeliyyat == "+":
    netice = eded1 + eded2
    print("Netice",netice)
elif emeliyyat == "-":
    netice = eded1 - eded2
    print("Netice",netice)
elif emeliyyat == "*":
    netice = eded1 * eded2
    print("Netice",netice)
elif emeliyyat == "/":
    if eded2 == 0:
        print("Xeta 0 a bolmek olmaz")
    else:
        netice = eded1 / eded2
    print("Netice",netice)
else:
    print("Emeliyyat taninmadi")
    

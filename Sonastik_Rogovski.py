from functions import *

est:list=loe_failist("est.txt")
rus:list=loe_failist("rus.txt")
eng:list=loe_failist("eng.txt")

while True:
    choice = int(input("0 - exit\n1 - gtts\n2 - lisa sõna\n3 - test\n4 - Parandada viga\n5 - est->rus->eng\n6 - salvestamine\n"))
    if choice == 1:
        Heli(rus,est,eng)
        Heli2
        print(rus,est,eng)
    elif choice == 0:
        break
    elif choice == 2:
        uus_sona(rus,est,eng)
    elif choice == 3:
        print()
    elif choice == 4:
        print()
    elif choice == 5:
        estrus_trans(rus,est,eng)
    elif choice == 6:
        salvestamine("est.txt",est)
        salvestamine("rus.txt",rus)
        salvestamine("eng.txt",eng)
    elif choice == 7:
        est:list=loe_failist("est.txt")
        rus:list=loe_failist("rus.txt")
        eng:list=loe_failist("eng.txt")

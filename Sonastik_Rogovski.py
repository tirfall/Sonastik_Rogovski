from functions import *
import io

password=8484

est:list=loe_failist("est.txt")
rus:list=loe_failist("rus.txt")
eng:list=loe_failist("eng.txt")
ind = 0
while True:
    try:
        choice = int(input("0 - exit\n1 - gtts\n2 - lisa sõna\n3 - test\n4 - Parandada viga\n5 - est->rus->eng\n6 - salvestamine\n7 - loe esimene fail\n8 - Vaata sõnastik\n9 - adminipanel\n"))
        if choice == 1:
            Heli(rus,est,eng)
        elif choice == 0:
            salvchoice = str(input("Kas sa tahad salvesta? ")).title()
            if salvchoice == "Jah":
                salvestamine("est.txt",est)
                salvestamine("rus.txt",rus)
                salvestamine("eng.txt",eng)
                break
            else:
                break
        elif choice == 2:
            uus_sona(rus,est,eng)
        elif choice == 3:
            test(rus,est,eng)
        elif choice == 4:
            ind=parandada(rus,est,eng)
            paran(rus,est,eng,ind)
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
        elif choice == 8:
            print(rus,est,eng)
        elif choice == 9:
            anspass=int(input("Sisesta password: "))
            if anspass == password:
                adminchoice = int(input("1 - loe failid reservist\n"))
                if adminchoice == 1:
                    est:list=loe_failist("reserve/est.txt")
                    rus:list=loe_failist("reserve/rus.txt")
                    eng:list=loe_failist("reserve/eng.txt")
                    
    except:
        ValueError
        print("Vale andmetüüp")

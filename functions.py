from os import *
from gtts import gTTS
from random import *
import io
from pydub import AudioSegment

def estrus_trans(rus_list,est_list,eng_list):
    slovo=input('sisesta sõna: ')
    slovo = slovo.title()
    if slovo in rus_list:
        ind=rus_list.index(slovo)
        print(f"{slovo} - {est_list[ind]} - {eng_list[ind]}")
    elif slovo in est_list:
        ind=est_list.index(slovo)
        print(f"{slovo} - {rus_list[ind]} - {eng_list[ind]}")
    elif slovo in eng_list:
        ind=eng_list.index(slovo)
        print(f"{slovo} - {rus_list[ind]} - {est_list[ind]}")
    else:
        print(f"{slovo.upper()} ei ole sõnastikus")
        v=input("kas te soovite lisa sõna?")
        #v = v.title
        if v.lower()=="jah":uus_sona(rus_list,est_list,eng_list)
        else:
            pass

def uus_sona(rus_list,est_list,eng_list):
    slovo_est=input('sisesta sõna eesti: ')
    slovo_est=slovo_est.title()
    est_list.append(slovo_est)
    slovo_rus=input('sisesta sõna vene: ')
    slovo_rus=slovo_rus.title()
    rus_list.append(slovo_rus)
    slovo_eng=input('sisesta sõna inglise: ')
    slovo_eng=slovo_eng.title()
    eng_list.append(slovo_eng)
    

def loe_failist(f):
    fail=io.open(f, "r", encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas

def salvestamine(fail,jarjend):
    f = io.open(fail, "w", encoding="utf-8-sig")
    for element in jarjend:
     f.write(element)
     f.write('\n')
    f.close()

def Heli(rus_list,est_list,eng_list):
    """
    Helime failis
    """
    slovo=input('sisesta sõna: ')
    slovo = slovo.title()
    if slovo in rus_list:
        ind=rus_list.index(slovo)
        print(f"{slovo} - {est_list[ind]} - {eng_list[ind]}")
        text= slovo
        keel="ru"
        ju=gTTS(text=text, lang=keel, slow=False)
        ju.save("heli1.mp3")
        text= est_list[ind]
        keel="et"
        ju2=gTTS(text=text, lang=keel, slow=False)
        ju2.save("heli2.mp3")
        text= eng_list[ind]
        keel="en"
        ju3=gTTS(text=text, lang=keel, slow=False)
        ju3.save("heli3.mp3")
    elif slovo in est_list:
        ind=est_list.index(slovo)
        print(f"{slovo} - {rus_list[ind]} - {eng_list[ind]}")
        text= slovo,rus_list[ind],eng_list[ind]
    elif slovo in eng_list:
        ind=eng_list.index(slovo)
        print(f"{slovo} - {rus_list[ind]} - {est_list[ind]}")
        text= slovo,rus_list[ind],est_list[ind]
    #gTTS(text=text, lang=keel, slow=False).save("heli.mp3")
    system("heli.mp3")
def Heli2():
        sound1 = AudioSegment.from_mp3("C:\\Users\\tirfall\\source\\repos\\tirfall\\Sonastik_Rogovski\\heli1.mp3")
        sound2 = AudioSegment.from_mp3("C:\\Users\\tirfall\\source\\repos\\tirfall\\Sonastik_Rogovski\\heli2.mp3")
        sound3 = AudioSegment.from_mp3("C:\\Users\\tirfall\\source\\repos\\tirfall\\Sonastik_Rogovski\\heli3.mp3")
        finalsound=sound1+sound2+sound3
        finalsound.export("C:\\Users\\tirfall\\source\\repos\\tirfall\\Sonastik_Rogovski\\heli.mp3", format="mp3")
        

#from pydub import AudioSegment
#sound1 = AudioSegment.from_mp3("/home/user/bleach.mp3")
#sound2 = AudioSegment.from_mp3("/home/user/dollar.mp3")
#sound3=sound1+sound2
#sound3.export("/home/user/3.mp3", format="mp3")



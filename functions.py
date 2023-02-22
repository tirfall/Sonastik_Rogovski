from os import *
from gtts import gTTS
from random import *

def estrus_trans():
    print()

def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())
    fail.close()
    return mas



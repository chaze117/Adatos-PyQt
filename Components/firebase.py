import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from Components.classes import *

cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://zomboradat-default-rtdb.europe-west1.firebasedatabase.app/'})


def getDolgozok():
        ref = db.reference('dolgozok')
        _temp = ref.get()
        Dolgozok = []
        for i in range(0,len(_temp)):
            Dolgozok.append(Dolgozo.from_dict(_temp[i]))
        return Dolgozok

def getGyerekek():
    ref = db.reference('gyerek')
    _temp = ref.get()
    Gyerekek = []
    for i in range(0,len(_temp)):
        Gyerekek.append(Gyerek.from_dict(_temp[i]))
    return Gyerekek

def getNGyerekek():
    ref = db.reference("gyerek_netak")
    _temp = ref.get()
    Gyerekek_n = []
    for i in range(0,len(_temp)):
        Gyerekek_n.append(Gyerek_NETAK.from_dict(_temp[i]))
    return Gyerekek_n

def getMunkairanyitok():
    ref = db.reference("munkairanyitok")
    _temp = ref.get()
    Munkairanyitok = []
    for i in range(0,len(_temp)):
        Munkairanyitok.append(Munkairanyito.from_dict(_temp[i]))
    return Munkairanyitok

def getMunkakorok():
    ref = db.reference("munkakorok")
    _temp = ref.get()
    Munkakorok = []
    for i in range(0,len(_temp)):
        Munkakorok.append(Munkakor.from_dict(_temp[i]))
    return Munkakorok

def getProgramok():
    ref = db.reference("programok")
    _temp = ref.get()
    Programok = []
    for i in range(0,len(_temp)):
        Programok.append(Program.from_dict(_temp[i]))
    return Programok

def getSzamlaszamok():
    ref = db.reference("szamlaszamok")
    _temp = ref.get()
    Szamlaszamok = []
    for i in range(0,len(_temp)):
        Szamlaszamok.append(Szamlaszam.from_dict(_temp[i]))
    return Szamlaszamok

def getEloado():
    ref = db.reference("beallitasok/eloado")
    eloado = ref.get()
    return eloado
    
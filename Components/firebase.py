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

def fillSearchCB(Dolgozok,searchCB:QComboBox):
    searchCB.clear()
    for dolgozo in Dolgozok:
        if dolgozo is not None:
            searchCB.addItem(f"{dolgozo.id}. {dolgozo.nev} - {dolgozo.sz_ido[0:10].replace('-','.')}")
    
    
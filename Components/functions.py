import datetime
from datetime import date, timedelta
from Components.orvosi import TableModel as orvosiTM
from Components.programok import TableModel as progTM
from Components.tuzelo import TableModel as tuzeloTM
from Components.munkairanyito import TableModel as mirTM
import Components.firebase as FB
from firebase_admin import db
from Components.classes import *

def SelectedDolgozo(window:any):
    SzemAdat = window.tabs_widget.tab1.szemadatF
    JogvAdat = window.tabs_widget.tab1.jvF
    today = date.today()
    if window.tabs_widget.tab1.searchCB.currentText() != '':
        id = window.tabs_widget.tab1.searchCB.currentText().split('.')
        id = int(id[0])

        SzemAdat.nameT.setText(window.Dolgozok[id].nev)
        SzemAdat.lnameT.setText(window.Dolgozok[id].l_nev)
        SzemAdat.anameT.setText(window.Dolgozok[id].a_nev)
        SzemAdat.szhT.setText(window.Dolgozok[id].sz_hely)
        y,m,d = window.Dolgozok[id].sz_ido[0:10].split('-')
        SzemAdat.sziD.setDate(QDate(int(y),int(m),int(d)))
        SzemAdat.adoT.setText(window.Dolgozok[id].ado_sz)
        SzemAdat.tajT.setText(window.Dolgozok[id].taj_sz)
        SzemAdat.cimT.setText(window.Dolgozok[id].cim)
        szamla = window.Dolgozok[id].szamla_sz.replace('-','').replace('8x0','00000000')
        if len(szamla) == 0:
                SzemAdat.szamlaT.setInputMask("")
        elif len(szamla) < 17:
            SzemAdat.szamlaT.setInputMask("99999999-99999999")
        else:
            SzemAdat.szamlaT.setInputMask("99999999-99999999-99999999")
        SzemAdat.szamlaT.setText(szamla)
        telefon = window.Dolgozok[id].tel_sz.replace("-","").replace("/","")
        SzemAdat.telT.setText(telefon)
        SzemAdat.szigT.setText(window.Dolgozok[id].szigsz)
        SzemAdat.tuzelo.setChecked(window.Dolgozok[id].tuzelo)
        y,m,d = window.Dolgozok[id].jog_k[0:10].split('-')
        JogvAdat.jkD.setDate(QDate(int(y),int(m),int(d)))
        y,m,d = window.Dolgozok[id].jog_v[0:10].split('-')
        JogvAdat.jvD.setDate(QDate(int(y),int(m),int(d)))
        JogvAdat.mkC.setCurrentIndex(window.Dolgozok[id].munkakor)
        JogvAdat.nettoT.setText(str(window.Munkakorok[window.Dolgozok[id].munkakor].netto))
        JogvAdat.progC.setCurrentIndex(window.Dolgozok[id].pid-1)
        JogvAdat.mirC.setCurrentIndex(window.Dolgozok[id].mir-1)
        JogvAdat.ugyT.setText(window.Dolgozok[id].ugyirat)
        y,m,d = window.Dolgozok[id].orvosi[0:10].split('-')
        JogvAdat.orvosiT.setDate(QDate(int(y),int(m),int(d)))
        fillCSJK(window,id)
        fillNETAK(window,id)

def fillCSJK(window:any,id):
    CSJK = window.tabs_widget.tab1.adoF.tab1
    today = date.today()
    CSJK.CSJKCB.clear()
    CSJK.nameT.clear()
    CSJK.anevT.clear()
    CSJK.szhT.clear()
    CSJK.sziD.setDate(today)
    CSJK.adoT.clear()
    CSJK.tajT.clear()
    CSJK.cimT.clear()
    for gyerek in window.Gyerekek:
        if gyerek is not None and int(gyerek.sz_id) == id:
                CSJK.CSJKCB.addItem(f"{gyerek.id}. {gyerek.nev} - {gyerek.sz_ido[0:10].replace('-','.')}")

def fillNETAK(window:any,id):
    NETAK = window.tabs_widget.tab1.adoF.tab2
    today = date.today()
    NETAK.NETAKCB.clear()
    NETAK.nameT.clear()
    NETAK.anevT.clear()
    NETAK.szhT.clear()
    NETAK.sziD.setDate(today)
    NETAK.adoT.clear()
    for gyerek in window.Gyerekek_n:
        if gyerek is not None and int(gyerek.sz_id) == id:
                NETAK.NETAKCB.addItem(f"{gyerek.id}. {gyerek.nev} - {gyerek.sz_ido[0:10].replace('-','.')}")

def SelectedCSJK(value,window:any):
    CSJK = window.tabs_widget.tab1.adoF.tab1
    if value > -1:
        id = CSJK.CSJKCB.currentText().split('.')
        id = int(id[0])
        CSJK.nameT.setText(window.Gyerekek[id].nev)
        CSJK.anevT.setText(window.Gyerekek[id].a_nev)
        CSJK.szhT.setText(window.Gyerekek[id].sz_hely)
        y,m,d = window.Gyerekek[id].sz_ido[0:10].split('-')
        CSJK.sziD.setDate(QDate(int(y),int(m),int(d)))
        CSJK.adoT.setText(window.Gyerekek[id].ado)
        CSJK.tajT.setText(window.Gyerekek[id].taj)
        CSJK.cimT.setText(window.Gyerekek[id].cim)

def SelectedNETAK(value,window:any):
    NETAK = window.tabs_widget.tab1.adoF.tab2
    if value > -1:
        id = NETAK.NETAKCB.currentText().split('.')
        id = int(id[0])
        NETAK.nameT.setText(window.Gyerekek_n[id].nev)
        NETAK.anevT.setText(window.Gyerekek_n[id].a_nev)
        NETAK.szhT.setText(window.Gyerekek_n[id].sz_hely)
        y,m,d = window.Gyerekek_n[id].sz_ido[0:10].split('-')
        NETAK.sziD.setDate(QDate(int(y),int(m),int(d)))
        NETAK.adoT.setText(window.Gyerekek_n[id].ado)

def fillSearchCB(window:any):
    window.tabs_widget.tab1.searchCB.clear()
    for dolgozo in window.Dolgozok:
        if dolgozo is not None:
            window.tabs_widget.tab1.searchCB.addItem(f"{dolgozo.id}. {dolgozo.nev} - {dolgozo.sz_ido[0:10].replace('-','.')}")

def fillMunkakorCB(window:any):
     window.tabs_widget.tab1.jvF.mkC.clear()
     window.tabs_widget.tab6.mkCb.clear()
     for munkakor in window.Munkakorok:
       if munkakor is not None:
        window.tabs_widget.tab1.jvF.mkC.addItem(f"{munkakor.id}. {munkakor.nev}")
        window.tabs_widget.tab6.mkCb.addItem(f"{munkakor.id}. {munkakor.nev}")

def fillProgramCB(window:any):
    window.tabs_widget.tab1.jvF.progC.clear()
    window.tabs_widget.tab2.progCB.clear()
    window.tabs_widget.tab3.progCB.clear()
    window.tabs_widget.tab6.pgCb.clear()
    for program in window.Programok:
      if program is not None:
        window.tabs_widget.tab1.jvF.progC.addItem(f"{program.id}. {program.r_nev}")
        window.tabs_widget.tab2.progCB.addItem(f"{program.id}. {program.r_nev}")
        window.tabs_widget.tab3.progCB.addItem(f"{program.id}. {program.r_nev}")
        window.tabs_widget.tab6.pgCb.addItem(f"{program.id}. {program.r_nev}")

def fillMunkairanyitoCB(window:any):
    window.tabs_widget.tab1.jvF.mirC.clear()
    window.tabs_widget.tab5.munkCB.clear()
    window.tabs_widget.tab6.miCb.clear()
    for munkairanyito in window.Munkairanyitok:
      if munkairanyito is not None:
        window.tabs_widget.tab1.jvF.mirC.addItem(f"{munkairanyito.id}. {munkairanyito.nev}")
        window.tabs_widget.tab5.munkCB.addItem(f"{munkairanyito.id}. {munkairanyito.nev}")
        window.tabs_widget.tab6.miCb.addItem(f"{munkairanyito.id}. {munkairanyito.nev}")
        
def fillOrvosiData(window:any):
    today = date.today()
    window.tabs_widget.tab2.oLabel.setText(f"Lejár {window.tabs_widget.tab2.oSlider.value()} napon belül")
    oData = []
    if window.tabs_widget.tab2.progCB.currentText() != "":
        id = window.tabs_widget.tab2.progCB.currentText().split('.')
        id = int(id[0])
        newtime = today + timedelta(days=window.tabs_widget.tab2.oSlider.value())
        for dolgozo in window.Dolgozok:
            if dolgozo is not None and dolgozo.pid == id:
                    y,m,d = dolgozo.orvosi[0:10].split('-')
                    dolOrv = datetime.date(int(y),int(m),int(d))
                    if dolOrv < newtime:
                        oData.append((dolgozo.id,dolgozo.nev,dolgozo.sz_hely,dolgozo.sz_ido[0:10],dolgozo.a_nev,dolgozo.cim,dolgozo.taj_sz.replace("-",""),dolgozo.orvosi[0:10].replace('-','.')))
        oData.sort(key=lambda x: x[1])
        oData.append(("","","","","","","",""))
        model = orvosiTM(oData)
        window.tabs_widget.tab2.table.setModel(model)

def fillProgramData(window:any):
      if window.tabs_widget.tab3.progCB.currentText() != '':
        id = window.tabs_widget.tab3.progCB.currentText().split('.')
        id = int(id[0])
        progData = []
        for dolgozo in window.Dolgozok:
                if dolgozo is not None and dolgozo.pid == id:
                    progData.append((dolgozo.id,dolgozo.nev,dolgozo.sz_ido[0:10].replace('-','.'),dolgozo.taj_sz,dolgozo.ado_sz,dolgozo.jog_k[0:10].replace('-','.')))
        progData.sort(key=lambda x: x[1])
        progData.append(("","","","","","","",""))
        model = progTM(progData)
        window.tabs_widget.tab3.table.setModel(model)

def fillTuzeloData(window:any, refresh:bool):
    if refresh is True:
        window.Dolgozok = FB.getDolgozok()
    tuzeloData = []
    for dolgozo in window.Dolgozok:
        if dolgozo is not None and dolgozo.tuzelo == True:
                cim = dolgozo.cim.split(" ")
                hsz = cim[len(cim)-1].replace('.','')
                tuzeloData.append((dolgozo.id,dolgozo.nev,cim[0],hsz))
    tuzeloData = sorted(tuzeloData, key = lambda x: (x[2], int(x[3])))
    model = tuzeloTM(tuzeloData)
    window.tabs_widget.tab4.table.setModel(model)

def FillMunkairanyitoData(window:any):
    if window.tabs_widget.tab5.munkCB.currentText() != '':
        id = window.tabs_widget.tab5.munkCB.currentText().split('.')
        id = int(id[0])
        munkairData = []
        for dolgozo in window.Dolgozok:
            if dolgozo is not None and dolgozo.mir == id:
                    munkairData.append((dolgozo.id, dolgozo.nev,dolgozo.sz_ido[0:10].replace('-','.'),dolgozo.taj_sz,dolgozo.jog_v[0:10].replace('-','.')))
        munkairData.sort(key=lambda x: x[1])
        munkairData.append(("","","","",""))
        model = mirTM(munkairData)
        window.tabs_widget.tab5.table.setModel(model)

def settingsMunkakorok(window:any):
    if window.tabs_widget.tab6.mkCb.currentText() != '':
        id = window.tabs_widget.tab6.mkCb.currentText().split(".")
        id = int(id[0])
        window.tabs_widget.tab6.mknameT.setText(window.Munkakorok[id].nev)
        window.tabs_widget.tab6.mkbrutT.setText(str(window.Munkakorok[id].brutto))
        window.tabs_widget.tab6.mknetT.setText(str(window.Munkakorok[id].netto))

def modMunkakor(window:any):
     if window.tabs_widget.tab6.mkCb.currentText() != '':
        id = window.tabs_widget.tab6.mkCb.currentText().split(".")
        id = int(id[0])
        munkakor = Munkakor(
            id,
            window.tabs_widget.tab6.mknameT.text(),
            window.tabs_widget.tab6.mkbrutT.text(),
            window.tabs_widget.tab6.mknetT.text())
        ref = db.reference("munkakorok")
        d = json.loads(munkakor.toJSON())
        ref.child(str(munkakor.id)).set(d)
        window.Munkakorok = FB.getMunkakorok()
        fillMunkakorCB(window)

def delMunkakor(window:any):
    if window.tabs_widget.tab6.mkCb.currentText() != '':
        id = window.tabs_widget.tab6.mkCb.currentText().split(".")
        ref = db.reference("munkakorok")
        ref.child(id[0]).set({})
        window.Munkakorok = FB.getMunkakorok()
        fillMunkakorCB(window)

def settingsMunkairanyitok(window:any):
    if window.tabs_widget.tab6.miCb.currentText() != '':
        id = window.tabs_widget.tab6.miCb.currentText().split('.')
        id = int(id[0])
        window.tabs_widget.tab6.minameT.setText(window.Munkairanyitok[id].nev)

def modMunkairanyito(window:any):
    if window.tabs_widget.tab6.miCb.currentText() != '':
        id = window.tabs_widget.tab6.miCb.currentText().split('.')
        munkairanyito = Munkairanyito(int(id[0]), window.tabs_widget.tab6.minameT.text())
        ref = db.reference("munkairanyitok")
        d = json.loads(munkairanyito.toJSON())
        ref.child(str(munkairanyito.id)).set(d)
        window.Munkairanyitok = FB.getMunkairanyitok()
        fillMunkairanyitoCB(window)

def delMunkairanyito(window:any):
    if window.tabs_widget.tab6.miCb.currentText() != '':
        id = window.tabs_widget.tab6.miCb.currentText().split('.')
        ref = db.reference("munkairanyitok")
        ref.child(id[0]).set({})
        window.Munkairanyitok = FB.getMunkairanyitok()
        fillMunkairanyitoCB(window)

def settingsProgramok(window:any):
    if window.tabs_widget.tab6.pgCb.currentText() != "":
        id = window.tabs_widget.tab6.pgCb.currentText().split('.')
        id = int(id[0])
        window.tabs_widget.tab6.pghnevT.setText(window.Programok[id].h_nev)
        window.tabs_widget.tab6.pgrnevT.setText(window.Programok[id].r_nev)
        window.tabs_widget.tab6.pghatT.setText(window.Programok[id].hatosagi)

def modProgram(window:any):
    if window.tabs_widget.tab6.pgCb.currentText() != "":
        id = window.tabs_widget.tab6.pgCb.currentText().split('.')
        program = Program(int(id[0]), window.tabs_widget.tab6.pgrnevT.text(),window.tabs_widget.tab6.pghnevT.text(),window.tabs_widget.tab6.pghatT.text())
        ref = db.reference("programok")
        d = json.loads(program.toJSON())
        ref.child(str(program.id)).set(d)
        window.Programok = FB.getProgramok()
        fillProgramCB(window)

def delProgram(window:any):
    if window.tabs_widget.tab6.pgCb.currentText() != "":
        id = window.tabs_widget.tab6.pgCb.currentText().split('.')
        ref = db.reference("programok")
        ref.child(id[0]).set({})
        window.Programok = FB.getProgramok()
        fillProgramCB(window)

def modDolgozo(window:any):
    if window.tabs_widget.tab1.searchCB.currentText() != "":
        id = window.tabs_widget.tab1.searchCB.currentText().split(".")
        mir = window.tabs_widget.tab1.jvF.mirC.currentText().split(".")
        mkk = window.tabs_widget.tab1.jvF.mkC.currentText().split(".")
        pid = window.tabs_widget.tab1.jvF.progC.currentText().split(".")
        dolgozo = Dolgozo(
            window.tabs_widget.tab1.szemadatF.anameT.text(),
            window.tabs_widget.tab1.szemadatF.adoT.text(),
            window.tabs_widget.tab1.szemadatF.cimT.text(),
            int(id[0]),
            window.tabs_widget.tab1.jvF.jkD.date().toString("yyyy-MM-dd"),
            window.tabs_widget.tab1.jvF.jvD.date().toString("yyyy-MM-dd"),
            window.tabs_widget.tab1.szemadatF.lnameT.text(),
            int(mir[0]),
            int(mkk[0]),
            window.tabs_widget.tab1.szemadatF.nameT.text(),
            window.tabs_widget.tab1.jvF.orvosiT.date().toString("yyyy-MM-dd"),
            int(pid[0]),
            window.tabs_widget.tab1.szemadatF.szhT.text(),
            window.tabs_widget.tab1.szemadatF.sziD.date().toString("yyyy-MM-dd"),
            window.tabs_widget.tab1.szemadatF.szamlaT.text().replace("-",""),
            window.tabs_widget.tab1.szemadatF.szigT.text(),
            window.tabs_widget.tab1.szemadatF.tajT.text().replace("-",""),
            window.tabs_widget.tab1.szemadatF.telT.text().replace("+36/","").replace("-",""),
            window.tabs_widget.tab1.szemadatF.tuzelo.isChecked(),
            window.tabs_widget.tab1.jvF.ugyT.text())
        ref = db.reference("dolgozok")
        d = json.loads(dolgozo.toJSON())
        ref.child(str(dolgozo.id)).set(d)
        window.Dolgozok = FB.getDolgozok()
        fillSearchCB(window)

def delDolgozo(window:any):
    if window.tabs_widget.tab1.searchCB.currentText() != "":
        id = window.tabs_widget.tab1.searchCB.currentText().split('.')
        ref = db.reference("dolgozok")
        ref.child(id[0]).set({})
        window.Dolgozok = FB.getDolgozok()
        fillSearchCB(window)

def modCSJK(window:any):
    if window.tabs_widget.tab1.adoF.tab1.CSJKCB.currentText() != "":
        id = window.tabs_widget.tab1.adoF.tab1.CSJKCB.currentText().split(".")
        pid = window.tabs_widget.tab1.searchCB.currentText().split('.')
        gyerek = Gyerek(
            window.tabs_widget.tab1.adoF.tab1.anevT.text(),
            window.tabs_widget.tab1.adoF.tab1.adoT.text(),
            window.tabs_widget.tab1.adoF.tab1.cimT.text(),
            int(id[0]),
            window.tabs_widget.tab1.adoF.tab1.nameT.text(),
            window.tabs_widget.tab1.adoF.tab1.szhT.text(),
            int(pid[0]),
            window.tabs_widget.tab1.adoF.tab1.sziD.date().toString("yyyy-MM-dd"),
            window.tabs_widget.tab1.adoF.tab1.tajT.text().replace('-','')
        )
        ref = db.reference('gyerek')
        d = json.loads(gyerek.toJSON())
        ref.child(id[0]).set(d)
        window.Gyerekek = FB.getGyerekek()
        fillCSJK(window,int(pid[0]))

def delCSJK(window:any):
    if window.tabs_widget.tab1.adoF.tab1.CSJKCB.currentText() != "":
        pid = window.tabs_widget.tab1.searchCB.currentText().split('.')
        id = window.tabs_widget.tab1.adoF.tab1.CSJKCB.currentText().split(".")
        ref = db.reference("gyerek")
        ref.child(id[0]).set({})
        window.Gyerekek = FB.getGyerekek()
        fillCSJK(window,int(pid[0]))

def modNETAK(window:any):
    if window.tabs_widget.tab1.adoF.tab2.NETAKCB.currentText() != "":
        id = window.tabs_widget.tab1.adoF.tab2.NETAKCB.currentText().split(".")
        pid = window.tabs_widget.tab1.searchCB.currentText().split('.')
        gyerek = Gyerek_NETAK(
                window.tabs_widget.tab1.adoF.tab2.anevT.text(),
                window.tabs_widget.tab1.adoF.tab2.adoT.text(),
                int(id[0]),
                window.tabs_widget.tab1.adoF.tab2.nameT.text(),
                window.tabs_widget.tab1.adoF.tab2.szhT.text(),
                int(pid[0]),
                window.tabs_widget.tab1.adoF.tab2.sziD.date().toString("yyyy-MM-dd"))
        ref = db.reference('gyerek_netak')
        d = json.loads(gyerek.toJSON())
        ref.child(id[0]).set(d)
        window.Gyerekek_n = FB.getNGyerekek()
        fillNETAK(window,int(pid[0]))

def delNETAK(window:any):
    if window.tabs_widget.tab1.adoF.tab2.NETAKCB.currentText() != "":   
        id = window.tabs_widget.tab1.adoF.tab2.NETAKCB.currentText().split(".")
        pid = window.tabs_widget.tab1.searchCB.currentText().split('.')
        ref = db.reference('gyerek_netak')
        ref.child(id[0]).set({})
        window.Gyerekek_n = FB.getNGyerekek()
        fillNETAK(window,int(pid[0]))

def saveEloado(window:any):
    eloado = window.tabs_widget.tab6.eloadoTxT.text()
    ref = db.reference('beallitasok')
    ref.child('eloado').set(eloado)
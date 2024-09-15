from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,PageBreak
from reportlab.lib.units import inch
from reportlab.lib import colors
from Components.classes import Dolgozo
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth,registerFont
from reportlab.pdfbase.ttfonts import TTFont

def generateTuzelo(values):
    pdf_filename = "tuzelo.pdf"
    document = SimpleDocTemplate(pdf_filename, pagesize=A4)
    document.topMargin = 10*mm
    tuzeloData = []

    for dolgozo in values:
        if dolgozo is not None and dolgozo.tuzelo == True:
                cim = dolgozo.cim.split(" ")
                hsz = cim[len(cim)-1].replace('.','')
                tuzeloData.append((dolgozo.id,dolgozo.nev,cim[0],hsz))
    tuzeloData = sorted(tuzeloData, key = lambda x: (x[2], int(x[3])))
    arpad     = [("#","Név","Utca","Házszám","Aláírás")]
    ady       = [("#","Név","Utca","Házszám","Aláírás")]
    arany     = [("#","Név","Utca","Házszám","Aláírás")]
    batthyany = [("#","Név","Utca","Házszám","Aláírás")]
    bercsenyi = [("#","Név","Utca","Házszám","Aláírás")]
    beke      = [("#","Név","Utca","Házszám","Aláírás")]
    damjanich = [("#","Név","Utca","Házszám","Aláírás")]
    dobo      = [("#","Név","Utca","Házszám","Aláírás")]
    dozsa     = [("#","Név","Utca","Házszám","Aláírás")]
    jozsef    = [("#","Név","Utca","Házszám","Aláírás")]
    kinizsi   = [("#","Név","Utca","Házszám","Aláírás")]
    kossuth   = [("#","Név","Utca","Házszám","Aláírás")]
    kolcsey   = [("#","Név","Utca","Házszám","Aláírás")] 
    legelo    = [("#","Név","Utca","Házszám","Aláírás")]
    lehel     = [("#","Név","Utca","Házszám","Aláírás")]
    matyas    = [("#","Név","Utca","Házszám","Aláírás")]
    petofi    = [("#","Név","Utca","Házszám","Aláírás")]
    rakoczi   = [("#","Név","Utca","Házszám","Aláírás")]
    rozsa     = [("#","Név","Utca","Házszám","Aláírás")]
    szabadsag = [("#","Név","Utca","Házszám","Aláírás")]
    szechenyi = [("#","Név","Utca","Házszám","Aláírás")]
    temeto    = [("#","Név","Utca","Házszám","Aláírás")]
    tancsics  = [("#","Név","Utca","Házszám","Aláírás")]
    zrinyi    = [("#","Név","Utca","Házszám","Aláírás")]
    jokai     = [("#","Név","Utca","Házszám","Aláírás")]
    
    x = 1
    alairas = 70
    for dolgozo in tuzeloData:
            if dolgozo[2] == "Ady":
                ady.append((x,dolgozo[1],"Ady Endre utca",dolgozo[3]))
                x = x+1
    adytable = Table(ady,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Arany":
              arany.append((x,dolgozo[1],"Arany János utca",dolgozo[3]))
              x = x+1
    aranytable = Table(arany,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Árpád":
              arpad.append((x,dolgozo[1],"Árpád utca",dolgozo[3]))
              x = x+1
    arpadtable = Table(arpad,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Batthyány":
              batthyany.append((x,dolgozo[1],"Batthyány utca",dolgozo[3]))
              x = x+1
    batthyanytable = Table(batthyany,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Béke":
              beke.append((x,dolgozo[1],"Béke utca",dolgozo[3]))
              x = x+1
    beketable = Table(beke,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Bercsényi":
              bercsenyi.append((x,dolgozo[1],"Bercsényi utca",dolgozo[3]))
              x = x+1
    bercsenyitable = Table(bercsenyi,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Damjanich":
              damjanich.append((x,dolgozo[1],"Damjanich utca",dolgozo[3]))
              x = x+1
    damjanichtable = Table(damjanich,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Dobó":
              dobo.append((x,dolgozo[1],"Dobó István utca",dolgozo[3]))
              x = x+1
    dobotable = Table(dobo,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Dózsa":
              dozsa.append((x,dolgozo[1],"Dózsa György utca",dolgozo[3]))
              x = x+1
    dozsatable = Table(dozsa,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:  
         if dolgozo[2] == "Jókai":
              jokai.append((x,dolgozo[1],"Jókai Mór utca",dolgozo[3]))
              x = x+1
    jokaitable = Table(jokai,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "József":
              jozsef.append((x,dolgozo[1],"József Attila utca",dolgozo[3]))
              x = x+1
    jozseftable = Table(jozsef,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Kinizsi":
              kinizsi.append((x,dolgozo[1],"Kinizsi utca",dolgozo[3]))
              x = x+1
    kinizsitable = Table(kinizsi,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Kossuth":
              kossuth.append((x,dolgozo[1],"Kossuth Lajos utca",dolgozo[3]))
              x = x+1
    kossuthtable = Table(kossuth,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Kölcsey":
              kolcsey.append((x,dolgozo[1],"Kölcsey Ferenc utca",dolgozo[3]))
              x = x+1
    kolcseytable = Table(kolcsey,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Legelő-köz":
              legelo.append((x,dolgozo[1],"Legelő-köz",dolgozo[3]))
              x = x+1
    legelotable = Table(legelo,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Lehel":
              lehel.append((x,dolgozo[1],"Lehel utca",dolgozo[3]))
              x = x+1
    leheltable = Table(lehel,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Mátyás":
              matyas.append((x,dolgozo[1],"Mátyás utca",dolgozo[3]))
              x = x+1
    matyastable = Table(matyas,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Petőfi":
              petofi.append((x,dolgozo[1],"Petőfi Sándor utca",dolgozo[3]))
              x = x+1
    petofitable = Table(petofi,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Rákóczi":
              rakoczi.append((x,dolgozo[1],"Rákóczi Ferenc utca",dolgozo[3]))
              x = x+1
    rakoczitable = Table(rakoczi,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Rózsa":
              rozsa.append((x,dolgozo[1],"Rózsa Ferenc utca",dolgozo[3]))
              x = x+1
    rozsatable = Table(rozsa,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Szabadság":
              szabadsag.append((x,dolgozo[1],"Szabadság utca",dolgozo[3]))
              x = x+1
    szabadsagtable = Table(szabadsag,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Széchenyi":
              szechenyi.append((x,dolgozo[1],"Széchenyi utca",dolgozo[3]))
              x = x+1
    szechenyitable = Table(szechenyi,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Táncsics":
              tancsics.append((x,dolgozo[1],"Táncsics utca",dolgozo[3]))
              x = x+1
    tancsicstable = Table(tancsics,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Temető":
              temeto.append((x,dolgozo[1],"Temető utca",dolgozo[3]))
              x = x+1
    temetotable = Table(temeto,colWidths=(None, None, None, None, alairas*mm))

    for dolgozo in tuzeloData:
         if dolgozo[2] == "Zrínyi":
              zrinyi.append((x,dolgozo[1],"Zrínyi utca",dolgozo[3]))
              x = x+1
    zrinyitable = Table(zrinyi,colWidths=(None, None, None, None, alairas*mm))

    registerFont(TTFont('Verdana', 'Verdana.ttf'))
    style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('BACKGROUND', (0, 1), (-1, -1), colors.white),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('FONTNAME', (0, 0), (-1, -1), 'Verdana'),
    ])

    # Apply the style to the table
    arpadtable.setStyle(style)
    adytable.setStyle(style)
    aranytable.setStyle(style)
    batthyanytable.setStyle(style)
    bercsenyitable.setStyle(style)
    beketable.setStyle(style)
    damjanichtable.setStyle(style)
    dobotable.setStyle(style)
    dozsatable.setStyle(style)
    jokaitable.setStyle(style)
    jozseftable.setStyle(style)
    kinizsitable.setStyle(style)
    kossuthtable.setStyle(style)
    kolcseytable.setStyle(style)
    legelotable.setStyle(style)
    leheltable.setStyle(style)
    matyastable.setStyle(style)
    petofitable.setStyle(style)
    rakoczitable.setStyle(style)
    rozsatable.setStyle(style)
    szabadsagtable.setStyle(style)
    szechenyitable.setStyle(style)
    tancsicstable.setStyle(style)
    temetotable.setStyle(style)
    zrinyitable.setStyle(style)
    content = [
         adytable,
         PageBreak(),
         aranytable,
         PageBreak(),
         arpadtable,
         PageBreak(),
         batthyanytable,
         PageBreak(),
         beketable,
         PageBreak(),
         bercsenyitable,
         PageBreak(),
         damjanichtable,
         PageBreak(),
         dobotable,
         PageBreak(),
         dozsatable,
         PageBreak(),
         jokaitable,
         PageBreak(),
         jozseftable,
         PageBreak(),
         kinizsitable,
         PageBreak(),
         kossuthtable,
         PageBreak(),
         kolcseytable,
         PageBreak(),
         legelotable,
         PageBreak(),
         leheltable,
         PageBreak(),
         matyastable,
         PageBreak(),
         petofitable,
         PageBreak(),
         rakoczitable,
         PageBreak(),
         rozsatable,
         PageBreak(),
         szabadsagtable,
         PageBreak(),
         szechenyitable,
         PageBreak(),
         tancsicstable,
         PageBreak(),
         temetotable,
         PageBreak(),
         zrinyitable
         ]
    document.build(content)
    
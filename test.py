from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import *
from reportlab.platypus import *
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch,mm,cm
from reportlab.pdfbase.pdfmetrics import stringWidth,registerFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.rl_config import defaultPageSize
import datetime, calendar
from datetime import timedelta
from Components.classes import *
import locale
locale.setlocale(locale.LC_ALL,'hu_HU.UTF-8')

Gyerekek = [
    Gyerek_NETAK("Krajczár Irén","8454464301",0,"Bódi Magdolna","Miskolc",0,"1991. 06. 06"),
    Gyerek_NETAK("Krajczár Irén","8478212507",0,"Bódi Ferenc","Mezőzombor",0,"1997. 12. 06"),
    Gyerek_NETAK("Krajczár Irén","8481371939",0,"Bódi Gergő","Miskolc",0,"1998. 10. 18"),
    Gyerek_NETAK("Krajczár Irén","8436924150",0,"Bódi Irén","Miskolc",0,"1986. 08. 17"),
]

PAGE_WIDTH  = defaultPageSize[1]
PAGE_HEIGHT = defaultPageSize[0]
def draw_lines(canvas,doc):
    canvas.line(50, 480, PAGE_WIDTH-50, 480)
    canvas.line(50,480,50,50)
    canvas.line(50, 50, PAGE_WIDTH-50, 50)
    canvas.line(PAGE_WIDTH-50,480,PAGE_WIDTH-50,50)

registerFont(TTFont('TNRB', 'timesbd.ttf'))
registerFont(TTFont('TNR', 'times.ttf'))

pdf_filename = "netak.pdf"
c = canvas.Canvas(pdf_filename, pagesize=landscape(A4))

c.line(50, 480, PAGE_WIDTH-50, 480)
c.line(50,480,50,50)
c.line(50, 50, PAGE_WIDTH-50, 50)
c.line(PAGE_WIDTH-50,480,PAGE_WIDTH-50,50)

header1_txt = "Adóelőleg-nyilatkozat a négy vagy több gyermeket nevelő anyák kedvezményének érvényesítéséről"
header1_txtw = stringWidth(header1_txt,fontName="TNRB",fontSize=14)
text = c.beginText((PAGE_WIDTH - header1_txtw) / 2.0, PAGE_HEIGHT-60)
text.setFont("TNRB", 14)
text.textLine(header1_txt)
c.drawText(text)
header2_txt = f"A nyilatkozat benyújtásának éve: {datetime.datetime.now().year}"
header2_txtw = stringWidth(header2_txt,fontName="TNR",fontSize=14)
text = c.beginText((PAGE_WIDTH - header2_txtw) / 2.0, PAGE_HEIGHT-75)
text.setFont("TNR", 14)
text.textLine(header2_txt)
c.drawText(text)
header3_txt = "(Kérjük, kitöltés előtt olvassa el a nyilatkozathoz tartozó tájékoztatót!)"
header3_txtw = stringWidth(header3_txt,fontName="TNRB",fontSize=14)
text = c.beginText((PAGE_WIDTH - header3_txtw) / 2.0, PAGE_HEIGHT-90)
text.setFont("TNRB", 14)
text.textLine(header3_txt)
c.drawText(text)
text = c.beginText(60,PAGE_HEIGHT-130)
text.setFont("TNR", 14)
text.textLines(f"I. A nyilatkozatot adó magánszemély\nneve: Balázs Lászlóné")
c.drawText(text)
text = c.beginText(300,PAGE_HEIGHT-147)
text.setFont("TNR", 14)
text.textLines("Adóazonosító jele: 8359484198")
c.drawText(text)
text = c.beginText(625,PAGE_HEIGHT-130)
text.setFont("TNR", 14)
text.textLines("Módosított nyilatkozat: ⎕")
c.drawText(text)
text = c.beginText(60,PAGE_HEIGHT-170)
text.setFont("TNRB", 14)
text.textLines("1. Gyermek neve")
c.drawText(text)
text = c.beginText(250,PAGE_HEIGHT-170)
text.setFont("TNRB", 14)
text.textLines("Adóazonosító jele")
c.drawText(text)
text = c.beginText(400,PAGE_HEIGHT-170)
text.setFont("TNRB", 14)
text.textLines("Születési helye, ideje")
c.drawText(text)
text = c.beginText(625,PAGE_HEIGHT-170)
text.setFont("TNRB", 14)
text.textLines("Anyja neve")
c.drawText(text)
X = 190
for gyerek in Gyerekek:
    text = c.beginText(60,PAGE_HEIGHT-X)
    text.setFont("TNR", 14)
    text.textLines(gyerek.nev)
    c.drawText(text)
    text = c.beginText(250,PAGE_HEIGHT-X)
    text.setFont("TNR", 14)
    text.textLines(gyerek.ado)
    c.drawText(text)
    text = c.beginText(400,PAGE_HEIGHT-X)
    text.setFont("TNR", 14)
    text.textLines(f"{gyerek.sz_hely}, {gyerek.sz_ido}")
    c.drawText(text)
    text = c.beginText(625,PAGE_HEIGHT-X)
    text.setFont("TNR", 14)
    text.textLines(gyerek.a_nev)
    c.drawText(text)
    c.line(60,PAGE_HEIGHT-(X+5),785,PAGE_HEIGHT-(X+5))
    X +=25
text = c.beginText(60,PAGE_HEIGHT-(X+10))
text.setFont("TNR", 14)
text.textLines("⎕ Jelölje itt x-szel, ha a gyermekek felsorolását külön lapon folytatja!")
c.drawText(text)
text = c.beginText(60,PAGE_HEIGHT-(X+35))
text.setFont("TNR", 14)
text.textLines("2. Nyilatkozom, hogy jogosult vagyok a négy vagy több gyermeket nevelő anyák kedvezményére, azt igénybe kívánom venni. ⎕")
c.drawText(text)
text = c.beginText(773.75,PAGE_HEIGHT-(X+34))
text.setFont("TNR", 14)
text.textLines("x")
c.drawText(text)
text = c.beginText(60,PAGE_HEIGHT-(X+60))
text.setFont("TNR", 14)
text.textLines("3. Nyilatkozatomat visszavonásig kérem figyelembe venni (folytatólagos nyilatkozatot teszek) ⎕.")
c.drawText(text)
text = c.beginText(594.75,PAGE_HEIGHT-(X+59))
text.setFont("TNR", 14)
text.textLines("x")
c.drawText(text)
text = c.beginText(60,PAGE_HEIGHT-(X+85))
text.setFont("TNR", 11)
text.textLines("4. Nyilatkozom, hogy a négy vagy több gyermeket nevelő anyák kedvezményét ⎕⎕ hónaptól kezdődően nem (erre a hónapra sem) kívánom igénybe venni.")
c.drawText(text)
text = c.beginText(60,PAGE_HEIGHT-(X+120))
text.setFont("TNR", 14)
now = datetime.datetime.now()
text.textLines(f"Kelt: {now.strftime("%Y.%m.%d")}")
c.drawText(text)
text = c.beginText(200,PAGE_HEIGHT-(X+120))
text.setFont("TNR", 11)
text.textLines("A nyilatkozatot tevő magánszemély aláírása:")
c.drawText(text)
c.line(400,PAGE_HEIGHT-(X+120),PAGE_WIDTH-150,PAGE_HEIGHT-(X+120))
c.line(50,160,PAGE_WIDTH-50,160)
text = c.beginText(60,60)
text.setFont("TNR", 14)
text.textLines(f"Kelt: {now.strftime("%Y.%m.%d")}")
c.drawText(text)
text = c.beginText(320,60)
text.setFont("TNR", 11)
text.textLines("cégszerű aláírás:")
c.drawText(text)
c.line(400,60,PAGE_WIDTH-150,60)
text = c.beginText(60,100)
text.setFont("TNR", 11)
text.textLines("A nyilatkozat tartalmát tudomásul vettem. A magánszemély adóelőlegét az I. Blokkban szereplő nyilatkozat figyelembevételével állapítom meg.")
c.drawText(text)
text = c.beginText(60,120)
text.setFont("TNR", 14)
text.textLines("A munkáltató, kifizető megnevezése:")
c.drawText(text)
text = c.beginText(300,120)
text.setFont("TNRB", 14)
text.textLines("Mezőzombor Község Önkormányzata adószáma: 15726353-2-05")
c.drawText(text)
text = c.beginText(60,140)
text.setFont("TNR", 14)
text.textLines("II. Az I. Blokkban szereplő magánszemély munkáltatója/kifizetője")
c.drawText(text)

c.save()
print(f"PDF created: {pdf_filename}")
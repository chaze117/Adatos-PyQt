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

def cellWidth(col):
    match col:
            case 0: return int(200)
            case 1: return int(200)
            case 2: return int(80)
            case 3: return int(80)
            case 4: return int(100)
            case 5: return int(20)
            case 6: return int(20)
            case 7: return int(100)
            case _: return int(100)

registerFont(TTFont('TNRB', 'timesbd.ttf'))
registerFont(TTFont('TNR', 'times.ttf'))

pdf_filename = "csjk.pdf"
c = canvas.Canvas(pdf_filename, pagesize=landscape(A4))
c.setLineWidth(1.5)
header1_txt = "Adóelőleg-nyilatkozat a családi kedvezmény és járulékkedvezmény érvényesítéséről"
header1_txtw = stringWidth(header1_txt,fontName="TNRB",fontSize=14)
text = c.beginText((PAGE_WIDTH - header1_txtw) / 2.0, PAGE_HEIGHT-30)
text.setFont("TNRB", 14)
text.textLine(header1_txt)
c.drawText(text)
header2_txt = f"A nyilatkozat benyújtásának éve: {datetime.datetime.now().year}"
header2_txtw = stringWidth(header2_txt,fontName="TNR",fontSize=14)
text = c.beginText((PAGE_WIDTH - header2_txtw) / 2.0, PAGE_HEIGHT-45)
text.setFont("TNR", 14)
text.textLine(header2_txt)
c.drawText(text)
header3_txt = "(Kérjük, kitöltés előtt olvassa el a nyilatkozathoz tartozó tájékoztatót!)"
header3_txtw = stringWidth(header3_txt,fontName="TNRB",fontSize=14)
text = c.beginText((PAGE_WIDTH - header3_txtw) / 2.0, PAGE_HEIGHT-60)
text.setFont("TNRB", 14)
text.textLine(header3_txt)
c.drawText(text)
c.line(25,PAGE_HEIGHT-65,PAGE_WIDTH-25,PAGE_HEIGHT-65)
text = c.beginText(25,PAGE_HEIGHT-80)
text.setFont("TNR", 13)
text.textLines(f"A nyilatkozó magánszemély\nneve: Balázs Lászlóné")
c.drawText(text)
text = c.beginText(300,PAGE_HEIGHT-97)
text.setFont("TNR", 13)
text.textLines("Adóazonosító jele: 8359484198")
c.drawText(text)
text = c.beginText(60,PAGE_HEIGHT-125)
text.setFont("TNR", 13)
text.textLines(f"1. Az eltartottak adatai:")
c.drawText(text)
text = c.beginText(600,PAGE_HEIGHT-125)
text.setFont("TNR", 13)
text.textLines(f"Módosító nyilatkozat ⎕")
c.drawText(text)

x_start = 25   # X coordinate for the start of the table
y_start = PAGE_HEIGHT-150  # Y coordinate for the start of the table
cell_width = 100  # Width of each cell
cell_heights = 20  # Height of each cell
num_rows = 4      # Number of rows
num_cols = 8      # Number of columns

data = [
    ["Név", "Adóazonosító", "TAJ szám", "Anyja neve","Cím","EM**","JJ**","Változás időpontja"],
    ["Balogh Domaaaaaaaaaaa","8526611372","130-710-666","Rontó Izabella","Kinizsi u. 13.",'1',"a",""],
    ["Balogh Dok","8526611372","130-710-666","Rontó Izabella","Kinizsi u. 13.",'1',"a",""],
    ["Balogh Dom","8526611372","130-710-666","Rontó Izabella","Kinizsi u. 13.",'1',"a",""],
]


def findLongest(col):
    longest = 0
    for row_idx, row in enumerate(data):
         current = stringWidth(data[row_idx][col],"TNR",12)
         if current > longest :
              longest = current
    return longest          
cell_widths = [findLongest(0)+20,findLongest(1)+20,findLongest(2)+20,findLongest(3)+20,findLongest(4)+20,30,30,100]
x_start = (PAGE_WIDTH-sum(cell_widths))/2

for row in range(num_rows + 1):  # +1 to draw the last horizontal line
    y = y_start - row * cell_heights
    c.line(x_start, y, x_start + sum(cell_widths), y)  # Draw horizontal lines

# Draw vertical lines with different column widths
current_x = x_start
for col_width in cell_widths:
    c.line(current_x, y_start, current_x, y_start - num_rows * cell_heights)
    current_x += col_width

# Draw the last vertical line at the end of the last column
c.line(current_x, y_start, current_x, y_start - num_rows * cell_heights)


c.setFont("TNR",12)
for row_idx, row in enumerate(data):
    current_x = x_start  # Reset x position for each row
    for col_idx, cell in enumerate(row):
        # Calculate text position within the cell
        x = current_x + 5  # Add some padding from the left
        y = y_start - row_idx * cell_heights - 15  # Adjust vertical position for text
        c.drawString(x, y, cell)
        
        # Move to the next column by adding the width of the current cell
        current_x += cell_widths[col_idx]

text = c.beginText(60,PAGE_HEIGHT-250)
text.setFont("TNR", 10)
text.setLeading(10)
text.textLines(f"""EM*- Eltartotti minőség kódjai: 1. Kedvezményezett eltartott, 2. Eltartott, 3. Felváltva gondozott gyermek, 5. Tartósan beteg, illetve súlyosan fogyatékos személy (gyermek),
               0. Kedvezménybe nem számító. Magzat esetén adatok helyett „magzat”-ot tüntessen fel!\n
               JJ**-Jogosultság jogcímei: a) Gyermek után családi pótlékra jogosult vagy ilyen jogosulttal közös háztartásban élő házastárs,
               b) Várandós nő vagy várandós nő közös háztartásban élő házastársa c) Családi pótlékra saját jogán jogosult vagy ilyen jogosulttal
               közös háztartásban élő hozzátartozó (ideértve a gyermek szüleinek hozzátartozóit is), d) Rokkantsági járadékban részesülő vagy ilyen
               személlyel közös háztartásban élő hozzátartozó.""")
c.drawText(text)
text = c.beginText(60,PAGE_HEIGHT-325)
text.setFont("TNR", 13)
text.textLines(f"2. Nyilatkozom, hogy a családi kedvezményt egyedül ⎕. Vagy jogosult házastársammal/élettársammal közösen ⎕ érvényesítem.")
c.drawText(text)
text = c.beginText(344,PAGE_HEIGHT-324)
text.setFont("TNR", 13)
text.textLines(f"x")
c.drawText(text)
text = c.beginText(60,PAGE_HEIGHT-340)
text.setFont("TNR", 13)
text.textLines(f"""3. Nyilatkozom, hogy jogosult vagyok a családi kedvezményt Magyarországon érvényesíteni, külföldi államban a jövedelmem után azonos
               vagy hasonló kedvezményt nem veszek (vettem) igénybe. ⎕""")
c.drawText(text)
text = c.beginText(366,PAGE_HEIGHT-354.5)
text.setFont("TNR", 13)
text.textLines("x")
c.drawText(text)
text = c.beginText(60,PAGE_HEIGHT-370)
text.setFont("TNR", 13)
text.textLines(f"""4. Nyilatkozom, hogy nem kérem a családi járulékkedvezmény havi összegének érvényesítését. ⎕""")
c.drawText(text)
text = c.beginText(60,PAGE_HEIGHT-385)
text.setFont("TNR", 13)
text.textLines(f"""5. A fentiek alapján nyilatkozom, hogy a családi kedvezményt (az a) vagy b) sor egyikét töltse ki!""")
c.drawText(text)
text = c.beginText(90,PAGE_HEIGHT-400)
text.setFont("TNR", 13)
text.textLines(f"""a. forint összegben kívánom igénybe venni.""")
c.drawText(text)
text = c.beginText(90,PAGE_HEIGHT-415)
text.setFont("TNR", 13)
text.textLines(f"""b. {"gyerekszám"} fő kedvezményezett eltartott után kívánom igénybe venni.""")
c.drawText(text)
text = c.beginText(60,PAGE_HEIGHT-450)
text.setFont("TNR", 13)
now = datetime.datetime.now()
text.textLines(f"Kelt: {now.strftime("%Y.%m.%d")}")
c.drawText(text)
text = c.beginText(300,PAGE_HEIGHT-450)
text.setFont("TNR", 13)
text.textLines(f"A nyilatkozatot tevő magánszemély aláírása:")
c.drawText(text)
c.line(550,PAGE_HEIGHT-450,PAGE_WIDTH-50,PAGE_HEIGHT-450)
c.line(25,PAGE_HEIGHT-455,PAGE_WIDTH-25,PAGE_HEIGHT-455)
text = c.beginText(60,PAGE_HEIGHT-470)
text.setFont("TNR", 13)
text.textLines(f"7. A családi kedvezményt kérő magánszemély jogosult házastársa/élettársa")
c.drawText(text)
text = c.beginText(60,PAGE_HEIGHT-485)
text.setFont("TNR", 13)
text.textLines(f"""Neve: adóazonosító jele:
                adóelőleget megállapító munkáltatója, kifizetője megnevezése: adószáma:""")
c.drawText(text)
c.line(25,PAGE_HEIGHT-505,PAGE_WIDTH-25,PAGE_HEIGHT-505)
text = c.beginText(60,PAGE_HEIGHT-520)
text.setFont("TNR", 13)
text.textLines(f"""A nyilatkozó magánszemély munkáltatójaként a nyilatkozat tartalmát tudomásul vettem. A magánszemély adóelőlegét a nyilatkozat
               figyelembevételével állapítom meg.
               A munkáltató, kifizető megnevezése: Mezőzombor Község Önkormányzata adószáma: 15726353-2-05
               Kelt:{now.strftime("%Y.%m.%d")}""")
c.drawText(text)
text = c.beginText(445,PAGE_HEIGHT-565)
text.setFont("TNR", 13)
text.textLines(f"Cégszerű aláírás:")
c.drawText(text)
c.line(550,PAGE_HEIGHT-565,PAGE_WIDTH-50,PAGE_HEIGHT-565)
c.save()
print(f"PDF created: {pdf_filename}")

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

data = [
    ["TP 1","2020.02.02","2020.02.02"],
    ["TP 2","2020.03.03","2020.03.03"]
]

PAGE_WIDTH  = defaultPageSize[0]
PAGE_HEIGHT = defaultPageSize[1]

registerFont(TTFont('TNRB', 'timesbd.ttf'))
registerFont(TTFont('TNR', 'times.ttf'))

pdf_filename = "tp.pdf"
c = canvas.Canvas(pdf_filename, pagesize=A4)
txt = "ÁTVÉTELI ELISMERVÉNY"
txtw = stringWidth(txt,fontName="TNRB",fontSize=24)
text = c.beginText((PAGE_WIDTH - txtw) / 2.0, PAGE_HEIGHT-100)
text.setFont("TNRB", 24)
text.textLine(txt)
c.drawText(text)
txt = "az egészségbiztosítás pénzbeli ellátásai, a baleset üzemiségének elismerése és a baleseti"
txtw = stringWidth(txt,fontName="TNRB",fontSize=12)
text = c.beginText((PAGE_WIDTH - txtw) / 2.0, PAGE_HEIGHT-120)
text.setFont("TNRB", 12)
text.textLines(txt)
c.drawText(text)
txt = "táppénz iránti kérelem elbírálásához szükséges irat(ok), igazolás(ok) átvételéről"
txtw = stringWidth(txt,fontName="TNRB",fontSize=12)
text = c.beginText((PAGE_WIDTH - txtw) / 2.0, PAGE_HEIGHT-130)
text.setFont("TNRB", 12)
text.textLines(txt)
c.drawText(text)
txt = "Alulírott Mezőzombor Község Önkormányzata részéről"
txtw = stringWidth(txt,fontName="TNR",fontSize=15)
text = c.beginText((PAGE_WIDTH - txtw) / 2.0, PAGE_HEIGHT-200)
text.setFont("TNR", 15)
text.textLines(txt)
c.drawText(text)
txt = "(munkáltató megnevezése)"
txtw = stringWidth(txt,fontName="TNR",fontSize=15)
text = c.beginText((PAGE_WIDTH - txtw) / 2.0, PAGE_HEIGHT-220)
text.setFont("TNR", 15)
text.textLines(txt)
c.drawText(text)
txt = f"igazolom, hogy {"NÉV"} -tól/től"
txtw = stringWidth(txt,fontName="TNR",fontSize=15)
text = c.beginText((PAGE_WIDTH - txtw) / 2.0, PAGE_HEIGHT-240)
text.setFont("TNR", 15)
text.textLines(txt)
c.drawText(text)
txt = "(biztosított neve)"
txtw = stringWidth(txt,fontName="TNR",fontSize=15)
text = c.beginText((PAGE_WIDTH - txtw) / 2.0, PAGE_HEIGHT-260)
text.setFont("TNR", 15)
text.textLines(txt)
c.drawText(text)
txt = f"TAJ száma: {"TAJSZ"}"
txtw = stringWidth(txt,fontName="TNR",fontSize=15)
text = c.beginText((PAGE_WIDTH - txtw) / 2.0, PAGE_HEIGHT-280)
text.setFont("TNR", 15)
text.textLines(txt)
c.drawText(text)
txt = f"Adóazonosító jele: {"ADOSZ"}"
txtw = stringWidth(txt,fontName="TNR",fontSize=15)
text = c.beginText((PAGE_WIDTH - txtw) / 2.0, PAGE_HEIGHT-300)
text.setFont("TNR", 15)
text.textLines(txt)
c.drawText(text)
txt = "az alábbiakban felsorolt nyomtatványt/nyomtatványokat a mai napon átvettem:"
txtw = stringWidth(txt,fontName="TNRB",fontSize=14)
text = c.beginText(60, PAGE_HEIGHT-330)
text.setFont("TNRB", 14)
text.textLines(txt)
c.drawText(text)

x_start = 25   # X coordinate for the start of the table
y_start = PAGE_HEIGHT-350  # Y coordinate for the start of the table
cell_width = 100  # Width of each cell
cell_heights = 20  # Height of each cell
num_rows = len(data)+1      # Number of rows
num_cols = 8   
data2 = [
        ["Megnevezés", "Kezdete", "Vége"]
    ]
for d in data:
    data2.append([d[0],d[1],d[2]])
def findLongest(col):
        longest = 0
        for row_idx, row in enumerate(data):
            current = stringWidth(data[row_idx][col],"TNR",12)
            if current > longest :
                longest = current
        return longest 
cell_widths = [findLongest(0)+20,findLongest(1)+20,findLongest(2)+20]
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
txt = "Alulírott biztosított nyilatkozom, hogy az ügyintéző nevéről és hivatali elérhatőségéről a\nszóbeli tájékoztatást megkaptam."
txtw = stringWidth(txt,fontName="TNR",fontSize=14)
text = c.beginText(60, PAGE_HEIGHT-650)
text.setFont("TNR", 14)
text.textLines(txt)
c.drawText(text)
now = str(datetime.datetime.now())
txt = f"Kelt: Mezőzombor, {now[0:10].replace('-','.')}"
txtw = stringWidth(txt,fontName="TNR",fontSize=14)
text = c.beginText(60, PAGE_HEIGHT-700)
text.setFont("TNR", 14)
text.textLines(txt)
c.drawText(text)
txt = "átadó (biztosított)"
txtw = stringWidth(txt,fontName="TNR",fontSize=12)
text = c.beginText(120, PAGE_HEIGHT-785)
text.setFont("TNR", 12)
text.textLines(txt)
c.drawText(text)
c.line(100,PAGE_HEIGHT-770,225,PAGE_HEIGHT-770)
txt = "átvevő (munkáltató)"
txtw = stringWidth(txt,fontName="TNR",fontSize=12)
text = c.beginText(PAGE_WIDTH-110-txtw, PAGE_HEIGHT-785)
text.setFont("TNR", 12)
text.textLines(txt)
c.drawText(text)
c.line(PAGE_WIDTH-100,PAGE_HEIGHT-770,PAGE_WIDTH-225,PAGE_HEIGHT-770)
txt = "P.H."
txtw = stringWidth(txt,fontName="TNR",fontSize=16)
text = c.beginText((PAGE_WIDTH - txtw) / 2.0, PAGE_HEIGHT-800)
text.setFont("TNR", 16)
text.textLines(txt)
c.drawText(text)
c.save()
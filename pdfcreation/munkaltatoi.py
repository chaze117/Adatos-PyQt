from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.rl_config import defaultPageSize
from reportlab.pdfbase.pdfmetrics import stringWidth,registerFont
from reportlab.pdfbase.ttfonts import TTFont
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF


def generateMig(values):
    PAGE_WIDTH  = defaultPageSize[0]
    PAGE_HEIGHT = defaultPageSize[1]
    c = canvas.Canvas("mig.pdf", pagesize=A4)
    registerFont(TTFont('Verdana', 'Verdana.ttf'))
    t_mig = "MUNKÁLTATÓI IGAZOLÁS"
    text_width = stringWidth(t_mig,fontName="Verdana",fontSize=20)
    text = c.beginText((PAGE_WIDTH - text_width) / 2.0, 750)
    text.setFont("Verdana", 20)
    text.textLine(t_mig)
    c.drawText(text)
    c.line(170,745,425,745)
    cimer = svg2rlg("cimer.svg")
    cimer.scale(0.4,0.4)
    renderPDF.draw(cimer, c,PAGE_WIDTH-(cimer.width*0.45),PAGE_HEIGHT-(cimer.height*0.45))
    c.setFont("Verdana", 15)
    Labels = ["Név:", "Születési Hely:", "Születési idő:", "Anyja Neve:", "Adóazonosító:", "TAJ Szám:", "Cím:", "Bruttó kereset:", "Nettó kereset:", "Jogviszony Kezdete:", "Jogviszony Vége:"]
    x = 650

    for label in Labels:
        c.drawString(50,x,label)
        c.line(50,x-5,PAGE_WIDTH-50,x-5)
        x=x-30
    x = 650
    for value in values:
        if len(value) > 35:
            c.setFont("Verdana", 10)
        else:
            c.setFont("Verdana", 15)
        c.drawString(250,x,value)
        x=x-30
    text = c.beginText(50,300)
    text.setLeading(10)
    text.textLines(
        """Ezen igazolás a közfoglalkoztatott kérésére, hivatalos felhasználás\n
        céljából került kiállításra.\n
        A munkáltató ezen munkáltatói igazolás kiállításának időpontjában\n
        nem áll sem csődeljárás, sem felszámolás alatt.\n
        Igazoljuk továbbá, hogy nevezett dolgozó jelen időpontban nem áll\n
        sem fegyelmi eljárás, sem felmondás alatt.""")
    c.drawText(text)
    ph = "PH"
    text_width = stringWidth(ph,fontName="Verdana",fontSize=20)
    text.setFont("Verdana", 20)
    text = c.beginText((PAGE_WIDTH - text_width) / 2.0, 100)
    text.textLine("PH")
    c.drawText(text)
    c.line(375,75,525,75)
    text = c.beginText(415,60)
    text.setFont("Verdana", 12)
    text.textLine("munkáltató")
    c.drawText(text)
    c.save()

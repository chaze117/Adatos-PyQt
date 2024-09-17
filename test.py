# from reportlab.lib.pagesizes import A3
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle,PageBreak, Paragraph
# from reportlab.lib.styles import ParagraphStyle
# from reportlab.lib import colors
# from reportlab.lib.units import inch,mm,cm
# from reportlab.pdfbase.pdfmetrics import stringWidth,registerFont
# from reportlab.pdfbase.ttfonts import TTFont
# import datetime, calendar
# from datetime import timedelta
# import locale
# locale.setlocale(locale.LC_ALL,'hu_HU.UTF-8')


# def calculate_easter(year):
#     # Meeus/Jones/Butcher algorithm for calculating Easter date
#     a = year % 19
#     b = year // 100
#     c = year % 100
#     d = b // 4
#     e = b % 4
#     f = (b + 8) // 25
#     g = (b - f + 1) // 3
#     h = (19 * a + b - d - g + 15) % 30
#     i = c // 4
#     k = c % 4
#     l = (32 + 2 * e + 2 * i - h - k) % 7
#     m = (a + 11 * h + 22 * l) // 451
#     month = (h + l - 7 * m + 114) // 31
#     day = ((h + l - 7 * m + 114) % 31) + 1
    
#     return datetime.datetime(year,month,day)


# def Unnep(year,month,day):
#     EaS = calculate_easter(year)
#     Pun = EaS + timedelta(days=50)
#     GFDay = EaS - timedelta(days=2)
#     EaS = EaS  + timedelta(days=1)
#     if month == 1 and day == 1 : return True 
#     if month == 3 and day == 15: return True
#     if month == 5 and day == 1: return True
#     if month == 8 and day == 20: return True
#     if month == 10 and day == 23: return True
#     if month == 11 and day == 1: return True
#     if month == 12 and day == 25: return True
#     if month == 12 and day == 26: return True
#     if month == EaS.month and day == EaS.day: return True
#     if month == Pun.month and day == Pun.day: return True
#     if month == GFDay.month and day == GFDay.day: return True

# def Megfelelo(year,month,day):
#     dayname = datetime.datetime(year,month,day).strftime("%A")
#     if dayname == "szombat" or dayname == "vasárnap" or Unnep(year,month,day): 
#         return True
#     else:
#         return False
# sYear = 2024
# sMonth = 12
# date = datetime.date(sYear,sMonth,1)
# lastday = calendar.monthrange(sYear, sMonth)[1]
# pdf_filename = "attendance_table_with_spanning.pdf"
# document = SimpleDocTemplate(pdf_filename, pagesize=A3)
# document.topMargin = 15*mm
# document.bottomMargin = 10*mm
# header_style = ParagraphStyle(
#     'header_style',
#     fontName='Helvetica-Bold',  # Set bold font
#     fontSize=16,  # Font size
#     alignment=1,  # Center alignment (0=left, 1=center, 2=right, 3=justify)
#     spaceAfter=10,
# )
# date_style = ParagraphStyle(
#     'header_style',
#     fontName='Helvetica-Bold',  # Set bold font
#     fontSize=14,  # Font size
#     alignment=2,  # Center alignment (0=left, 1=center, 2=right, 3=justify)
#     spaceAfter=5
# )
# paragraph = Paragraph("H120 1 Jelenléti",header_style)
# p2 = Paragraph(f"{date.strftime('%B')} 1. - {date.strftime('%B')} {calendar.monthrange(sYear, sMonth)[1]}.",date_style)
# content = [paragraph,p2]
# # Define the data structure for the table
# header = [
#     ['Nap', '', 'A közfoglalkoztatott személy neve', '', '', '', '', '','', '', '','', '', '','', '', '',''],  # Row 1 with column merging (spanning)
#     ['Nap', '', 'Glonczi Géza', '', '', 'Glonczi Géza', '', '','Glonczi Géza', '', '','Glonczi Géza', '', '','Glonczi Géza', '', '',''],
#     ['Nap', '', 'Óra\nPerc', 'Ledol-\ngozott\nóra', 'Aláírás', 'Óra\nPerc', 'Ledol-\ngozott\nóra', 'Aláírás','Óra\nPerc', 'Ledol-\ngozott\nóra', 'Aláírás','Óra\nPerc', 'Ledol-\ngozott\nóra', 'Aláírás','Óra\nPerc', 'Ledol-\ngozott\nóra', 'Aláírás',''],  # Row 2
# ]

# # Create a Table object
# HeaderTable = Table(header, colWidths=[2.14*cm, 1.83*cm, 1.83*cm, 0.79*cm, 1.83*cm, 1.83*cm, 0.79*cm, 1.83*cm, 1.83*cm, 
#                                    0.79*cm, 1.83*cm, 1.83*cm, 0.79*cm, 1.83*cm, 1.83*cm, 0.79*cm, 1.83*cm, 1.83*cm],
#               rowHeights=[0.2*inch,0.2*inch,0.3*inch])

# # Define the style for the table, including spanning


# HeaderStyle = TableStyle([
#     #('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background color
#     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Align text to the center
#     ('FONTNAME', (0, 0), (-1, 0), 'Verdana'),  # Font for the header row
#     ('FONTSIZE', (0, 0), (-1, 0), 10),
#     ('FONTSIZE', (1, 2), (17, 2), 5),
#     ('LEADING',(1,2),(17,2),5),# Font size for the header
#     #('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Background for the table content
#     ('GRID', (0, 0), (-1, -1), 1, colors.black),
#     ('FONTNAME',(0,1),(17,1),'Helvetica-Bold'),
#     ('SPAN', (2, 0), (16, 0)),
#     ('SPAN', (2, 1), (4, 1)),
#     ('SPAN', (5, 1), (7, 1)),
#     ('SPAN', (8, 1), (10, 1)),
#     ('SPAN', (11, 1), (13, 1)),
#     ('SPAN', (14, 1), (16, 1)),
#     ('SPAN', (0, 0), (0, 2)),
#     ('SPAN', (1, 0), (1, 2)),
#     ('SPAN', (17, 0), (17, 2)),   
# ])
# content.append(HeaderTable)

# for i in range(1,17):
#     day = [
#         [f'{i}.','Érkezés'],
#         ['','Távozás'],
#         ['Munkaközi\nszünet','Kezdete','','X','','','X','','','X','','','X','','','X','',''],
#         ['','Vége']
#     ]
#     dayStyle = TableStyle([
#     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  
#     ('FONTNAME', (0, 0), (-1, 0), 'Verdana'),  
#     ('FONTSIZE', (0, 0), (-1, 0), 10),
#     ('FONTSIZE', (0, 2), (0, 3), 7),
#     ('GRID', (0, 0), (-1, -1), 1, colors.black),
#     ('SPAN',(0,0),(0,1)),
#     ('SPAN',(0,2),(0,3)),
#     ('SPAN',(3,2),(3,3)),
#     ('FONTSIZE', (3,2),(3,3), 20),
#     ('LEADING',(3,2),(3,3),25),
#     ('SPAN',(6,2),(6,3)),
#     ('FONTSIZE', (6,2),(6,3), 20),
#     ('LEADING',(6,2),(6,3),25),
#     ('SPAN',(9,2),(9,3)),
#     ('FONTSIZE', (9,2),(9,3), 20),
#     ('LEADING',(9,2),(9,3),25),
#     ('SPAN',(12,2),(12,3)),
#     ('FONTSIZE', (12,2),(12,3), 20),
#     ('LEADING',(12,2),(12,3),25),
#     ('SPAN',(15,2),(15,3)),
#     ('FONTSIZE', (15,2),(15,3), 20),
#     ('LEADING',(15,2),(15,3),25),
#     ('SPAN',(17,0),(17,3)),
#     ('SPAN',(3,0),(3,1)),
#     ('SPAN',(6,0),(6,1)),
#     ('SPAN',(9,0),(9,1)),
#     ('SPAN',(12,0),(12,1)),
#     ('SPAN',(15,0),(15,1)),
#     ])
#     if Megfelelo(sYear,sMonth,i):
#         dayStyle.add('BACKGROUND', (0, 0), (-1, -1), colors.grey)
#     _table = Table(day, colWidths=[2.14*cm, 1.83*cm, 1.83*cm, 0.79*cm, 1.83*cm, 1.83*cm, 0.79*cm, 1.83*cm, 1.83*cm, 
#                                    0.79*cm, 1.83*cm, 1.83*cm, 0.79*cm, 1.83*cm, 1.83*cm, 0.79*cm, 1.83*cm, 1.83*cm],
#               rowHeights=[0.22*inch,0.22*inch,0.22*inch,0.22*inch])
#     _table.setStyle(dayStyle)
#     content.append(_table)
# content.append(PageBreak())
# content.append(paragraph)
# content.append(p2)
# content.append(HeaderTable)
# for i in range(17,lastday+1):
#     day = [
#         [f'{i}.','Érkezés'],
#         ['','Távozás'],
#         ['Munkaközi\nszünet','Kezdete','','X','','','X','','','X','','','X','','','X','',''],
#         ['','Vége']
#     ]
#     dayStyle = TableStyle([
#     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  
#     ('FONTNAME', (0, 0), (-1, 0), 'Verdana'),  
#     ('FONTSIZE', (0, 0), (-1, 0), 10),
#     ('FONTSIZE', (0, 2), (0, 3), 7),
#     ('GRID', (0, 0), (-1, -1), 1, colors.black),
#     ('SPAN',(0,0),(0,1)),
#     ('SPAN',(0,2),(0,3)),
#     ('SPAN',(3,2),(3,3)),
#     ('FONTSIZE', (3,2),(3,3), 20),
#     ('LEADING',(3,2),(3,3),25),
#     ('SPAN',(6,2),(6,3)),
#     ('FONTSIZE', (6,2),(6,3), 20),
#     ('LEADING',(6,2),(6,3),25),
#     ('SPAN',(9,2),(9,3)),
#     ('FONTSIZE', (9,2),(9,3), 20),
#     ('LEADING',(9,2),(9,3),25),
#     ('SPAN',(12,2),(12,3)),
#     ('FONTSIZE', (12,2),(12,3), 20),
#     ('LEADING',(12,2),(12,3),25),
#     ('SPAN',(15,2),(15,3)),
#     ('FONTSIZE', (15,2),(15,3), 20),
#     ('LEADING',(15,2),(15,3),25),
#     ('SPAN',(17,0),(17,3)),
#     ('SPAN',(3,0),(3,1)),
#     ('SPAN',(6,0),(6,1)),
#     ('SPAN',(9,0),(9,1)),
#     ('SPAN',(12,0),(12,1)),
#     ('SPAN',(15,0),(15,1)),
#     ])
#     if Megfelelo(sYear,sMonth,i):
#         dayStyle.add('BACKGROUND', (0, 0), (-1, -1), colors.grey)
#     _table = Table(day, colWidths=[2.14*cm, 1.83*cm, 1.83*cm, 0.79*cm, 1.83*cm, 1.83*cm, 0.79*cm, 1.83*cm, 1.83*cm, 
#                                    0.79*cm, 1.83*cm, 1.83*cm, 0.79*cm, 1.83*cm, 1.83*cm, 0.79*cm, 1.83*cm, 1.83*cm],
#               rowHeights=[0.22*inch,0.22*inch,0.22*inch,0.22*inch])
#     _table.setStyle(dayStyle)
#     content.append(_table)
# # Apply the style to the table
# HeaderTable.setStyle(HeaderStyle)
# # Build the PDF with the table

# document.build(content)

# print(f"PDF with table spanning columns created: {pdf_filename}")
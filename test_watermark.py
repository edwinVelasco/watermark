import pyqrcode
import hashlib
import datetime

from reportlab.graphics import renderPDF, renderPM
from svglib.svglib import svg2rlg
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

pdf = open('p.pdf', 'rb')
data = pdf.read()
pdf.close()

sha224 = hashlib.sha224(data)
sha224 =  sha224.hexdigest()

# qr = pyqrcode.create(sha224)
#
# qr.svg('uca-url.svg', scale=8)
# print(qr.terminal(quiet_zone=1))
date = datetime.datetime.now()
type_doc = 'CN'
code = '18282004'
ref = f"{date.strftime('%Y%m%d%H%M%S')}COD{code}" \
      f"{type_doc}"
metadata = f"Estudiante: {code}\nFecha: {date.strftime('%Y/%m/%d')}" \
           f"\nHash: {sha224}\nRef: {ref}\nUrl: https://www.udes.edu.co/" \
           f"{ref}/"
url = f'https://www.udes.edu.co/{ref}'

qr2 = pyqrcode.create(url)
qr2.svg('uca-url2.svg', scale=1)
qr2.png('uca-url2.png', scale=8)

# print(qr2.terminal(quiet_zone=1))


# drawing = svg2rlg('uca-url2.svg')
# renderPDF.drawToFile(drawing, 'watermark.pdf')
# renderPM.drawToFile(drawing, 'svg_demo.png', 'PNG')

my_canvas = canvas.Canvas('watermark.pdf', pagesize=letter)
drawing = svg2rlg('uca-url2.svg')
renderPDF.draw(drawing, my_canvas, 500, 70)
my_canvas.drawString(50, 60, 'La autenticidad de este documento puede ser '
                             'verificada en el registro electrónico que '
                             'se encuantra en la pagina '
                             f'http://www.udes.edu.co, bajo el código {ref}')
my_canvas.save()

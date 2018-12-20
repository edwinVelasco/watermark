import pyqrcode
import datetime
import PyPDF2

from reportlab.graphics import renderPDF, renderPM
from svglib.svglib import svg2rlg
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def createQR():
    date = datetime.datetime.now()
    type_doc = 'CN'
    code = '18282004'
    ref = f"{date.strftime('%Y%m%d%H%M%S')}COD{code}" \
          f"{type_doc}"

    url = f'https://www.udes.edu.co/{ref}'

    qr2 = pyqrcode.create(url)
    qr2.svg(f'{ref}.svg', scale=1)

    my_canvas = canvas.Canvas(f'{ref}.pdf', pagesize=letter)
    drawing = svg2rlg(f'{ref}.svg')
    renderPDF.draw(drawing, my_canvas, 500, 70)
    my_canvas.setFont("Times-Roman", 10)
    my_canvas.drawString(60, 90, 'La autenticidad de este documento puede ser '
                                 'verificada en el registro electrónico que '
                                 'se encuantra en la ')
    my_canvas.drawString(60, 80, f'pagina http://www.udes.edu.co, bajo el '
                                 f'código {ref}')
    my_canvas.save()
    return ref


def create_pdf_out(ref):
    file = open('pol.pdf', 'rb')
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)

    water = open(f'{ref}.pdf', 'rb')
    reader2 = PyPDF2.PdfFileReader(water)
    waterpage = reader2.getPage(0)
    page.mergePage(waterpage)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    for pageNum in range(1,
                         reader.numPages):  # this will give length of book
        pageObj = reader.getPage(pageNum)
        writer.addPage(pageObj)
    resultFile = open(f'{ref}_origin.pdf', 'wb')  # here we are writing so
    # 'wb' is for write binary

    writer.write(resultFile)
    file.close()
    resultFile.close()


ref = createQR()
create_pdf_out(ref)
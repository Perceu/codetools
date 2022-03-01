import io
import json
import base64

from django.http.response import JsonResponse, FileResponse
from django.shortcuts import render, HttpResponse
from django.conf import settings

from faker import Faker
from PIL import Image, ImageDraw, ImageFont
from codetools.lorem.reports.sample_pdf import SamplePdf
from codetools.lorem.reports.sample_doc import sampleDoc
from codetools.lorem.reports.sample_xlsx import sampleXls

def lorem_ipsum(request):
    fake = Faker('pt_BR')
    ipsum = []
    for i in range(2):
        ipsum.append(fake.paragraph(nb_sentences=10))

    with open(f"{settings.BASE_DIR}/codetools/lorem/json/lorem_ipsum.json") as db_json:
        links_uteis = json.loads(db_json.read())

    context = {
        "name": fake.name(),
        "job": fake.job(),
        "address": fake.address(),
        "placa": fake.license_plate(),
        "uf": fake.estado(),
        "cpf": fake.cpf(),
        "color": fake.hex_color(),
        "ipsum": ipsum,
        "links_uteis": links_uteis,
    }

    return render(request, "lorem-ipsum.html", context=context)

def lorem_pixel(request):

    width = int(request.GET.get("width", 1280))
    height = int(request.GET.get("height", 720))
    base64_response = request.GET.get("base64", False)

    color = request.GET.get("color", "#cccccc")

    img = Image.new('RGB', (width, height), color = color)
    draw = ImageDraw.Draw(img)

    font_path = f"{settings.BASE_DIR}/contrib/roboto.ttf"
    
    font = ImageFont.truetype(font_path, 30)
    font_2 = ImageFont.truetype(font_path, 18)
    
    mark = f"Codetools {settings.APP_VERSION}"
    
    draw.text((20, 20),mark,(255,255,255), font=font)
    draw.text((20, 50),"codetools.com.br",(255,255,255), font=font_2)

    output = io.BytesIO()

    img.save(output, format='PNG')

    if base64_response:
        base_image = base64.b64encode(output.getvalue()).decode()
        resposta = dict(base64_img=f"data:image/png;base64,{base_image}", filename="loren_pixel.png")
        response = JsonResponse(resposta)
    else:
        response = HttpResponse(output.getvalue(), content_type='image/png')
        response['Content-Disposition'] = 'filename="loren_pixel.png"'

    return response

def lorem_pixel_index(request):

    with open(f"{settings.BASE_DIR}/codetools/lorem/json/lorem_pixel.json") as db_json:
        links_uteis = json.loads(db_json.read())

    context = {
        "links_uteis": links_uteis,
    }
    
    return render(request, "lorem-pixel.html", context)

def lorem_docs_index(request):
    with open(f"{settings.BASE_DIR}/codetools/lorem/json/lorem_docs.json") as db_json:
        links_uteis = json.loads(db_json.read())

    context = {
        "links_uteis": links_uteis,
    }

    return render(request, "lorem-docs.html", context)

def lorem_pdf(request):
    pdf = SamplePdf('P', 'mm', 'A4')
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.ln(5)
    pdf.cell(0, 10, 'Code Tools v {}'.format(settings.APP_VERSION), 0, 1)
    pdf.cell(0, 5, 'Documento gerado como sample de PDF. ', 0, 1)
    pdf.cell(0, 5, 'Para mais informações visite:', 0, 1)
    pdf.write(5, 'codetools.com.br', 'http://codetools.com.br')
    response = HttpResponse(pdf.output(dest='S').encode('latin-1'))
    response['Content-Type'] = 'application/pdf'
    return response

def lorem_excel(request):
    doc = sampleXls()
    response = HttpResponse(doc, content_type="application/xlsx")
    response['Content-Disposition'] = 'inline; filename="sample.xlsx"'
    return response

def lorem_doc(request):
    doc = sampleDoc()
    doc_stream = doc.getvalue()
    response = HttpResponse(doc_stream, content_type="application/docx")
    response['Content-Disposition'] = 'inline; filename="sample.docx"'
    return response
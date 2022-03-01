from openpyxl import Workbook
from django.conf import settings
from tempfile import NamedTemporaryFile

def sampleXls():

    wb = Workbook()
    ws1 = wb.create_sheet("Code Tools")
    ws1['A1'] = 'Tools Verse'
    ws1['B1'] = 'Version'
    ws1['A2'] = 'Code Tools'
    ws1['B2'] = settings.APP_VERSION
    ws1['A3'] = 'Horus'
    ws1['B3'] = '-'

    file = NamedTemporaryFile()
    wb.save(file)
    file.seek(0)
    return file.read()
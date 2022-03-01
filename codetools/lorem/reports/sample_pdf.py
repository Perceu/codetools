from fpdf import FPDF
from datetime import datetime 


class SamplePdf(FPDF):

    def header(self):
        
        self.set_y(5)
        self.set_x(5)
        today = datetime.today()
        today.strftime("%d/%m/%Y")
        self.set_font('Arial', '', 10)
        self.cell(0, 0, 'Code Tools', 0, 0, 'L')
        self.set_font('Arial', '', 10)

        self.cell(0, 0, '{}'.format(today.strftime("%d/%m/%Y")), 0, 0, 'R')
        self.line(5,8,210-5,8)

    # Page footer
    def footer(self):
        self.set_y(-10)
        self.set_font('Arial', '', 8)
        self.line(5,287,210-5,287)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'R')
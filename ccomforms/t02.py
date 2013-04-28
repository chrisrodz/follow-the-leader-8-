from PyPDF2 import PdfFileReader, PdfFileWriter
import StringIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import json
import os

class t02(object):
  
  def __init__(self):
    pass
    
  def buildPDF(self, data, document_root):
    data = json.loads(data)[0]['fields']
    content = StringIO.StringIO()
    parser = canvas.Canvas(content, pagesize=letter)
    self.Transaccion(parser, data['Transaccion'])
    self.Ano_Fiscal(parser, data['Ano_Fiscal'])
    self.f1(parser, data['f1'])
    self.f2(parser, data['f2'])
    self.f3(parser, data['f3'])
    self.f5(parser, data['f5'])
    self.f6(parser, data['f6'])
    self.f8(parser, data['f8'].split('-'))
    self.f9(parser, data['f9'].split('-'))
    self.f10(parser, data['f10'])
    self.f11(parser, data['f11'])
    self.f12(parser, data['f12'])
    self.f13(parser, data['f13'])
    self.f14(parser, data['f14'])
    self.f15(parser, data['f15'])
    self.f16(parser, data['f16'])
    self.f17(parser, data['f17'])
    self.f18(parser, data['f18'])
    self.f19(parser, data['f19'])
    self.f20(parser, data['f20'])
    self.f21(parser, data['f21'])
    self.f22(parser, data['f22'])
    self.f23(parser, data['f23'])
    self.f24(parser, data['f24'])
    self.f25(parser, data['f25'])
    self.f26(parser, data['f26'])
    self.f27(parser, data['f27'])
    self.f30(parser, data['f30'])
    parser.save()
    content.seek(0)
    text = PdfFileReader(content)

    form = PdfFileReader(document_root+'/t02.pdf').getPage(0)
    output = PdfFileWriter()
    form.mergePage(text.getPage(0))
    output.addPage(form)
    
    outputStream = open(document_root+'/t02-gen.pdf', 'wb')
    output.write(outputStream)
    self.form = output
    
  def Transaccion(self, parser, Transaccion):
    parser.setFontSize(8)
    if(Transaccion == 'Nombramiento'):
      parser.drawString(462, 935, 'X')
    elif(Transaccion == 'Contrato'):
      parser.drawString(462, 925, 'X')
    elif(Transaccion == 'Renovacion'):
      parser.drawString(462, 916, 'X')
    elif(Transaccion == 'Compensacion'): #check this shit
      parser.drawString(462, 907, 'X')
    else:
      parser.drawString(462, 897, 'X')
    parser.setFontSize(12)
    
  def Ano_Fiscal(self, parser, Ano_Fiscal):
    parser.drawString(40, 842, str(Ano_Fiscal))
    
  def f1(self, parser, f1):
    parser.drawString(100, 810, f1)
    
  def f2(self, parser, f2):
    parser.drawString(510, 810, str(f2))
    
  def f3(self, parser, f3):
    parser.drawString(100, 775, f3)
    
  def f5(self, parser, f5):
    parser.drawString(520, 771, str(f5))

  def f6(self, parser, f6):
    parser.drawString(125, 750, f6)

  def f8(self, parser, f8):
    parser.drawString(180, 730, f8[2])
    parser.drawString(220, 730, f8[1])
    parser.drawString(265, 730, f8[0])
      
  def f9(self, parser, f9):
    parser.drawString(465, 730, f9[2])
    parser.drawString(505, 730, f9[1])
    parser.drawString(550, 730, f9[0])
    
  def f10(self, parser, f10):
    parser.drawString(225, 695, f10[0])
    parser.drawString(420, 695, f10[1])
    
  def f11(self, parser, f11):
    parser.drawString(225, 675, f11[0])
    parser.drawString(420, 675, f11[1])
    
  def f12(self, parser, f12):
    parser.drawString(225, 655, f12[0])
    parser.drawString(420, 655, f12[1])

  def f13(self, parser, f13):
    parser.drawString(225, 635, f13[0])
    parser.drawString(420, 635, f13[1])
    
  def f14(self, parser, f14):
    parser.drawString(225, 615, f14[0])
    parser.drawString(420, 615, f14[1])
    
  def f15(self, parser, f15):
    parser.drawString(225, 595, f15[0])
    parser.drawString(420, 595, f15[1])

  def f16(self, parser, f16):
    parser.drawString(225, 580, f16[0])
    parser.drawString(420, 580, f16[1]) 

  def f17(self, parser, f17):
    parser.drawString(225, 555, f17[0])
    parser.drawString(420, 555, f17[1])
    
  def f18(self, parser, f18):
    parser.drawString(225, 530, f18[0])
    parser.drawString(420, 530, f18[1])

  def f19(self, parser, f19):
    if (f19[0] == 1): 
      parser.drawString(375, 515, 'X') 
    else:
      parser.drawString(397, 515, 'X')  
    if (f19[1] == 1): 
      parser.drawString(545, 515, 'X') 
    else:
      parser.drawString(570, 515, 'X')    
      
  def f20(self, parser, f20):
    f20 = map(str, f20)
    parser.drawString(110, 470, f20[0])
    parser.setFontSize(8)
    parser.drawString(110, 461, f20[1])
    parser.setFontSize(12)
    parser.drawString(280, 480, f20[2])  
    parser.drawString(280, 462, f20[3]) 
    parser.drawString(520, 470, f20[4]) 
    parser.setFontSize(8) 
    parser.drawString(520, 461, f20[5])  
    
  def f21(self, parser, f21):
    parser.drawString(105, 442, f21[0])
    parser.drawString(215, 442, f21[1])
    parser.drawString(315, 450, f21[2])
    parser.drawString(147, 415, f21[3])
    parser.drawString(315, 415, f21[4])
    parser.drawString(147, 423, f21[5])
    parser.drawString(185, 423, f21[6])
    parser.drawString(228, 423, f21[7])
    parser.drawString(380, 432, f21[8])
    parser.drawString(425, 432, f21[9])
    parser.drawString(465, 432, f21[10])
    
  def f22(self, parser, f22):
    if(f22):
      parser.drawString(60, 395, 'X')
    else:
      parser.drawString(105, 395, 'X')
      
  def f23(self, parser, f23):
    if(f23[0] == 'yes'):
      parser.drawString(167, 395, 'X')
    else:
      parser.drawString(212, 395, 'X')
    parser.drawString(290, 395, f23[1])
    
  def f24(self, parser, f24):
    if(f24):
      parser.drawString(423, 395, 'X')
    else:
      parser.drawString(425, 385, 'X')

  def f25(self, parser, f25):
    if(f25):
      parser.drawString(462, 394, 'X')
    else:
      parser.drawString(502, 394, 'X')
      
  def f26(self, parser, f26):
    parser.drawString(40, 350, f26)
    
  def f27(self, parser, f27):
    parser.drawString(242, 355, f27[0])
    parser.drawString(280, 352, f27[1])
    parser.drawString(242, 330, f27[2])
    parser.drawString(280, 328, f27[3])
    
  def f30(self, parser, f30):
    parser.drawString(290, 280, f30)
         
from PyPDF2 import PdfFileReader, PdfFileWriter
import StringIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import json
import os

class a125(object):
  
  def __init__(self):
    pass
    
  def buildPDF(self, data, document_root):
    data = json.loads(data)[0]['fields']
    content = StringIO.StringIO()
    parser = canvas.Canvas(content, pagesize=letter)
  
    self.employee_name(parser, data['name'])
    self.social_security(parser, data['ssn'])
    self.title(parser, data['title'])
    self.base_salary(parser, data['base_salary'])
    self.period(parser, data['period'])
    self.period_year(parser, data['period_year'])
    self.effective_date(parser, data['effective_date'])
    self.multi_campus(parser, data['multi_campus'])
    self.sponsored_accounts(parser, data['sponsored_accounts'])
    self.cost_sharing(parser, data['cost_sharing'])
    self.university_funds(parser, data['university_funds'])
    self.payments_paid(parser, data['payments_paid'])
    self.comments(parser, data['comments'])
  
    parser.save()
    content.seek(0)
    text = PdfFileReader(content)
    
    form = PdfFileReader(document_root+'/a125.pdf').getPage(0)
    output = PdfFileWriter()
    form.mergePage(text.getPage(0))
    output.addPage(form)
    
    outputStream = open(document_root+'/a125-gen.pdf', 'wb')
    output.write(outputStream)
    self.form = output
  
  def employee_name(self, parser, name):
    parser.setFontSize(8)
    parser.drawString(125, 695, name)
    
  def social_security(self, parser, ssn):
    parser.drawString(375, 695, str(ssn))
    
  def title(self, parser, title):
    if title == '0':
      parser.drawString(87, 660, 'X') 
    elif title == '1':
     parser.drawString(165, 660, 'X')
    else:
      parser.drawString(255, 660, 'X') 
      
  def base_salary(self, parser, salary):
    parser.drawString(400, 658, str(salary))
      
  def period(self, parser, period):
    if period == '0':
      parser.drawString(182, 645, 'X')
    elif period == '1':
      parser.drawString(233, 645, 'X')
    else:
      parser.drawString(290, 645, 'X')
      
  def period_year(self, parser, year):
    parser.drawString(330, 645, year)
    
  def effective_date(self, parser, date):
    parser.drawString(190, 632, date)
    
  def multi_campus(self, parser, multi):
    if multi:
      parser.drawString(420, 622, 'X')
    else:
      parser.drawString(455, 622, 'X')
      
  def sponsored_accounts(self, parser, accounts):
    rows = []
    parserAccount = []
    for index, account in enumerate(accounts):
      if(index != 0 and index%5 == 0):
        rows.append(parserAccount)
        parserAccount = [account]  
      else:
        parserAccount.append(account)
    offsetY = 0
    originalX = 55
    originalY = 555
    for account in rows:
      parser.drawString(originalX, originalY + offsetY, account[0])
      parser.drawString(originalX + 70, originalY + offsetY, account[1])
      parser.drawString(originalX + 240, originalY + offsetY, account[2])
      parser.drawString(originalX + 385, originalY + offsetY, account[3])
      parser.drawString(originalX + 438, originalY + offsetY, account[4])
      offsetY -= 10

  def cost_sharing(self, parser, accounts):
    rows = []
    parserAccount = []
    for index, account in enumerate(accounts):
      if(index != 0 and index%5 == 0):
        rows.append(parserAccount)
        parserAccount = [account]  
      else:
        parserAccount.append(account)
    offsetY = 0
    originalX = 55
    originalY = 507
    for account in rows:
      parser.drawString(originalX, originalY + offsetY, account[0])
      parser.drawString(originalX + 70, originalY + offsetY, account[1])
      parser.drawString(originalX + 240, originalY + offsetY, account[2])
      parser.drawString(originalX + 385, originalY + offsetY, account[3])
      parser.drawString(originalX + 438, originalY + offsetY, account[4])
      offsetY -= 10

  def university_funds(self, parser, accounts):
    rows = []
    parserAccount = []
    for index, account in enumerate(accounts):
      if(index != 0 and index%5 == 0):
        rows.append(parserAccount)
        parserAccount = [account]  
      else:
        parserAccount.append(account)
    offsetY = 0
    originalX = 55
    originalY = 449
    for account in rows:
      parser.drawString(originalX, originalY + offsetY, account[0])
      parser.drawString(originalX + 70, originalY + offsetY, account[1])
      parser.drawString(originalX + 240, originalY + offsetY, account[2])
      parser.drawString(originalX + 385, originalY + offsetY, account[3])
      parser.drawString(originalX + 438, originalY + offsetY, account[4])
      offsetY -= 10
      
  def payments_paid(self, parser, accounts):
    rows = []
    parserAccount = []
    for index, account in enumerate(accounts):
      if(index != 0 and index%3 == 0):
        rows.append(parserAccount)
        parserAccount = [account]  
      else:
        parserAccount.append(account)
    offsetY = 0
    originalX = 55
    originalY = 366
    for account in rows:
      parser.drawString(originalX, originalY + offsetY, account[0])
      parser.drawString(originalX + 145, originalY + offsetY, account[1])
      parser.drawString(originalX + 438, originalY + offsetY, account[2])
      offsetY -= 10
      
  def comments(self, parser, comment):
    parser.drawString(55, 318, comment)
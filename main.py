from PyPDF2 import PdfReader
import re

reader = PdfReader("JANEIRO2025.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text().split('\n')

textRemove = {'SlpName', 'DocNum', 'pr_comissaovl_comissao', 'Helio', 'Cesar', 'Nogueira', 'de', 'Almeida', 'FAT', 'COM.:', 'NOTA:', '-', '20.000000%'}
linesPDF = []

for line in text:
  listLineText = line.split()
  listLineText = [_ for _ in listLineText if _ not in textRemove]
  length = len(listLineText) - 1
  
  patterns = {
    'itemProduct': r'^\d{2}\.\d{3}$',
    'date': r'^\d{1}-\d{4}$',
    'docNum': r'^\d{6}$'
  }

  indexes = {}

  for index, text in enumerate(listLineText):
    for key, expr in patterns.items():
      if key not in indexes and re.match(expr, text):
        indexes[key] = {'index':index, 'value':text}

  joinClientName = []
  joinProductName = []
  dateDoc = ''

  if indexes:
    for index, text in enumerate(listLineText):
      if index < indexes['docNum']['index']:
        joinClientName.append(text)
      elif index > indexes['itemProduct']['index'] and index < indexes['date']['index']:
        joinProductName.append(text)
      elif index == length:
        dateDoc = text
  
    clientName = ' '.join(joinClientName)
    productName = ' '.join(joinProductName)
    listLineText = listLineText[indexes['date']['index']:indexes['date']['index'] + 12] #I need the elements that are 12 positions after the date
    listLineText[0:1] = [dateDoc,clientName, indexes['itemProduct']['value'], productName, indexes['date']['value']]

  print(listLineText)


from PyPDF2 import PdfReader
import re

reader = PdfReader("JANEIRO2025.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text().split('\n')

textRemove = {'Helio', 'Cesar', 'Nogueira', 'de', 'Almeida', 'FAT', 'COM.:', 'NOTA:', '-'}
linesPDF = []

for line in text:
  listLineText = line.split()
  length = len(listLineText)
  listLineText = [_ for _ in listLineText if _ not in textRemove]
  
  itemproductExpr = r'^\d{2}\.\d{3}$'
  dateExpr = r'^\d{2}-\d{4}$'
  indexitemProduct = [index for index, _ in enumerate(listLineText) if re.match(itemproductExpr, _)]
  indexDate = [index for index, _ in enumerate(listLineText) if re.match(itemproductExpr, _)]
  print(indexitemProduct)
  
  endIndex = 0
  joinClientName = []
  joinProductName = []
  
  for index, word in enumerate(listLineText):
    #Client Name
    if word.replace(' ', '').isalpha():
      joinClientName.append(word)
      endIndex += 1
    else:
      break

    #Product Name
    
  
  clientName = ' '.join(joinClientName)
  listLineText = listLineText[endIndex:length]
  listLineText.insert(0, clientName)
  #print(listLineText)


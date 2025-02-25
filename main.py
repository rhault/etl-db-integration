from PyPDF2 import PdfReader
from datetime import datetime
import re
import csv

def extractTextPdf(pdfPath):
  reader = PdfReader(pdfPath)
  extractedText = []

  for readerPage in reader.pages:
    extractedText.append(readerPage.extract_text())

  return extractedText

def processText(textLines):
  updated = datetime.now()
  patterns = {
    'itemProduct': r'^\d{2}\.\d{3}$',
    'date': r'^\d{1}-\d{4}$',
    'docNum': r'^\d{5,6}$'
  }

  processedText = []

  for line in textLines.split('\n'):
    listLineText = line.split()[5:]
    length = len(listLineText) - 1
    indexes = {}

    for index, text in enumerate(listLineText):
      for key, expr in patterns.items():
        if key not in indexes and re.match(expr, text):
          indexes[key] = {'index':index, 'value':text}

    if indexes:
      joinClientName = []
      joinProductName = []
      dateDoc = ''

      #Join the names of products and customers
      for index, text in enumerate(listLineText):
        indexDate = indexes.get('date', {}).get('index', index)
        indexItemProduct = indexes.get('itemProduct', {})
        if index < indexes.get('docNum', {}).get('index', index):
          joinClientName.append(text)
        elif\
          index > indexItemProduct.get('index', index) and \
          index < indexDate:
            joinProductName.append(text)
        elif index == length:
          dateDoc = text
    
      clientName = ' '.join(joinClientName)
      productName = ' '.join(joinProductName)
      listLineText = listLineText[indexDate:indexDate + 12] #I need the elements that are 12 positions after the date
      listLineText[0:1] = [dateDoc,clientName, indexItemProduct.get('value', ''), productName]
      listLineText.append(updated)

    processedText.append(listLineText)
    
  return processedText

def main():
  path ='JANEIRO2025.pdf'
  extractedText = extractTextPdf(path)

  with open('header.csv', 'r') as header:
    fildnames = csv.DictReader(header).fieldnames
    
    with open('JANEIRO2025.csv', 'w', newline = '') as newFile:
      csvWrite = csv.DictWriter(newFile, fieldnames = fildnames)
      csvWrite.writeheader()

      for text in extractedText:
        processedData = processText(text)
        for data in processedData:
          if len(data) == len(fildnames):
            row = dict(zip(fildnames, data))
            csvWrite.writerow(row)

if __name__ == '__main__':
  main()

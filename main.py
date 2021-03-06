#!/usr/bin/python

import sys
import urllib2
import httplib2
import re
import json
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup
from datetime import datetime

'''
  create url
'''
def createUrl(date, managerId, portfolioType):

  dateTmp = date.split("-")

  day=int(dateTmp[2])
  month=int(dateTmp[1])
  year=dateTmp[0]

  host = "http://www.aafm.cl/estadisticas_publico/valor_cuota_diaria.php?"
  argumentUrl = 'administradora=%s&tipo=%s&dia=%s&mes=%s&anio=%s&orden=1&inversion=%%' % (managerId,portfolioType,day,month,year)
  url=host + argumentUrl
  print "fetching url: [%s]" % url

  return url

'''
  downlaod data file
'''
def downloadFile(url):
  data = []
  page = urllib2.urlopen(url)
  soup = BeautifulSoup(page)
  r = soup.find(name="table", attrs={"bordercolor":"#c0c0c0", "cellspacing": "1", "cellpadding": "0", "width": "100%", "border": "0"}).tbody.find_all('tr')
  for i in range(1, len(r)):
    row = r[i].find_all('td')
    if(len(row) == 5):
      try:
        tmp = {"name": cleanData(row[2].font.text), "price": cleanData(row[4].font.text)}
        data.append(tmp)
      except BaseException, e:
        print "Error in row number " + str(i)
  return data

'''
table bordercolor=#c0c0c0 cellspacing=1 cellpadding=0 
            width=100% border=0
'''

'''
  clean strings
'''
def cleanData(string):
  cleanString = string.strip()
  cleanString = re.sub(r'\s+', ' ', cleanString)
  return cleanString


'''
  get quote
'''
def getCuotas(date, managerId, maxType):
  data = []
  for rangeNumber in range(1, int(maxType)):
    urlFile = createUrl(date, managerId, rangeNumber)
    data += downloadFile(urlFile)

  return data


'''
store data to server
'''
def storeData(data):
  try :
    url = os.environ["FONDOSMUTUOS_ENDPOINT_SAVE"] or 'http://localhost:8080/fondosMutuos/record/save';
    headers = { 'Content-Type' : 'application/json' }
    h = httplib2.Http(".cache")
    h.add_credentials('test', 'test')
    for objBody in data:
      objBody = json.dumps(objBody)
      resp, content = h.request(url, "POST", body=objBody, headers=headers)
      if(resp.status != 200):
        print "!!ERROR!!"
      print content
  except Exception, e: print e

'''
  get info from asociacion de fondos mutuos
'''
def getInfo(dataFM, date, maxType):
  for managerId, fmNames in dataFM.items():
    rawData = getCuotas(date, managerId, maxType)
    return findFM(rawData, fmNames, date)

'''
  load fm data from xml
'''
def loadFMInfo():
  tree = ET.parse('fm_names.xml')
  root = tree.getroot()
  result = {}

  for fmManager in root.findall('fm_manager'):
    fmData = []
    managerId = fmManager.attrib['id']
    for fmName in fmManager.findall('fm_name'):
      fmData.append(fmName.text)
    result[managerId] = fmData

  return result


'''

'''
def findFM(data, fmNames, dateObtain):
  dateCreate = datetime.now().strftime('%Y-%m-%d')
  result = []
  print "** Searching for"
  print fmNames
  for name in fmNames:
    for row in data:
      if re.match(row['name'],name):
        row['name'] = name
        row['price'] = row['price'].replace('.','')
        row['price'] = float(row['price'].replace(',','.'))
        row['priceDate'] = dateCreate
#        row['obtain'] = dateObtain 
        result.append(row)

  return result


if __name__ == '__main__':
  date = sys.argv[1]
  maxType = 10
  dataFM = loadFMInfo()
  dataParsed = getInfo(dataFM, date, maxType)
  if len(dataParsed) > 0:
    storeData(dataParsed)
  else:
    print "Nothing to save"


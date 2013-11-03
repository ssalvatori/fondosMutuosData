#!/usr/bin/python

import sys
import urllib
import urllib2
import re
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
#from array import *

'''
  create url
'''
def createUrl(date, managerId, portfolioType):

  dateTmp = date.split("-")

  day=dateTmp[2]
  month=dateTmp[1]
  year=dateTmp[0]

  host = "http://www.aafm.cl/estadisticas_publico/valor_cuota_diaria.php?"

  argumentUrl = 'administradora=%s&tipo=%s&dia=%s&mes=%s&anio=%s&orden=1&inversion=%%' % (managerId,portfolioType,day,month,year)

  '''
  administradora=&tipo=4&dia=24&dia2=&mes=10&mes2=&anio=2013&anio2=&orden=1&inversion=%

  '''

  url=host + argumentUrl


  print "fetching url: "
  print url

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

  print "getting " + str(len(data))
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
  for rangeNumber in range(int(maxType)):
    urlFile = createUrl(date, managerId, rangeNumber)
    data += downloadFile(urlFile)

  print "total "+ str(len(data))
  return data

def storeData(data):
  return 1

def getInfo(dataFM, date, maxType):
  for managerId, fmNames in dataFM.items():

    rawData = getCuotas(date, managerId, maxType)
    print fmNames
    print findFM(rawData, fmNames)

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

def findFM(data, fmNames):
  result = []
  print data
  for name in fmNames:
    for row in data:
      #print "searching "+ name + " in " + row['name']
      regex = re.compile(r'%s'%row['name'])
      if regex.match(name):
        result.append(row)

  return result
   
#regex    <!--<fm_name>GESTION FLEXIBLE SERIE CLASICA</fm_name>-->    
if __name__ == '__main__':
  date = sys.argv[1]
  maxType = 10
  dataFM = loadFMInfo()
  getInfo(dataFM, date, maxType)
  #data = getCuotas(date,managerId, maxType)
  #print data[3]
  #print findFM(data, nameFM)


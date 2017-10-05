import os
import csv
from bs4 import BeautifulSoup as bs

#creates an array with title and call number for each finding aid
titleCallNoArray = []
for file in os.listdir('H:/Library/ArchivesSpace/cpparchives.org_MARCXML'):
	xmlTemp = open(('H:/Library/ArchivesSpace/cpparchives.org_MARCXML/' + file), 'r', encoding='utf8')
	xmlString = xmlTemp.read()
	xmlTemp.close()
    
	soup = bs(xmlString, 'lxml')
	findTitle = soup.find('datafield', ind1='1', ind2='0', tag='245')
	soup = bs(str(findTitle), 'lxml')
	findTitle = soup.find('subfield', code='a')
    
	soup = bs(xmlString, 'lxml')
	findCallNo = soup.find('datafield', tag='099')
	soup = bs(str(findCallNo), 'lxml')
	findCallNo = soup.find('subfield', code='a')

	callNo = str(findCallNo)[19:-11]
	title = str(findTitle)[19:-11]
	titleCallNoArray.append([title,callNo])
	
	#writes title and call number array to CSV
	with open('C:/Users/tdahn/Desktop/FindingAidTitleCallNo.csv', 'w', newline='', encoding='utf8') as f:
		writer = csv.writer(f)
		for row in titleCallNoArray:
			writer.writerow(row)
	f.close()

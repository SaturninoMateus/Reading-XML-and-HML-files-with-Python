#!/usr/bin/python
#Nome: Saturnino Mateus.
import csv
import urllib
import re
#:::::::::::::::::5 STEPS:::::::::::::::::#

#1- Open and read html/xml.
print 'Reading XML'
xml = urllib.urlopen('http://www.formula1.com/rss/news/latest.rss').read()
print 'Grabing the Titles'
xmlTitle = re.compile('<title>(.*)</title>')
print 'Grabing the links'
xmlLink = re.compile('<link>(.*)</link>')
#3- Store the data.
print 'Finding all titles'
findTitle = re.findall(xmlTitle,xml)
print 'Finding all links'
findLink = re.findall(xmlLink,xml)
#4- Open the CSV File
print 'Creating CSV file'
writer = csv.writer(open('arquivo.csv','wb'))
head = ('Title', 'URL')
writer.writerow(head)
#5- Write the results to the CSV file.
print 'Saving to the CSV file'
for i in range(0, len(findTitle)):
	writer.writerow([findTitle[i], findLink[i]])

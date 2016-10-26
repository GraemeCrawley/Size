from lxml import html
from bs4 import BeautifulSoup
import requests
import urllib2
import json

site = "https://www.americanapparel.net/sizing/default.asp?chart=womens.shirts"

hdr = {'User-Agent': 'giMozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = urllib2.Request(site, headers=hdr)


try:
    page = urllib2.urlopen(req)
except urllib2.HTTPError, e:
    print e.fp.read()

content = page.read()

soup = BeautifulSoup(content, 'html.parser')

table1 = soup('td', {'style': 'padding-top:7px'})

table2 = table1[0].find_all('td')

data =[]
prefix = ""
p = 0
trying = [[]]
i = 0
j = 0
p = 0
for row in table1[0].find_all('tr'):
    if p == 0:
        p = 1
        continue
    item = {"title": row.find_all('td')[0].b.string}
    for col in row.find_all('td'):
        try:
            if col.b.string != None:
                #item[table1[0].find_all('tr')[0].find_all('td')[i].b.string] = col.b.string
                #print col.b.string
                #print j, " ", i
                i = i + 1
                continue
        except AttributeError, e:
            pass
        try:
            if col.div.string != None:
                #print "hello"
                #print table1[0].find_all('tr')[0].find_all('td')[i].b.string

                if("-" in col.div.string):
                    values = col.div.string.split('-')
                    average = int(values[0])+1
                    print average
                else:
                    average = col.div.string
                item[average] = table1[0].find_all('tr')[0].find_all('td')[i].b.string
                #print "hello"
                #item[col.div.string] = col.div.string
                #print col.div.string
                #print j, " ", i

        except AttributeError, e:
            pass
        i = i + 1
    print item
    data.append(item)
    i = 0
    j = j + 1

jsonData = json.dumps(data)

print jsonData


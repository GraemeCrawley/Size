from lxml import html
from bs4 import BeautifulSoup
import requests
import urllib2

site = "https://www.americanapparel.net/sizing/default.asp?chart=womens.shirts"

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
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


for row in table1[0].find_all('tr'):
        for col in row.find_all('td'):
            try:
                if col.b.string != None:
                    print col.b.string
                    continue
            except AttributeError, e:
                pass
            try:
                if col.div.string != None:
                    print col.div.string
            except AttributeError, e:
                pass


import urllib2
from BeautifulSoup import BeautifulSoup

db = {}
#MAX = 503
MAX = 500
# MAX = 3
LEN = 5

site = 'https://database.fig-gymnastics.com/public/gymnasts/biography/'
auth = '/true?backUrl='

def id_to_str(t_id):
  digits_to_fill = LEN - len(str(t_id))
  id_str = str(t_id)
  for i in range(0, digits_to_fill):
    id_str = '0' + id_str
  return id_str

def store_to_db(t_id):
  url = site + id_to_str(t_id) + auth
  # print url
  response = urllib2.urlopen(url)
  # response = urllib2.urlopen('https://database.fig-gymnastics.com/public/gymnasts/biography/00503/true?backUrl=')
  html = response.read()
  soup = BeautifulSoup(html)
  # Only retrieve names
  h1 = soup.findAll('h1')
  db[t_id] = h1
# import re, string
# for elem in soup.findAll('div', {'class': 'span3 labeledInfo'}):
# print html
for i in range(2, MAX+1):
  store_to_db(i)

f = open('db', 'w')
f.write(str(db))

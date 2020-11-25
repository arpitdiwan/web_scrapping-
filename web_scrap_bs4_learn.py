import urllib.request
from bs4 import BeautifulSoup

url = input('Enter url : ')
#count = int(input('Enter the count'))

h = urllib.request.urlopen(url).read()
so = BeautifulSoup(h, 'html.parser')

tags = so('a')
for tag in tags:
    print('Retriving', tag.get('href', None))


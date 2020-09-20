cat examples/example_6_12.html

from bs4 import BeautifulSoup

with open('examples/example_6_12.html') as fo:
    soup = BeautifulSoup(fo, 'html.parser')

soup.head

soup.title

soup.find_all('li')


import html.parser
from bs4 import BeautifulSoup
import requests

url = input("Enter a website to extract the links from(Use https:// or http://) ")

r = requests.get(url)

data = r.text

soup = BeautifulSoup(data, 'html.parser')

list = ''

for link in soup.find_all('a'):
	list += link.get('href') + '\n'
	print ("Number of urls:" , len(list))

br = soup.find_all('br')
print ("Number of br:" , len (br))

p = soup.find_all('p')
print ("Number of br:" , len (p))

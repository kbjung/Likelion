from bs4 import BeautifulSoup
import requests

url = "http://www.daum.net/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

results = soup.findAll('a','link_favorsch')
i=0
for result in results:
    i = i+1
    print(i, result.get_text(),"\n")
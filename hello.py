import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.goodreads.com/quotes')
data = r.text.encode('utf8')
soup = BeautifulSoup(r.text,'html.parser')

tag = soup.find("div",class_="quotes")
sec = tag.find_all("div",class_="quote")
quotes_list = {}
for i in sec:
    quoter = i.find("div",class_="quoteText")
    author = i.find("span",class_="authorOrTitle");

    quotes_list[quoter.text] = (author.text)
print(quotes_list)

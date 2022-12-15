import requests
from bs4 import BeautifulSoup
import pandas

r = requests.get('https://books.toscrape.com/')

soup = BeautifulSoup(r.text,'html.parser')

tag = soup.find("div",class_="col-sm-8 col-md-9")
sec = soup.find("section")
books = soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
book_list = {}
for i in books:
    name = i.find("h3")
    price = i.find("p",class_="price_color");
    availability = i.find("p",class_="instock availability")
    b = str(availability.text)
    book_list[name.text] = (price.text,b.strip())
    #print(name.text," : ",price.text," : ",b.strip())
print(book_list)

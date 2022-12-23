import pandas as pd
import requests
from bs4 import BeautifulSoup
r = requests.get('https://github.com/topics' , headers={'User-Agent':"Mozilla/5.0"} )
response_code = r.status_code
h = r.content
soup = BeautifulSoup(h,'html.parser')
repo = soup.find("div",class_="col-lg-9 position-relative pr-lg-5 mb-6 mr-lg-5")

h = repo.find_all("div",class_="py-4 border-bottom d-flex flex-justify-between")
names = []
descri = []
links = []
for k in h :
   v = k.find("a",class_="no-underline flex-1 d-flex flex-column") 
   l = v.attrs["href"]
   link = "https://github.com{}".format(l)
   name = v.find("p",class_="f3 lh-condensed mb-0 mt-1 Link--primary")
   desc = v.find("p",class_="f5 color-fg-muted mb-0 mt-1")
   names.append(name.text)
   descri.append(desc.text.replace('\n'," "))
   links.append(link)
df = pd.DataFrame({'Name':names,'Desc':descri,'Link':links}) 
df.to_csv('csvfile.csv')

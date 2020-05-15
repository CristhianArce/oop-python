import requests
from bs4 import BeautifulSoup


URL =  "https://www.linio.com.co/p/combo-colchon-dublin-gris-doble-base-cama-ent-almohadas-protec-cabecer-rzgin6?qid=8da9bf8fa42bf62709c59c9082b10d6f&oid=DO007HL0S774OLCO&position=1&sku=DO007HL0S774OLCO"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0"}
page = requests.get(URL,headers= headers)
print(page.json())
soup = BeautifulSoup(page.content,'html.parser')
price = soup.findAll('div',class_ = "product-price-container option-container option-1 ")
print(price)
#print(soup.prettify())
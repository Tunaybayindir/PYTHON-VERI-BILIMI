import requests
from bs4 import BeautifulSoup
import time
import datetime

url="https://www.doviz.com"
while True: 
    
    response=requests.get(url)

    html_icerigi=response.content

    soup=BeautifulSoup(html_icerigi,"html.parser")

    kurlar=soup.find_all("span", {"class":"value"})
    kurlar_liste=[]
    saat=datetime.datetime.now()
    for i in kurlar:
        kurlar_liste.append(i.text)
   
    print("Saat: {}\nGram Altın: {}\nDOLAR: {}\nEURO: {}\nSTERLİN: {}\nBIST 100: {}\nBITCOIN: {}\nGRAM GÜMÜŞ: {}\nBRENT: {}".format(datetime.datetime.strftime(saat, '%X'),kurlar_liste[0],kurlar_liste[1],kurlar_liste[2],kurlar_liste[3],kurlar_liste[4],kurlar_liste[5],kurlar_liste[6],kurlar_liste[7],))
    time.sleep(10)
    print("-------------------------------------")
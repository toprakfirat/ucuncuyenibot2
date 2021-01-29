import requests
import urllib.parse
from bs4 import BeautifulSoup


def kelbul(): 
    kelimeler=[]

    #kelime alici ve birlestirici

    url = 'https://www.nisanyansozluk.com/?k=Toprak'
    r = requests.get(url)
    text= r.text
        #Hep buradan basliyor ve random kelime buluyor asagidan
    hdata= open("htmldata.txt","w+")
    hdata.write(r.text)

    soup = BeautifulSoup(text, "html.parser")
    alar = (soup.find_all('a'))

        #html koddan a href kodlulari ayirdik
    kelime = (soup.title.string)
    kelime = kelime.split()
    kelime = kelime[0]

        #49.a'da random kelimenin kodu var onu aldik cevirdik, htmlde kod bozuluyo urllible duzelttik
    ranlink = str(alar).split('Â« Ãnceki sayfa</a>,')[1].split('>Rastgele kelime</a>')[0].split('"')[1]

    url2 = 'https://www.nisanyansozluk.com/' + ranlink
    r = requests.get(url2)
    r.encoding = 'UTF-8'
    text= r.text


    soup = BeautifulSoup(text, "html.parser")
    title = (soup.find_all('title'))
    pisbaslik = str(title[0])
    kelime = pisbaslik.replace('<title>','').split(' - N')[0]
    kelime = kelime.capitalize()

        #bazi kelimelerin sonunda - var onu silip ek eklemek lazim (yig-, sayili olanlar var, hav2, tok1 gibi), (o)+'lular var, ufal-), yüz-2
        #dilbilgili bir ek eklemece olmasi lazim
        #once suffa attigimiz seylere baksin ve onlari silsin
    suff=["(o)+", "-1", "-2", "1", "2", "-", "4", "5", "3","+"]
    suffnum=0
        #once kac kelimelik bi isim yapiyoz ona bakalim ona gore silelim ve editleyelim

    for j in suff:
        if j in kelime:
            lenkel = len(j)
            kelime = kelime[:len(kelime) - lenkel]
        else:
            suffnum=suffnum+1

    hdata.close

    return kelime
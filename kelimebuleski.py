def kelbul():
    import requests
    import urllib.parse
    from bs4 import BeautifulSoup
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

    print(alar)
        #html koddan a href kodlulari ayirdik
    kelime = (soup.title.string)
    kelime = kelime.split()
    kelime = kelime[0]

        #49.a'da random kelimenin kodu var onu aldik cevirdik, htmlde kod bozuluyo urllible duzelttik
    rankel= alar[49]
    rankel=str(rankel)
    rankel=rankel.split('"')
    rankel=rankel[1]
    rankel=str(rankel)
    kelime = urllib.parse.unquote(rankel[3:])
    kelime =str(kelime)
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

    return str(kelime)



print(kelbul())
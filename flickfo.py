def flickfo():
    import urllib.request
    import requests
    import urllib.parse
    from bs4 import BeautifulSoup
    import random

    url = 'https://www.flickr.com/explore/interesting/7days/'
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all('span',attrs={'class':'photo_container pc_m'})

    kod=results[random.randint(1,4)]
    hreff= str(kod.find('a', attrs={'data-track':'thumb'}))
    link= hreff.split('"')
    link= link[3]
    link= 'https://www.flickr.com'+link

    r2= requests.get(link)

    soup = BeautifulSoup(r2.text, 'html.parser')
    results = soup.find_all('meta', attrs={'property':'og:image'})
    fotolink= (str(results[0]).split('"'))
    fotolink= fotolink[1]

    return(fotolink)

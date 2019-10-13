def grupkel():

    import requests
    import urllib.parse
    import random
    from bs4 import BeautifulSoup
    from kdata import kdata
    from kelimebul import kelbul

    #random zar atici
    zar = random.randint(1, 100)
    if zar>65:
        zarval=3
    elif zar>15 and zar<66:
        zarval=2
    else:
        zarval=1

    kelimeler=[]

    for i in range(zarval):
        kelimeler.append(kdata(kelbul()))

    return kelimeler

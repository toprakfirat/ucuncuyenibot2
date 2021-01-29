from translate import Translator
import urllib.request
import requests
import urllib.parse
from bs4 import BeautifulSoup
import random


url = 'https://www.fantasynamegenerators.com/album-names.php'

res = requests.get(url).text
soup = BeautifulSoup(res,'lxml')

ss=soup.select("body>div>div>div>div")

print(ss)

#quote= random.choice(wikiquote.quotes(wikiquote.random_titles(max_titles=1)[0]))
#sent= quote.split('.')[0]

#translator= Translator(to_lang="tr")
#trans = translator.translate(sent)
#cumpar = trans.split(" ")






def quotegetir():
    import wikiquote
    from googletrans import Translator
    import random


    wikii=wikiquote.random_titles(max_titles = 3)
    wikiism=str(wikii[0])
    quoteee=wikiquote.quotes(wikiism, max_quotes = 5)

    quotee=quoteee[0].replace('?','.').replace('!','.').split('.')
    quote=quotee[0]

    if ',' in quote:
        quote=quote.split(',')[1]

    elif ':' in quote:
        quote=quote.split(':')[1]

    elif ';' in quote:
        quote=quote.split(';')[1]

    quotelist=quote.split(' ')

    if len(quotelist) > 7:
        quotelist = quotelist[0:7]

    x=len(quotelist)
    z=random.randint(0,x)



    for i in range(0,z):
        if i == 0:
            y=quotelist[0]+" "
        elif i == z-1:
            y=y+quotelist[z-1]
        else:
            y=y+" "+quotelist[i]

    
    translator = Translator()
    
    translation= translator.translate(y,dest='tr').text
    
    return translation

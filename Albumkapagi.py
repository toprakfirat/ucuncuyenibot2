from flickfo import flickfo
from PIL import Image
from io import BytesIO
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps
import os
import random
import requests
from Grupadi import son
import math
from CompAvg import compute_average_image_color
from Quotegetir import quotegetir
import os

def albumkapagi():

    direct = os.path.abspath(os.path.dirname(__file__))

    succ= False

    while True:
        try:
            yazi=son()
            url= flickfo()
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            w, h = img.size
            print(h, w)
            box = (0,0,500,500)
            crimg = img.crop(box)
            
            fontlar =os.listdir(direct+"/Fontlar")
            fontismi=(fontlar[random.randint(1,len(fontlar))])
            succ = True
            
            print(fontismi)
            break
        except:
            pass

        
    ############# 

    #img =5 img.resize((50,50))  # Small optimization
    ork = compute_average_image_color(img)

    ##############
    renk=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    #renk=(ork[0]-150%255 ,random.randint(0,255),random.randint(0,255))

    draw = ImageDraw.Draw(crimg)
    #fontboy=random.randint(30,40)
    fontboy=random.randint(25,50)
    font=ImageFont.FreeTypeFont(direct+"/Fontlar/"+fontismi, fontboy)

    fs=font.getsize(yazi)

    print(fs)

    #we use this to stop font being larger than the cropped photo
    if fs[0]>500 or fs[1]>500:
        while fs[0]>500 or fs[1]>500:
            fontboy=fontboy-2
            font=ImageFont.FreeTypeFont(direct+"/Fontlar/"+fontismi, fontboy)
            fs=font.getsize(yazi)

    elif fs[0]<30 or fs[1]<30:
        while fs[0]<30 or fs[1]<30:
            fontboy=fontboy+2
            font=ImageFont.FreeTypeFont(direct+"/Fontlar/"+fontismi, fontboy)
            fs=font.getsize(yazi)

    #important part#
    ##first we pick a location for our text to appear, then we take the most common color of the picture and reverse it mod 255
    ##then we write the text using to font

    xxx=(random.randint(0,500-fs[0]))

    yyy=(random.randint(0,500-fs[1]))



    draw.text((xxx,yyy),yazi,((ork[0]-175)%255,(ork[1]-175)%255,(ork[2]-175)%255),font=font) # this will draw text with Blackcolor and 16 size
    #draw.text((xxx,yyy),yazi,renk,font=font)

    while True:
        try:
            quoo=quotegetir()
            break
        except:
            pass

    print(quoo)

    font2=ImageFont.FreeTypeFont(direct+"/Fontlar/"+fontismi, fontboy-8)
    draw.text((xxx, (yyy+(random.randint(30,120)))%500),quoo,((ork[0]-130)%255,(ork[1]-130)%255,(ork[2]-130)%255), font2)

    crimg.save('albumkapagi.jpg')
    return (yazi, quoo)

albumkapagi()

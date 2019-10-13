def kdata(x):
    sesli=["a","ı","o","u","e","i","ö","ü"]
    sert1=["a","ı"]
    sert2=["o","u"]   
    yum1=["e","i"]
    yum2=["ö", "ü"]

    fistik=['f','s','t','k','ç','ş','h','p']
    pecete=['p','ç','t','k']

    ilksesli = -1
    keldata=[x,0,0,0]

    for i in range(len(x)):
        if x[i] in sesli:
            while x[ilksesli] not in sesli:
                ilksesli += -1

    if x[ilksesli] in sert1:
        keldata[1]+=0
    elif x[ilksesli] in sert2:
        keldata[1]+=1
    elif x[ilksesli] in yum1:
        keldata[1]+=2
    elif x[ilksesli] in yum2:
        keldata[1]+=3

    if x[-1] not in sesli:
        if x[-1] in fistik:
            keldata[2] += 1
            if x[-1] in pecete:
                keldata[3] += 1
    else:
        keldata[2] -= 1
        keldata[3] -= 1
    return keldata

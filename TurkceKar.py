def TurkceKar(metin):
    liste = str.maketrans("ÇĞİÖŞÜçğıöşü", "CGIOSUcgiosu")

    metin = metin.translate(liste)
    return metin.lower()

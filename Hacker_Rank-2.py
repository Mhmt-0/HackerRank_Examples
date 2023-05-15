def kucuk_harflere_cevir(string):
    return string.lower()

def cift_sayilari_filtrele(liste):
    return list(filter(lambda x: x % 2 == 0, liste))



def karakterleri_sirala(string):
    frekanslar = {}
    for karakter in string:
        if karakter in frekanslar:
            frekanslar[karakter] += 1
        else:
            frekanslar[karakter] = 1
    sirali_karakterler = sorted(frekanslar.items(), key=lambda x: x[1], reverse=True)
    return sirali_karakterler



def farki_bul(liste):
    en_buyuk = max(liste)
    en_kucuk = min(liste)
    return en_buyuk - en_kucuk




def tekrarlanan_karakterleri_kaldir(string):
    karakterler = []
    sonuc = ""
    for karakter in string:
        if karakter not in karakterler:
            karakterler.append(karakter)
            sonuc += karakter
    return sonuc

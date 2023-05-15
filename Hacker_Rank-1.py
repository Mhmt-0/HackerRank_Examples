print("Hello, World!")

def toplam(a, b):
    return a + b

def liste_ters_cevir(liste):
    return liste[::-1]

def faktoriyel(n):
    faktoriyel = 1
    for i in range(1, n+1):
        faktoriyel *= i
    return faktoriyel



def palindrome_kontrol(string):
    ters_string = string[::-1]
    if string == ters_string:
        return True
    else:
        return False
print("""
*************************************************
*                                               *
* BEDEN KİTLE ENDEKSİ HESAPLAMA PROGRAMI        *
*                                               *
*                 Ahmet Serdar Songur           *
*************************************************




""")




while True:
    boy = float(input("boyunuzu ondalık olarak girin örnek [1.64] : "))
    kilo = float(input("kilonuzu girin : "))
    bki = kilo/boy**2
    if bki < 18.5:
        print("beden kitle indeksiniz = {} buna göre zayıfsınız :)".format(bki))
    elif bki >= 18.5 and bki <= 24.9:
        print("beden kitle indeksiniz = {} buna göre sağlıklı kilodasınız :)".format(bki))
    elif bki >= 25 and bki <= 30:
        print("beden kitle indeksiniz = {} buna göre fazla kilolusunuz :(".format(bki))
    elif bki > 30:
        print("beden kitle indeksiniz = {} buna göre şişmansınız :(".format(bki))
    else:
        print("beklenmeyen bir hata oluştu . . . ")
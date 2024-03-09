def parola_gucu(parola):
    buyuk_harf = 0
    kucuk_harf = 0
    sayi = 0
    ozel_karakter = 0

    for karakter in parola:
        if karakter.isupper():
            buyuk_harf += 1
        elif karakter.islower():
            kucuk_harf += 1
        elif karakter.isdigit():
            sayi += 1
        else:
            ozel_karakter += 1

    puan = buyuk_harf + kucuk_harf + sayi + ozel_karakter

    if len(parola) >= 8 and buyuk_harf > 0 and kucuk_harf > 0 and sayi > 0 and ozel_karakter > 0:
        print("Güçlü parola.")
    elif len(parola) >= 6 and puan >= 3:
        print("Orta seviye.")
    else:
        print("Zayıf parola.")

parola = input("parola gir : ")
parola_gucu(parola)

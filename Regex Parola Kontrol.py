import re
"""
[a-z]   --> Küçük harf varmı. 
[A-Z]   --> Büyük harf varmı. 
\d      --> 0-9 arasında rakam Rakam varmı.
[!%*@#] --> şifrede Özel karakter varmı.
{6,14}  --> Şifre 6-14 aralığındamı.
[^\s]   --> şifrede hiç boşluk varmı.
^\s     --> şifre başında boşluk varmı(ikisi farklı)
"""

def sifre_kontrol(sifre):
    Kontrol_et = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!%*@#])[^\s]{6,14}$'

    if re.search(Kontrol_et, sifre):
        print("Şifre gerekli tüm standartları karşılıyor:", sifre)
    else:
        print("Şifre gerekli standartları karşılamıyor!:", sifre)


sifre_kontrol("Password123@")
sifre_kontrol("Password 123@")
sifre_kontrol("password123")

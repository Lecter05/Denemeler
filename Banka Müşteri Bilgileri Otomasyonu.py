
class Hesap:
    def __init__(self, ad, bakiye=0):
        self._ad = ad
        self._bakiye = bakiye

    def para_yatir(self, miktar):
        pass

    def para_cek(self, miktar):
        pass

    def bakiye_getir(self):
        return self._bakiye


class Musteri(Hesap):
    def __init__(self, ad, adres, hesap_no, kimlik_no, bakiye=0):
        super().__init__(ad, bakiye)
        self.adres = adres
        self.hesap_no = hesap_no
        self.kimlik_no = kimlik_no

    def para_yatir(self, miktar):  #
        self._bakiye += miktar
        return f"{miktar} TL yatırıldı. Yeni bakiye: {self._bakiye}"

    def para_cek(self, miktar):
        if miktar > self._bakiye:
            return "Yetersiz bakiye"
        self._bakiye -= miktar
        return f"{miktar} TL çekildi. Yeni bakiye: {self._bakiye}"


class BankaSistemi:
    def __init__(self):
        self.musteriler = []

    def musteri_ekle(self, ad, adres, hesap_no, kimlik_no):
        for musteri in self.musteriler:
            if musteri.hesap_no == hesap_no:
                return "Hesap zaten mevcut"
        yeni_musteri = Musteri(ad, adres, hesap_no, kimlik_no)
        self.musteriler.append(yeni_musteri)
        return "Müşteri başarıyla eklendi"

    def musteri_islem(self, hesap_no, miktar, islem_tipi):
        for musteri in self.musteriler:
            if musteri.hesap_no == hesap_no:
                if islem_tipi == 'yatir':
                    return musteri.para_yatir(miktar)
                elif islem_tipi == 'cek':
                    return musteri.para_cek(miktar)
        return "Müşteri bulunamadı"

    def musteri_sil(self, kimlik_no):
        for i, musteri in enumerate(self.musteriler):
            if musteri.kimlik_no == kimlik_no:
                self.musteriler.pop(i)
                return f"Müşteri {kimlik_no} silindi."
        return "Müşteri bulunamadı."
# [[deneme,12,3], 20, 885, [deneme2, 5 ,8]]


banka_sistemi = BankaSistemi()

# müşteri ekle
ekle = banka_sistemi.musteri_ekle("Ahmet Yılmaz", "123 Çınar Sokak", "0001", "174858")
print(ekle, "\n")

# para yatırma
yatir = banka_sistemi.musteri_islem("0001", 500, "yatir")
print(yatir)

# para çekme
cek = banka_sistemi.musteri_islem("0001", 100, "cek")
print(cek, "\n")

# müşteri ekle
ekle1 = banka_sistemi.musteri_ekle("Merve Kaya", "456 Lale Caddesi", "0002", "209286")
print(ekle1, "\n")


yatir1 = banka_sistemi.musteri_islem("0002", 1500, "yatir")
print(yatir1)
cek1 = banka_sistemi.musteri_islem("0002", 500, "cek")
print(cek1, "\n")

# müşteri sil
sil = banka_sistemi.musteri_sil("209286")
print(sil)

# silinen müşteriyle ilgili işlem yap
cekilen = banka_sistemi.musteri_islem("0002", 100, "cek")
print(cekilen)


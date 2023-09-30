# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

__instance__ = str if hasattr("", "encode") else unicode

class unicode_tr(__instance__):
    CHARMAP = {
        "to_upper": {
            u"i": u"İ",
            u"ı": u"I",
            u"ğ": u"Ğ",
            u"ü": u"Ü",
            u"ö": u"Ö",
            u"ş": u"Ş",
            u"ç": u"Ç",
            u"â": u"Â",
            u"ô": u"Ô",
            u"î": u"Î",
            u"ê": u"Ê",
            u"û": u"Û"
        },
        "to_lower": {
            u"İ" : u"i",
            u"I" : u"ı",
            u"Ğ" : u"ğ",
            u"Ü" : u"ü",
            u"Ö" : u"ö",
            u"Ş" : u"ş",
            u"Ç" : u"ç",
            u"Â" : u"â",
            u"Ô" : u"ô",
            u"Î" : u"î",
            u"Ê" : u"ê",
            u"Û" : u"û"
        }
    }

    def lower(self):
        for key, value in self.CHARMAP.get("to_lower").items():
            self = self.replace(key, value)

        return unicode_tr(getattr(__instance__, "lower")(self))

    def upper(self):
        for key, value in self.CHARMAP.get("to_upper").items():
            self = self.replace(key, value)

        return unicode_tr(getattr(__instance__, "upper")(self))

    def replace(self, *args, **kwargs):
        return unicode_tr(getattr(__instance__, "replace")(self, args[0], args[1]))

    def capitalize(self):
        first, rest = self[0], self[1:]
        return unicode_tr(unicode_tr(first).upper() + unicode_tr(rest).lower())

    def title(self):
        return unicode_tr(" ".join(map(lambda x: unicode_tr(x).capitalize(), self.split())).title())


from re     import sub, search, IGNORECASE
from string import punctuation

class TurkceNormalize:
    def __tarih_ayristir(self, metin:str) -> str:
        metin = unicode_tr(metin)
        if eslesen := search(r"(\d{1,2})[-.]?(\d{2})[-.]?(\d{4})", metin):
            gun, ay, yil = eslesen.groups()
            aylar = {
                "01": "Ocak", "02": "Şubat", "03": "Mart", "04": "Nisan",
                "05": "Mayıs", "06": "Haziran", "07": "Temmuz", "08": "Ağustos",
                "09": "Eylül", "10": "Ekim", "11": "Kasım", "12": "Aralık"
            }
            try:
                return f"{gun} {aylar[ay]} {yil}"
            except KeyError:
                return ""
        return ""

    def __saat_ayristir(self, metin:str) -> str:
        metin = unicode_tr(metin)
        if eslesen := search(r"(\d{1,2}):(\d{2})(?:\s?(AM|PM))?", metin, IGNORECASE):
            saat, dakika, dilim = eslesen.groups()
            if dilim:
                saat_metni = f"öğleden sonra {saat}:{dakika}" if dilim.lower() == "pm" or int(saat) >= 12 else f"öğleden önce {saat}:{dakika}"
            elif int(saat) >= 12:
                saat_metni = f"öğleden sonra {int(saat) - 12}:{dakika}"
            else:
                saat_metni = f"öğleden önce {int(saat) - 12}:{dakika}"

            metin = metin.replace(eslesen.group(), saat_metni)

        return metin

    def tarih_saat_duzelt(self, metin:str) -> str:
        metin = unicode_tr(metin)
        metin = sub(r"(\d{1,2})[-.]?(\d{2})[-.]?(\d{4})", lambda x: self.__tarih_ayristir(x.group()), metin)
        metin = self.__saat_ayristir(metin)
        return metin

    def __grup_cevir(self, sayi:int, birler:list, onlar:list) -> str:
        kelime = ""
        if sayi >= 100:
            kelime += f"{birler[sayi // 100]} yüz" if sayi // 100 != 1 else "yüz"
            sayi %= 100
        if sayi >= 10:
            kelime += f" {onlar[sayi // 10 - 1]}"
            sayi %= 10
        if sayi > 0:
            kelime += f" {birler[sayi]}"
        return kelime.strip()

    def __sayiyi_kelimeye_cevir(self, sayi:int) -> str:
        negatif_ifade = ""
        if sayi < 0:
            sayi = abs(sayi)
            negatif_ifade = "eksi "

        birler     = ["sıfır", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
        onlar      = ["on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
        basamaklar = ["", "bin", "milyon", "milyar", "trilyon", "katrilyon"]
        kelime     = ""

        if sayi == 0:
            return birler[0]

        grup = 0
        while sayi > 0:
            sayi, kalan = divmod(sayi, 1000)
            if kalan > 0:
                grup_tanimlama = self.__grup_cevir(kalan, birler, onlar)
                if grup == 1 and kalan == 1:
                    grup_tanimlama = basamaklar[grup]
                elif grup > 0:
                    grup_tanimlama += f" {basamaklar[grup]}"
                kelime = f"{grup_tanimlama} {kelime}"
            grup += 1

        return negatif_ifade + kelime.strip()

    def sayi_cevir(self, metin:str) -> str:
        metin = unicode_tr(metin)
        metin = sub(r"\b(\d+)[.,](\d+)\b", lambda x: f"{self.__sayiyi_kelimeye_cevir(int(x.group(1)))} virgül {self.__sayiyi_kelimeye_cevir(int(x.group(2)))}", metin)
        metin = sub(r"\b\d+\b", lambda x: self.__sayiyi_kelimeye_cevir(int(x.group())), metin)
        return metin

    def kucuk_harfe_cevir(self, metin:str) -> str:
        metin = unicode_tr(metin)
        return metin.lower()

    def sapkali_harf_duzelt(self, metin:str) -> str:
        metin = unicode_tr(metin)
        aksanli_harfler = str.maketrans("âôîêûÂÔÎÊÛ", "aoieuAOIEU")
        return metin.translate(aksanli_harfler)

    def turkce_karakter_duzelt(self, metin:str) -> str:
        metin = unicode_tr(metin)
        turkce_karakterler = str.maketrans("ğĞıİöÖüÜşŞçÇ", "gGiIoOuUsScC")
        return metin.translate(turkce_karakterler)

    def etkisiz_kelime_temizle(self, metin:str) -> str:
        metin = unicode_tr(metin)

        with open("Dil/etkisiz_kelimeler.txt", "r", encoding="utf-8") as dosya:
            etkisiz_kelimeler = [unicode_tr(kelime).strip() for kelime in dosya.readlines() if unicode_tr(kelime).strip()]

        return " ".join(kelime for kelime in metin.split() if kelime not in etkisiz_kelimeler)

    def noktalama_sil(self, metin:str) -> str:
        metin = unicode_tr(metin)
        metin = metin.translate(str.maketrans(punctuation, " "*len(punctuation)))
        return sub(r"[^\w\sğüşıöçĞÜŞİÖÇ]", "", metin).strip()

    def fazla_bosluk_sil(self, metin:str) -> str:
        metin = unicode_tr(metin)
        return sub(r"\s+", " ", metin).strip()


def normalize(metin:str) -> str:
    norm  = TurkceNormalize()
    metin = norm.tarih_saat_duzelt(metin)
    metin = norm.sayi_cevir(metin)
    metin = norm.kucuk_harfe_cevir(metin)
    metin = norm.sapkali_harf_duzelt(metin)
    metin = norm.turkce_karakter_duzelt(metin)
    metin = norm.etkisiz_kelime_temizle(metin)
    metin = norm.noktalama_sil(metin)
    metin = norm.fazla_bosluk_sil(metin)
    return metin.strip()


# KekikNLP: NLP Eğitimi İçin Bir Başlangıç

Bu proje, dil işleme (NLP) konusunda temel bilgisi olmayan kişilere yönelik bir eğitim aracı olarak tasarlanmıştır.

## Projenin Amacı

KekikNLP, dil işleme görevlerinde kullanılabilecek bir araçtır. Özellikle metin sınıflandırma konusunda temel bilgileri pratiğe dökmek isteyenler için ideal bir başlangıçtır.

## Projenin Yapısı

```log
├── Dil/
│   ├── etkisiz_kelimeler.txt
│   └── __init__.py
├── Veriler/
│   └── islenmemis_veri.csv
├── model_egit.py
├── model_kullan.py
└── requirements.txt
```

## Kullanılan Teknolojiler ve Kütüphaneler

Bu projede temel Python programlama dili kullanılmıştır. Ayrıca, dil işleme ve makine öğrenimi görevleri için aşağıdaki kütüphanelerden yararlanılmıştır:

- `pandas`: Veri analizi ve manipülasyonu için.
- `imbalanced-learn`: Dengesiz veri kümelerini dengelemek için.
- `scikit-learn`: Makine öğrenimi modeli eğitimi ve değerlendirmesi için.
- `joblib`: Eğitilmiş modelleri disk üzerinde saklamak için.

## Veri Seti Yapısı

Projenizde kullanılan ana veri seti `islenmemis_veri.csv` dosyasıdır. Bu dosya, metin yorumlarını ve bu yorumların etiketlerini içerir.

---

**Not:** Bu eğitimde veri seti örnek olarak sunulmuştur. Kendi verilerinizle veya ihtiyaçlarınıza göre bu yapıyı değiştirebilirsiniz. Ancak, kodların sorunsuz çalışabilmesi için sütun adlarını korumanız önerilir.

---

## Başlangıç

### Gereksinimler

```bash
pip install -Ur requirements.txt
```

### Modeli Eğitme

```bash
python model_egit.py
```

[![model_egit](https://github.com/keyiflerolsun/NLP_Yenir_Mi/blob/main/.github/Resimler/model_egit.png?raw=true)](#)

#### Akış Şeması

1. **Veri Hazırlama**
> Bu aşamada, veri seti diskten okunur ve makine öğrenimi modelinin eğitimi için uygun bir formata getirilir.

2. **Önişleme**
> Verinin kalitesini artırmak ve modelin daha iyi sonuçlar elde etmesini sağlamak için gerçekleştirilen adımlardır. Örneğin; küçük harfe dönüştürme, gereksiz kelimeleri çıkarma, noktalama işaretlerini temizleme gibi işlemler bu aşamada yapılır.

3. **Etiket Dengeleme**
> Veri setinde bazı sınıfların diğerlerine göre daha fazla örnek içermesi durumunda, bu sınıfların dengeye getirilmesi gerekmektedir. Bu, modelin bütün sınıfları eşit şekilde tanıması için önemlidir.

4. **Eğitim ve Test Kümelerinin Ayrılması**
> Veri seti, modelin eğitimi için kullanılacak bir eğitim kümesi ve modelin performansının değerlendirilmesi için kullanılacak bir test kümesine ayrılır.

5. **Sayma Vektörü (Count Vectorizer)**
> Metin verisini, her kelimenin kaç kere geçtiğini temsil eden bir vektöre dönüştürür.

6. **TF-IDF Vektörü**
> Terim Frekansı - Ters Belge Frekansı (TF-IDF) olarak bilinir. Metin içerisindeki kelimelerin ne kadar önemli olduğunu belirlemek için kullanılır.

7. **MultinomialNB (Çok Terimli Naive Bayes)**
> Metin sınıflandırma gibi görevlerde sıkça kullanılan bir istatistiksel sınıflandırma algoritmasıdır.

8. **LogisticRegression (Lojistik Regresyon)**
> Verinin ait olduğu sınıfın olasılığını tahmin etmek için kullanılan bir sınıflandırma algoritmasıdır.

9. **LinearSVC (Doğrusal Destek Vektör Makinesi)**
> Veri noktalarını iki sınıfa ayıran en iyi doğruyu (veya hiper düzlemi) bulmaya çalışan bir sınıflandırma algoritmasıdır.

10. **RandomForestClassifier (Rastgele Orman Sınıflandırıcısı)**
> Birden fazla karar ağacının kombinasyonunu kullanarak çalışan bir sınıflandırma algoritmasıdır.

### Modeli Kullanma

```bash
python model_kullan.py
```

[![model_kullan](https://github.com/keyiflerolsun/NLP_Yenir_Mi/blob/main/.github/Resimler/model_kullan.png?raw=true)](#)

## Öneriler ve Tavsiyeler

Eğer dil işleme konusunda daha derinlemesine bilgi sahibi olmak isterseniz, çeşitli online kaynaklardan ve kurslardan yararlanabilirsiniz. Ayrıca bu projeyi kendi ihtiyaçlarınıza göre özelleştirerek daha karmaşık NLP projeleri geliştirebilirsiniz.

---

## 💸 Bağış Yap

**[☕️ Kahve Ismarla](https://KekikAkademi.org/Kahve)**

## 🌐 Telif Hakkı ve Lisans

* *Copyright (C) 2023 by* [keyiflerolsun](https://github.com/keyiflerolsun) ❤️️
* [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/keyiflerolsun/NLP_Yenir_Mi/blob/master/LICENSE) *Koşullarına göre lisanslanmıştır..*

## ♻️ İletişim

*Benimle iletişime geçmek isterseniz, **Telegram**'dan mesaj göndermekten çekinmeyin;* [@keyiflerolsun](https://t.me/KekikKahve)

##

> **[@KekikAkademi](https://t.me/KekikAkademi)** *için yazılmıştır..*

# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kekik.cli                       import konsol, cikis_yap
import pandas                        as pd
import numpy                         as np
from Dil                             import normalize
from imblearn.over_sampling          import RandomOverSampler
from sklearn.model_selection         import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.base                    import BaseEstimator
from sklearn.naive_bayes             import MultinomialNB
from sklearn.linear_model            import LogisticRegression
from sklearn.svm                     import LinearSVC
from sklearn.ensemble                import RandomForestClassifier
from sklearn.metrics                 import accuracy_score
from joblib                          import dump as pkl_ver

def veri_hazirla():
    konsol.log("[blue]\[i] İşlenmemiş Veri İçe Aktarılıyor")
    veri = pd.read_csv("Veriler/islenmemis_veri.csv")
    veri = veri.sample(frac=1).reset_index(drop=True)

    girdi_sayisi = int(veri["girdi"].count())
    konsol.log(f"[blue]\[i] {girdi_sayisi:,} Girdi İşleniyor")
    veri["girdi"] = veri["girdi"].apply(normalize)

    konsol.log("[green][+] İşlenmiş Veri Kaydediliyor")
    veri.to_csv("Veriler/islenmis_veri.csv", index=False)

def egit_ve_degerlendir(model:BaseEstimator, x_egitim:np.ndarray, y_egitim:np.ndarray, x_test:np.ndarray, y_test:np.ndarray) -> None:
    konsol.log(f"[violet]\[i] {type(model).__name__} Modeli Eğitiliyor")
    model.fit(x_egitim, y_egitim)

    # dogruluk = model.score(x_test, y_test)
    # konsol.log(f"[green][+] {type(model).__name__} Doğruluk Oranı: % {dogruluk * 100:.2f}")
    konsol.log("[yellow][~] Model Tahmini Çalıştırılıyor")
    tahminler = model.predict(x_test)

    konsol.log("[yellow][~] Doğruluk Oranı Hesaplanıyor")
    dogruluk = accuracy_score(y_test, tahminler)
    konsol.log(f"[green][+] {type(model).__name__} Doğruluk Oranı: % {dogruluk * 100:.2f}")

    konsol.log(f"[turquoise2][+] {type(model).__name__} Modeli Kaydediliyor")
    pkl_ver(model, f"Modeller/{type(model).__name__}.pkl")

def model_egitimi():
    konsol.log("[blue]\[i] İşlenmiş Veri İçe Aktarılıyor")
    veri = pd.read_csv("Veriler/islenmis_veri.csv")
    konsol.log("[turquoise2]\[i] Dengeleme Öncesi Etiketlerin Dağılımı:")
    for etiket, miktar in veri["etiket"].value_counts().items():
        konsol.log(f"[dark_turquoise]\[#] {etiket} : {miktar:,}")

    konsol.log("[yellow][~] Veri Etiket Dengesi Sağlanıyor")
    veri_dengeleyici    = RandomOverSampler(random_state=42)
    girdiler, etiketler = veri_dengeleyici.fit_resample(veri[["girdi"]], veri["etiket"])
    konsol.log("[turquoise2][~] Dengeleme Sonrası Etiketlerin Dağılımı:")
    for etiket, miktar in etiketler.value_counts().items():
        konsol.log(f"[dark_turquoise]\[#] {etiket} : {miktar:,}")

    girdiler  = girdiler["girdi"].values.astype("U")
    etiketler = etiketler.values.astype("U")

    konsol.log("[yellow][~] Eğitim ve Test Kümeleri Ayrıştırılıyor")
    x_egitim, x_test, y_egitim, y_test = train_test_split(girdiler, etiketler, test_size=0.2, random_state=42)

    konsol.log("[yellow][~] Sayma Vektörleri Oluşturuluyor")
    sayma_vektoru  = CountVectorizer()
    x_egitim_sayma = sayma_vektoru.fit_transform(x_egitim)

    konsol.log("[yellow][~] TF-IDF Vektörleri Oluşturuluyor")
    tfidf_vektoru  = TfidfTransformer()
    x_egitim_tfidf = tfidf_vektoru.fit_transform(x_egitim_sayma)

    konsol.log("[green][+] Vektörleştirme Modelleri Kaydediliyor")
    pkl_ver(sayma_vektoru, "Modeller/sayma_vektoru.pkl")
    pkl_ver(tfidf_vektoru, "Modeller/tfidf_vektoru.pkl")

    konsol.log("[yellow][~] Test Verisi Dönüştürülüyor")
    x_test_sayma = sayma_vektoru.transform(x_test)
    x_test_tfidf = tfidf_vektoru.transform(x_test_sayma)

    for model in [
        MultinomialNB(),
        LogisticRegression(max_iter=1000),
        LinearSVC(dual=False),
        RandomForestClassifier(n_estimators=500, max_depth=50, n_jobs=-1)
    ]:
        egit_ve_degerlendir(model, x_egitim_tfidf, y_egitim, x_test_tfidf, y_test)



if __name__ == "__main__":
    from time  import time
    from Kekik import zaman_donustur

    print()

    basla = time()

    veri_hazirla()
    model_egitimi()

    konsol.print(f"\n[aquamarine1][⌛️] Geçen Süre : {zaman_donustur(time() - basla)}\n")
    cikis_yap(False)

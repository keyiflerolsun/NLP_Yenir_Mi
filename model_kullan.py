# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kekik.cli    import konsol, cikis_yap
from joblib       import load as pkl_al
from sklearn.base import BaseEstimator
from Dil          import normalize


modeller      = {
    model_adi: pkl_al(f"Modeller/{model_adi}.pkl")
        for model_adi in [
            "MultinomialNB",
            "LogisticRegression",
            "LinearSVC",
            "RandomForestClassifier"
        ]
}
sayma_vektoru = pkl_al("Modeller/sayma_vektoru.pkl")
tfidf_vektoru = pkl_al("Modeller/tfidf_vektoru.pkl")

def model_kullan(metin:str, model:BaseEstimator) -> str:
    print()
    konsol.log(f"[yellow][«] {metin}")
    yorum = normalize(metin)

    yorum_sayma = sayma_vektoru.transform([yorum])
    yorum_tfidf = tfidf_vektoru.transform(yorum_sayma)

    if type(model).__name__ != "LinearSVC":
        olasiliklar = model.predict_proba(yorum_tfidf)
        for etiket, olasilik in zip(model.classes_, olasiliklar[0]):
            konsol.log(f"[dark_turquoise]\[#] {etiket} : %{olasilik*100:.2f}")

    tahmin = model.predict(yorum_tfidf)
    return tahmin[0]

if __name__ == "__main__":
    from time  import time
    from Kekik import zaman_donustur

    basla = time()

    for model_adi, model in modeller.items():
        konsol.log(f"\n\n[violet]\[i] {model_adi} Modeli İle Tahminler")
        for yorum in [
            "Harika! Buradaki ürünler çok kaliteli!",
            "kim üretti bunları",
            "çok kötü, almayın, güzel diye almıştık",
            "bunları yapanın ellerini öpeyim"
        ]:
            tahmin = model_kullan(yorum, model)
            konsol.log(f"[{'green' if tahmin == 'pozitif' else 'red'}][»] {model_adi} Tahmin Sonucu : {tahmin}")

    konsol.print(f"\n[aquamarine1][⌛️] Geçen Süre : {zaman_donustur(time() - basla)}\n")
    cikis_yap(False)
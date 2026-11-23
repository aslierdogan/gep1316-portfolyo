# Kullanıcıdan adını girmesini istiyoruz ve bu bilgiyi 'ad' değişkenine kaydediyoruz.
ad = input("Adınız nedir? ")

# Kullanıcıdan doğum yılını metin olarak alıp int() ile tam sayıya çeviriyoruz.
dogum_yili = int(input("Doğum yılınız nedir? "))

# Mevcut yılı (2026) bir değişkende tutuyoruz.
mevcut_yil = 2026
# Kendi eklediğim gelecek yıl kontrolü:
if dogum_yili > mevcut_yil:
    print("doğum yılı mevcut yıldan büyük olamaz")
else:
    yas = mevcut_yil - dogum_yili
    print(f"Merhaba {ad}! {yas} yaşındasın. GEP1316 Kodlama Okuryazarlığı dünyasına hoş geldin!")

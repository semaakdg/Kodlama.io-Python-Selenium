# int : Tam sayıları ifade eder. Örneğin 34, 45, 1, gibi

# long : uzun olan tam sayıları ifade eder.  Örneğin 123963344 gibi

# float : Ondalıklı sayıları ifade eder. Örneğin 2.31, 345.3, 1.124, gibi

# str (string) : Harf, rakam, kombinasyonlardan oluşur. Örneğin 'Kodlama.io 1.ödev' gibi

# bool : sadece iki değer alabilirler; True, False.. Bu veri tipi karşılaştırma sonucu ortaya çıkan sonucun ya da bir koşulun doğru ya da yanlış olup olmadığını belirlemek içiin kullanılır. Ayrıca programlama temelinde de yeri oldukça büyüktür. 

# list : Birden çok veriyi gruplayıp bir arada tutmak istediğimizde zamanlarda kullanabileceğimiz bir veri tipidir. 
no = ["elb" , "eks"] # bu bir list örneği, çalıştırdığımızda bize "eks" yi verecek
print(no[1])
no[1] = "des" # bunu kullanarak 1.index yerine "des" i yazdırarak; dışarıdan müdahale ile list içerisinde değişiklik yaptım
print(no)

# tuple : BU da listler gibidir, farkı ise tuple'lar immutable yani değiştirilemez(gibi bir şey). Şöyle söyleyebilirim bir obje belirledik, kod satırı yazdık ama yazdığımız bu şeyin değiştirilmesini istemiyoruz, İşte o zaman tupleı kullanıyoruz.
non = ("elb","eks")# bu bir tuple örneği, çalıştırdığımızda bize "eks" yi verecek
print(non[1])
#non[1] = "des" # çalıştırdığımda error verecek

# dic (dictionaries) : Bu bir anahtar-değer çiftleri koleksiyonudur. Her anahtar (key), bir değerle (value) eşleştirilir ve bu anahtarlar benzersiz olmalıdır. Dic veri tipi, '{}' ile tanımlanır ve anahtar-değer çiftleri virgülle ayrılır.
keh = {"ab": 2, "cd": 3, "ef": 5} # örnek olarak verilebilir
for key, value in keh.items(): # bunu çalıştırarak dicteki verileri kolaylıkla çekebiliriz
    print(key, value)
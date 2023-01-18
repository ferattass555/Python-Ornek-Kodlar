#WORDLİST OLUŞTURUCU
import itertools as t #gerekli kütüphaneler
chars = input("Kurban hakkında bilgi: ") #kullanıcıdan bilgi alınması
min = int(input("Minimum karakter sayısı: ")) #kullanıcıdan bilgi alınması
max = int(input("Maximum karakter sayısı: ")) #kullanıcıdan bilgi alınması
output = input("Output Fil: ") #kullanıcıdan bilgi alınması

if output == "" or output is None: #dosya adı girilmediyse
    file = open(chars+".txt", "w") #dosya adı chars.txt olarak kaydedilir

else: #dosya adı girildiyse
    file = open(output, "w") #dosya adı output olarak kaydedilir

if min == max: #min ve max aynı ise 
    for i in range(min, max+1): #min ve max arasında döngü oluşturulur
        for a in t.product(chars, repeat=i): #chars içindeki karakterlerin tekrar sayısı i
            s = "".join(a) #s değişkenine atılır
            file.write(s+"\n") #s değişkeni dosyaya yazılır
        file.close() #dosya kapatılır

elif min < max: #min max dan küçük ise
    for i in range(min, max+1): #min ve max arasında döngü oluşturulur
        for a in t.product(chars, repeat=i): #chars içindeki karakterlerin tekrar sayısı i
            s = "".join(a) #s değişkenine atılır
            file.write(s+"\n") #s değişkeni dosyaya yazılır
        file.close() #dosya kapatılır
else: #min max dan büyük ise hata verir
    print("Maksimum tekrar, minimum tekrardan büyük olmalıdır.") #hata mesajı
    exit #programdan çıkış yapılır

if output == "" or output is None: #dosya adı girilmediyse
    print("Dosyayı adına göre kaydedildi: "+chars+".txt") #dosya adı chars.txt olarak kaydedilir 
else: #dosya adı girildiyse
    print("Wordlist oluşturuldu: "+output) #dosya adı output olarak kaydedilir



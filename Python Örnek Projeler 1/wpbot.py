#whatsapp mesaj bombalama aracı

from selenium import webdriver

driver = webdriver.Firefox() #Burda Hangi Tarayıcıyı Kullanacaksanız Onu Yazın
driver.get("https://web.whatsapp.com/") #Whatsapp Web Adresi

print("login...\n") #Konsola Login Yazısı

name = input("Göndereceğiniz kişinin adını giriniz: ") #Konsoldan Kişi Adı Alınır
count = int(input("Kaç mesaj göndermek istiyorsunuz: ")) #Konsoldan Kaç Mesaj Gönderileceği Alınır
message = input("Mesajınızı giriniz: ") #Konsoldan Mesaj Alınır

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)) #Kişi Adı Alınır
user.click() #Kişiye Tıklanır

msgBox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]') #Mesaj Kutusu Alınır

for i in range(count): #Mesaj Sayısı Kadar Döngü
    msgBox.send_keys(message) #Mesaj Kutusuna Mesaj Gönderilir
    sendButton = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button') #Gönder Butonu Alınır
    sendButton.click() #Gönder Butonuna Tıklanır
    
print("Mesajlar gönderildi.") #Konsola Mesaj Gönderildi Yazısı

driver.close() #Tarayıcı Kapatılır

#Kodun Çalışması İçin Selenium Kütüphanesini Kurmanız Gerekiyor
#Selenium Kurulumu İçin: pip install selenium
#Selenium İçin Tarayıcı Sürücüsünü İndirmeniz Gerekiyor
#Firefox İçin: driver = webdriver.Firefox()
#Chrome İçin: driver = webdriver.Chrome()
#İndirme Linkleri:
#Firefox: firefox driver
#Chrome: chrome driver


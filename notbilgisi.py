notlar = []

def anaMenu():
    global secenek
    while True:
        try:
            print("Yapmak istediğiniz İşlemi Seçiniz. (1- Not Girme, 2- Not Değiştirme, 3- Ortalama Hesaplama, 4- Çıkış)")
            secenek = int(input("Seçtiğiniz Seçeneği Giriniz : "))

            if secenek == 1:
                print("Hangi Not Bilgisini Girmek İstiyorsunuz? (1- Birinci Not Bilgisi, 2- İkinci Not Bilgisi, 3- Birinci Sözlü Not Bilgisi, 4- İkinci Sözlü Not Bilgisi, 5- Geri)")
                notSecenek = int(input("Seçeneğinizi Giriniz : "))
                if notSecenek == 1:
                    not1 = int(input("Birinci Not Bilgisini Giriniz : "))
                    notlar.insert(0, not1)
                    continue
                elif notSecenek == 2:
                    not2 = int(input("İkinci Not Bilgisini Giriniz : "))
                    notlar.insert(1, not2)
                    continue
                elif notSecenek == 3:
                    not3 = int(input("Birinci Sözlü Not Bilgisini Giriniz : "))
                    notlar.insert(2, not3)
                    continue
                elif notSecenek == 4:
                    not4 = int(input("İkinci Sözlü Not Bilgisini Giriniz : "))
                    notlar.insert(2, not3)
                    continue
                elif notSecenek == 5:
                    print("Ana Menü'ye Geri Dönülüyor...")
                    anaMenu()
                    continue
                else:
                    print("Hatalı Giriş. Lütfen Tekrardan Deneyiniz!\n")
                    continue

        except ValueError:
            print("Lütfen Sadece Rakam Giriniz!")
        break

def notDegisme():
    while True:
        try:
            if secenek == 2:
                print("Hangi Not Bilgisini Değiştirmek İstiyorsunuz? (1- Birinci Not Bilgisi, 2- İkinci Not Bilgisi, 3- Birinci Sözlü Not Bilgisi, 4- İkinci Sözlü Not Bilgisi, 5- Geri)")
                notSecenek = int(input("Seçeneğinizi Giriniz : "))
                if notSecenek == 1:
                    yNot1 = int(input("Birinci Not Bilgisini Giriniz : "))
                    notlar.pop(0) and notlar.insert(0, yNot1)
                    anaMenu()
                    continue
                elif notSecenek == 2:
                    yNot2 = int(input("İkinci Not Bilgisini Giriniz : "))
                    notlar.pop(0) and notlar.insert(1, yNot2)
                    anaMenu()
                    continue
                elif notSecenek == 3:
                    yNot3 = int(input("Birinci Sözlü Not Bilgisini Giriniz : "))
                    notlar.pop(0) and notlar.insert(2, yNot3)
                    anaMenu()
                    continue
                elif notSecenek == 4:
                    yNot4 = int(input("İkinci Sözlü Not Bilgisini Giriniz : "))
                    notlar.pop(0) and notlar.insert(3, yNot4)
                    anaMenu()
                    continue
                elif notSecenek == 5:
                    print("Ana Menü'ye Geri Dönülüyor...")
                    anaMenu()
                    continue
                else:
                    print("Hatalı Giriş. Lütfen Tekrardan Deneyiniz!")
                continue
        except ValueError:
            print("Lütfen Sadece Rakam Giriniz!")
        except IndexError:
            print("Lütfen Not Bilgisi Giriniz!")
            anaMenu()
        break

def ortalamaHesap():
    while True:
        try:
            if secenek == 3:
                print(f"Notların Ortalaması : {(notlar[0] + notlar[1] + notlar[2] + notlar[3])/4}")
                anaMenu()
            continue
        except IndexError:
            print("Lütfen Not Bilgisi Giriniz!")
            anaMenu()
        break

def cikis():
     while secenek == 4:
        print("Çıkış Yapılıyor...")
        quit()
        
anaMenu(), cikis(), notDegisme(), ortalamaHesap()
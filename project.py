class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file_name = "books.txt"
        with open(self.file_name, "r") as file:
            books = file.readlines()
            for book in books:
                book_info = book.strip().split(", ")
                print(f"Kitap Adı: {book_info[0]}, Yazar Adı: {book_info[1]}")



    def add_book(self):
        self.file_name = "books.txt"
        def kitap_bilgileri_al():
            kitap_bilgileri = {}

            def kitap_adi_tanimlama():
                while True:
                    kitap_adi = input("Lütfen bir kitap adı girin: ")
                    if kitap_adi.strip():
                        print("Kitap adı kaydedildi:", kitap_adi)
                        kitap_bilgileri["Kitap Adı"] = kitap_adi
                        break
                    else:
                        print("Lütfen boş olmayan bir metin girin.")

            def yazar_adi_tanimlama():
                while True:
                    yazar_adi = input("Lütfen yazar adı girin: ")
                    if yazar_adi.strip():
                        print("Yazar adı kaydedildi:", yazar_adi)
                        kitap_bilgileri["Yazar Adı"] = yazar_adi
                        break
                    else:
                        print("Lütfen boş olmayan bir metin girin.")

            def yayinlanma_tarihi_tanimlama():
                while True:
                    tarih = input("Lütfen yayınlanma tarihi (yıl) girin: ")
                    if tarih.isdigit():
                        tarih = int(tarih)
                        print("Yayınlanma tarihi:", tarih)
                        kitap_bilgileri["Yayınlanma Tarihi"] = tarih
                        break
                    else:
                        print("Lütfen bir sayı giriniz.")

            def sayfa_sayisi_tanimlama():
                while True:
                    sayfa_sayisi = input("Lütfen sayfa sayısı girin: ")
                    if sayfa_sayisi.isdigit():
                        sayfa_sayisi = int(sayfa_sayisi)
                        print("Sayfa sayısı:", sayfa_sayisi)
                        kitap_bilgileri["Sayfa Sayısı"] = sayfa_sayisi
                        break
                    else:
                        print("Lütfen bir sayı giriniz.")

            kitap_adi_tanimlama()
            yazar_adi_tanimlama()
            yayinlanma_tarihi_tanimlama()
            sayfa_sayisi_tanimlama()

            return kitap_bilgileri

        kitap_bilgileri = kitap_bilgileri_al()

        with open(self.file_name, "a+") as file:
            file.write(f"{kitap_bilgileri['Kitap Adı']}, {kitap_bilgileri['Yazar Adı']}, {kitap_bilgileri['Yayınlanma Tarihi']}, {kitap_bilgileri['Sayfa Sayısı']}\n")

        print("Kitap başarıyla eklendi.")




    def remove_book(self):
        title_to_remove = input("Silmek istediğiniz kitabın adını girin: ")
        found = False
    
        with open(self.file_name, "r") as file:
            lines = file.readlines()
        with open(self.file_name, "w") as file:
            for line in lines:
                book_info = line.strip().split(", ")
                if title_to_remove == book_info[0]:
                    found = True
                else:
                    file.write(line)

        if found:
            print(f"'{title_to_remove}' adlı kitap başarıyla silindi.")
        else:
            print(f"'{title_to_remove}' adlı kitap bulunamadı.")



def menu():
    lib = Library()
    while True:
        print("\n*** MENÜ ***")
        print("1) Kitapları Listele")
        print("2) Kitap Ekle")
        print("3) Kitap Sil")
        print("q) Çıkış")
        choice = input("Seçiminiz (1/2/3/q): ")

        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        elif choice == "q":
            del lib
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    menu()
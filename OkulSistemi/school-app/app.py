from baglanti import DbManager
from connection import connection
import datetime
from ogrenciler import Student
from ogretmenler import Teacher

class App:
    def __init__(self):
        self.db = DbManager(connection)

    def initApp(self):
        msg ="****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-SInıflara Göre Dersler\n7-Çıkış(E/Ç)"
        while True:
            print(msg)
            islem = input("Seçim:")
            if islem == "1":
                self.displayStudents()
            elif islem =="2":
                self.addStudent()
            elif islem == "3":
                self.editStudent()
            elif islem =="4":
                self.deleteStudent()
            elif islem == "5":
                self.addTeacher()
            elif islem == "6":
                self.sinifDersleriniListele()
            elif islem == "e" or islem == "Ç":
                break
            else:
                print("yanlış seçim yaptınız!")

    def sinifDersleriniListele(self):
        print("\n--- Sınıflara Göre Dersler ---")

        siniflar = self.db.sınıfgetir()
        for sinif in siniflar:
            print(f"{sinif.Id}: {sinif.sınıf_ismi}")

        secim = input("\nSınıf ID giriniz (tümünü listelemek için'0'): ")

        if secim == "0":
            self.tumSinifDersleriniListele()
        else:
            sinif_id = int(secim)
            self.tekSinifDersleriniListele(sinif_id)

    def tumSinifDersleriniListele(self):
        self.db.cursor.execute("SELECT SınıfId, DersId, ÖğretmenId FROM sınıf_dersleri")
        iliskiler = self.db.cursor.fetchall()

        if not iliskiler:
            print("Hiç kayıt bulunamadı!'")
            return

        print("\n Tüm sınıfların ders Listesi")
        print("{:<5} {:<15} {:<20} {:<15}".format("Sınıf", "Sınıf Adı", "Ders", "Öğretmen"))
        print("-"*45)

        for iliski in iliskiler:
            sinif_id, ders_id ,ogretmen_id = iliski
#Sınıf
            self.db.cursor.execute("SELECT sınıf_ismi FROM sınıflar WHERE Id = %s", (sinif_id,))
            sinif_adi = self.db.cursor.fetchone()[0]
#Ders#  
            self.db.cursor.execute("SELECT ders_ismi FROM dersler WHERE Id = %s", (ders_id,))
            ders_adi = self.db.cursor.fetchone()[0]
#Öğretmen
            self.db.cursor.execute("SELECT isim, soyisim FROM öğretmenler WHERE Id = %s", (ogretmen_id,))
            ogretmen = self.db.cursor.fetchone()
            ogretmen_adi = f"{ogretmen[0]} {ogretmen[1]}"

            print("{:<5} {:<15} {:<20} {:<15}".format(
                sinif_id, sinif_adi, ders_adi, ogretmen_adi))
    
    def tekSinifDersleriniListele(self,sinif_id):
        self.db.cursor.execute("SELECT DersId, ÖğretmenId FROM sınıf_dersleri WHERE SınıfId = %s", (sinif_id,))
        iliskiler = self.db.cursor.fetchall()

        self.db.cursor.execute("SELECT sınıf_ismi FROM sınıflar WHERE Id = %s", (sinif_id,))
        sinif_adi = self.db.cursor.fetchone()[0]   

        if not iliskiler:
            print(f"\n{sinif_adi} sınıfına ait ders bulunamadı!")
            return   
        print(f"\n{sinif_adi} Sınıfı Dersleri:")
        print("{:<20} {:<25}".format("Ders", "Öğretmen"))
        print("-"*45) 
        for iliski in iliskiler:
            ders_id, ogretmen_id = iliski
#Ders
            self.db.cursor.execute("SELECT ders_ismi FROM dersler WHERE Id = %s", (ders_id,))
            ders_adi = self.db.cursor.fetchone()[0]
# Öğretmen
            self.db.cursor.execute("SELECT isim, soyisim FROM öğretmenler WHERE Id = %s", (ogretmen_id,))
            ogretmen = self.db.cursor.fetchone()
            ogretmen_adi = f"{ogretmen[0]} {ogretmen[1]}"

            print("{:<20} {:<25}".format(ders_adi, ogretmen_adi))
    def addTeacher(self):
        print("\n--- Öğretmen Ekleme ---")

        while True:
            try:
                teacher_id = int(input("Öğretmen ID: "))

                existing_teacher = self.db.öğretmengetirId(teacher_id)
                if existing_teacher:
                    print(f"{teacher_id}'ye sahip bir öğretmen zaten var.Başka bir ID belirleyiniz.")
                    continue              
                branş = input("Branş: ")
                isim = input("Öğretmen adı: ")
                soyisim = input("Öğretmen soyadı: ")

                while True:
                    try:
                        year = int(input("Doğum yılı: "))
                        month = int(input("Doğum ayı: "))
                        day = int(input("Doğum günü: "))
                        birthdate = datetime.date(year, month, day)
                        break
                    except ValueError:
                        print("Geçersiz tarih! Lütfen doğru bir tarih girin.")

                cinsiyet = ""
                while cinsiyet not in ["E", "K"]:
                    cinsiyet = input("Cinsiyet (E/K): ").upper()
                    if cinsiyet not in ["E", "K"]:
                        print("Lütfen sadece 'E' veya 'K' giriniz!(E:Erkek/K:Kız)")

                teacher = Teacher(teacher_id, branş, isim, soyisim, birthdate, cinsiyet)
                self.db.öğretmenkayıt(teacher)
                print(f"\n {isim} {soyisim} başarıyla eklendi!")
                break

            except ValueError:
                print("Geçersiz ID! Lütfen sadece sayı girin.")
            except Exception as e:
                print(f"\nHata oluştu: {str(e)}")
                break

    def deleteStudent(self):
        classid = self.displayStudents()
        student_id = int(input("öğrenci numarası:"))

        self.db.öğrenciSil(student_id)

    def editStudent(self):
        classid = self.displayStudents()
        student_no = int(input("Öğrenci numarası:"))

        student = self.db.öğrencigetirId(student_no)

        student[0].isim = input('isim:') or student[0].isim
        student[0].soyisim = input('soyisim:') or student[0].soyisim
        student[0].cinsiyet = input('cinsiyet:') or student[0].cinsiyet
        student[0].sınıfId = input('sınıfId:') or student[0].sınıfId

        year = input("Doğum yılı:") or student[0].birthdate.year
        month = input("Doğum ayı:") or student[0].birthdate.month
        day = input("Doğum günü:") or student[0].birthdate.day

        year = int(year)
        month = int(month)
        day = int(day)

        student[0].doğumtarihi = datetime.date(int(year),int(month),int(day))
        self.db.öğrencidüzenle(student[0]) 

    def addStudent(self):
        classes = self.db.sınıfgetir()
        for c in classes:
            print(f"{c.Id}:{c.sınıf_ismi}") 

        classid = int(input("Hangi sınıf:"))      
        number = int(input("öğrenci numara:"))                     
        name = input("Öğrenci adı:")
        surname = input("Öğrenci soyad:")
        year = int(input("Doğum yılı:"))
        month = int(input("Doğum ayı:"))
        day = int(input("Doğum günü:"))
        birthdate = datetime.date(year,month,day)
        gender = input("Cinsiyet(E/K):")    
        student = Student(number,name,surname,birthdate,gender,classid)
        self.db.öğrencikayıt(student)

    def displayStudents(self):
        print("---Sınıf Listesi---")
        classes = self.db.sınıfgetir()
        for c in classes:
            print(f"{c.Id}:{c.sınıf_ismi}")

        classid = int(input("Hangi sınıf:")) 

        students = self.db.öğrencilerigetirSınıfId(classid )
        print("Öğrenci Listesi")
        for std in students:
            print(f"{std.okulnumarası}-{std.isim}{std.soyisim}")

        return classid
    def _get_sinif_ismi(self, classid, classes):
        for c in classes:
            if c.Id == classid:
                return c.sınıf_ismi
        return f"ID:{classid}"
app = App()
app.initApp()
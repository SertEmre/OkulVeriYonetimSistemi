from baglanti import DbManager
from connection import connection
import datetime
from ogrenciler import Student

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
                pass
            elif islem == "6":
                pass
            elif islem == "e" or islem == "Ç":
                break
            else:
                print("yanlış seçim yaptınız!")
    
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

        student[0].doğumtarihi = datetime.date(year, month, day)
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
        gender = input("Cindiyet(E/K):")    
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
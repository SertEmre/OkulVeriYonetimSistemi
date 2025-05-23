from baglanti import DbManager
from connection import connection
class App:
    def __init__(self):
        self.db = DbManager(connection)

    def initApp(self):
        msg ="****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\nÖğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-SInıflara Göre Dersler\n7-Çıkış(E/Ç)"
        while True:
            print(msg)
            islem = input("Seçim:")
            if islem == "1":
                self.displayStudents()
            elif islem =="2":
                pass
            elif islem =="4":
                pass
            elif islem == "5":
                pass
            elif islem == "6":
                pass
            elif islem == "e" or islem == "Ç":
                break
            else:
                print("yanlış seçim yaptınız!")
    
    def displayStudents(self):

        classes = self.db.sınıfgetir()
        for c in classes:
            print(f"{c.Id}:{c.sınıf_ismi}")

        classid = int(input("Hangi sınıf:")) 

        students = self.db.öğrencilerigetirSınıfId(classid )
        print("Öğrenci Listesi")
        for index,std in enumerate(students):
            print(f"{index+1}-{std.sınıf_ismi}{std.öğretmenId}")

app = App()
app.initApp()
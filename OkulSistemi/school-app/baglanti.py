import mysql.connector
from datetime import datetime
from connection import connection
from ogrenciler import Student
from ogretmenler import Teacher
from sınıflarr import Sınıflar

class DbManager:
    def __init__(self,connection):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def öğrencigetirId(self, okulnumarası):
        sql = "SELECT okulnumarası, isim, soyisim, doğumtarihi, cinsiyet, sınıfId FROM öğrenciler WHERE okulnumarası = %s"
        try:
            self.cursor.execute(sql, (okulnumarası,))
            obj = self.cursor.fetchone()

            if obj:
                return Student.CreateStudent(obj)
            else:
                return None
        except Exception as e:
            print("VERİTABANI HATASI:", str(e))
            return None

    def öğrencilerigetirSınıfId(self, sınıfId):
        sql = "SELECT okulnumarası, isim, soyisim, doğumtarihi, cinsiyet, sınıfId FROM öğrenciler WHERE sınıfId = %s"
        self.cursor.execute(sql, (sınıfId,))
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj) 
        except mysql.connector.Error as err:
            print("hata:", err)
            return None

    def öğrencikayıt(self,student: Student):  
        sql = "INSERT INTO öğrenciler(okulnumarası,isim,soyisim,doğumtarihi,cinsiyet,sınıfId) VALUES (%s,%s,%s,%s,%s,%s)"
        value =(student.okulnumarası,student.isim,student.soyisim,student.doğumtarihi,student.cinsiyet,student.sınıfId)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print('Hata:',err)
    
    def öğrencidüzenle(self,student:Student):
        sql = "UPDATE öğrenciler SET isim=%s, soyisim=%s, doğumtarihi=%s, cinsiyet=%s, sınıfId=%s WHERE okulnumarası=%s" 
        value = (student.isim, student.soyisim, student.doğumtarihi, student.cinsiyet, student.sınıfId, student.okulnumarası)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print('Hata:',err)
    
    def öğretmengetirId(self,Id):
        sql = "select * from öğretmenler where Id = %s" 
        value = (Id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Teacher.CreateTeacher(obj)
        except mysql.connector.Error as err:
            print("hata:",err)

    def öğretmendüzenle(self,teacher:Teacher):
        sql = "UPDATE öğretmenler SET branş = %s,isim=%s, soyisim=%s, doğum_günü=%s, cinsiyet=%s WHERE Id= %s" 
        value = (teacher.branş, teacher.isim, teacher.soyisim, teacher.doğum_günü, teacher.cinsiyet, teacher.Id)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt güncellendi.")
        except mysql.connector.Error as err:
            print('Hata:', err)

    def öğretmenkayıt(self,teacher:Teacher):
        sql = "INSERT INTO öğretmenler(Id,branş,isim,soyisim,doğum_günü,cinsiyet) VALUES (%s,%s,%s,%s,%s,%s)"
        value =(teacher.Id,teacher.branş,teacher.isim,teacher.soyisim,teacher.doğum_günü,teacher.cinsiyet)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print('Hata:',err)       
    def sınıfgetir(self):
        sql = "SELECT Id, sınıf_ismi, öğretmenId FROM sınıflar"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            liste = []
            for i in obj:
                liste.append(Sınıflar(i[0], i[1], i[2]))  
            return liste
        except mysql.connector.Error as err:
            print("hata:", err)
            return None
    def öğrenciSil(self,okulnumarası):
        sql = "DELETE FROM öğrenciler WHERE okulnumarası = %s"
        value = (okulnumarası,)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt silindi.")
        except mysql.connector.Error as err:
            print('Hata:',err)
    
    def __del__(self):
        self.connection.close()
        print("db silindi")

db = DbManager(connection)


# ---------------------------------Öğretmen Ekleme
# doğum_tarihi = datetime(1994,4,23)
# tchr = Teacher(4,"Beden","İsmet","Paşa",doğum_tarihi,"E")
# db.öğretmenkayıt(tchr)
#------------------------------Öğretmen Düzenle
# tchr = db.öğretmengetirId(2)
# if tchr:
#     tchr = tchr[0]
#     tchr.isim = "Fırat"
#     db.öğretmendüzenle(tchr)
# else:
#     print("Değişiklik yapmak istediğiniz öğretmen bulunamadı")

#-----------------------------------Öğrenci Düzenle
# student =db.öğrencigetirId(1010)
# if isinstance(student,list):
#     student = student[0]
#     student.isim = "Fırat"
#     db.öğrencidüzenle(student)
# else:
#     print("Değiştirilmek istenen Öğrenci bulunamadı")

#-----------------------------------Öğrenci kayıt
# doğumtarihi = datetime(2005,2,17)
# std = Student(1011,"Emre","Sert",doğumtarihi,"E",1)

# db.öğrencikayıt(std)
#-----------------------------------------------Öğrenci gösterme
#students = db.öğrencigetirId(1001)
# if students:
#     student = students[0]
#     print(f"Öğrenci: {student.isim} {student.soyisim}")
# else:
#     print("Bu okul numarasına ait öğrenci bulunamadı!")

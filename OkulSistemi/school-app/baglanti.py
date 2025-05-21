import mysql.connector
from datetime import datetime
from connection import connection
from ogrenciler import Student
from ogretmenler import Teacher


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

    def öğrencilerigetirSınıfId(self,sınıfId):
        sql = "select * from öğrenciler where sınıfId = %s" 
        value = (sınıfId,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("hata:",err)

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

    def öğretmendüzenle(self,teacher:Teacher):
        pass

    def öğretmenkayıt(self,teacher:Teacher):
        pass       

    def __del__(self):
        self.connection.close()
        print("db silindi")

db = DbManager(connection)

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

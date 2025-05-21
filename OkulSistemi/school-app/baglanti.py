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
        pass
    
    def öğrencidüzenle(self,student:Student):
        pass

    def öğretmendüzenle(self,teacher:Teacher):
        pass

    def öğretmenkayıt(self,teacher:Teacher):
        pass       

db = DbManager(connection)

students = db.öğrencigetirId(1)
if students:
    student = students[0]
    print(f"Öğrenci: {student.isim} {student.soyisim}")
else:
    print("Bu okul numarasına ait öğrenci bulunamadı!")

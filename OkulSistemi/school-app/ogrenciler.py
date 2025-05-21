class Student:
    def __init__(self,okulnumarası,isim,soyisim,doğumtarihi,cinsiyet,sınıfId):
        if okulnumarası is None:
            self.okulnumarası = 0
        else:
            self.okulnumarası = okulnumarası
        self.isim = isim
        self.soyisim = soyisim
        self.doğumtarihi = doğumtarihi
        self.cinsiyet = cinsiyet
        self.sınıfId = sınıfId

    @staticmethod
    def CreateStudent(obj):
        liste = []

        if isinstance(obj, tuple):
            liste.append(Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5]))
        else:
            for i in obj:
                liste.append(Student(i[0],i[1],i[2],i[3],i[4],i[5]))
        return liste
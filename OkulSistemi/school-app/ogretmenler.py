class Teacher:
    def __init__(self,Id,branş,isim,soyisim,doğum_günü,cinsiyet):
        if Id is None:
            self.Id = 0
        else:
            self.Id = Id
        self.branş = branş
        self.isim = isim
        self.soyisim = soyisim
        self.doğum_günü = doğum_günü
        self.cinsiyet = cinsiyet
        
    @staticmethod
    def CreateTeacher(obj):
        liste = []
        if isinstance(obj, tuple):
            liste.append(Teacher(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5]))
        else:
            for i in obj:
                liste.append(Teacher(i[0],i[1],i[2],i[3],i[4],i[5]))
        return liste
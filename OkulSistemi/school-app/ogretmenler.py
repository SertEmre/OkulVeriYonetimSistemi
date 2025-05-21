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
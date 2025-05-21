class Sınıflar:
    def __init__(self,Id,isim,öğretmenId):
        if Id is None:
            self.Id = 0
        else:
            self.Id = Id
        self.isim = isim
        self.öğretmenId = öğretmenId
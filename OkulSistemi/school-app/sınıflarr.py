class Sınıflar:
    def __init__(self, Id, sınıf_ismi, öğretmenId):
        self.Id = Id if Id is not None else 0
        self.sınıf_ismi = sınıf_ismi  
        self.öğretmenId = öğretmenId
    @staticmethod
    def SınıfOluştur(obj):
        liste = []

        for i in obj:
            list.append(Sınıflar(i[0],i[1],i[2]))

        return liste
        

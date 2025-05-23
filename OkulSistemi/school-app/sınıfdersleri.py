class Sınıfdersleri:
    def __init__(self,SınıfId,DersId,ÖğretmenId):
        if SınıfId is None:
            self.SınıfId = 0
        else:
            self.SınıfId = SınıfId
        self.DersId = DersId
        self.ÖğretmenId = ÖğretmenId
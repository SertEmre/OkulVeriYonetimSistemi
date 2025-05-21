class Dersler:
    def __init__(self,Id,isim):
        if Id is None:
            self.Id = 0
        else:
            self.Id = Id
        self.isim = isim
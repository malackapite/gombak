class Gomba:
    def __init__(self, sor : str):
        self.nev= sor.split("@")[0]
        self.nemzettseg= sor.split("@")[1]
        self.evszak= sor.split("@")[2]
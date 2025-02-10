class Pycar:
    velocidad:int
    
    def encender(self):
        return True
    
    def apagar(self):
        return False
    
    def acelerar(self):
        self.velocidad=100
    
    def frenar(self):
        self.velociad=0

    def retroceder(self):
        self.velocidad=-10
        
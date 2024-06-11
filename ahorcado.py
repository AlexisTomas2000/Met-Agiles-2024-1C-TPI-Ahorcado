class Ahorcado():
    pass
    def __init__(self) -> None:
        self.nombre = ''
        self.letra=''
        self.name=''
        self.intentonro=0
        self.puntajeJug=0
  
    def login(self,name:str):
        self.nombre = name

    def jugar(self,leta:chr):
        self.letra=leta
    
    def letrapertenece(self,letra,palabra):
        return letra in palabra
    
    def arri_pal(self,name):
        self.name=name

    def intento(self,intento):
        self.intentonro=intento+1

    def puntaje(self,intento):
        self.puntajeJug=(1/intento)*100
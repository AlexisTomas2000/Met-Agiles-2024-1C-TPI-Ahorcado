from ahorcado import *

nombre = 'Alexis'

def test_log():
    jugada = Ahorcado()
    jugada.login(nombre)=='Alexis'
def test_letra():
    jugada = Ahorcado()
    jugada.jugar('A')=='A'
    
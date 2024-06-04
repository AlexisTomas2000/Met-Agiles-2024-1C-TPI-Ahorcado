from ahorcado import *

nombre = 'Alexis'
palabra = 'Python'
letrap = 'h'
letranp = 'q'

def test_log():
    jugada = Ahorcado()
    jugada.login(nombre)=='Alexis'

def test_letra():
    jugada = Ahorcado()
    jugada.jugar('A')=='A'

def test_perteneceletra():
    jugada = Ahorcado()
    assert jugada.letrapertenece(letrap,palabra)==True

def test_noperteneceletra():
    jugada = Ahorcado()
    assert jugada.letrapertenece(letranp,palabra)==False

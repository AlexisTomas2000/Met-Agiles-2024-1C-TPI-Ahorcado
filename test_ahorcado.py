from ahorcado import *

nombre = 'Alexis'
palabra = 'Python'
palabra2 = 'NoPython'
letrap = 'h'
letranp = 'q'
intento=4

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

def test_arriPal():
    jugada = Ahorcado()
    jugada.arri_pal(palabra)=='Python'

def test_arriPal():
    jugada = Ahorcado()
    jugada.arri_pal(palabra)=='Python'

def test_NoarriPal():
    jugada = Ahorcado()
    jugada.arri_pal(palabra2)=='Python'

def test_intentos():
    jugada = Ahorcado()
    jugada.intento(intento)==4

def test_puntaje():
    jugada = Ahorcado()
    jugada.puntaje(intento)==(1/4)*100
    
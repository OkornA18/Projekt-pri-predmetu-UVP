import bottle
from model import Matrika

def prepoznaj_matriko(matrika):

    matrika = matrika.split("\n")
    matrika1 = []
    for vrstica in matrika:
        vrstica = vrstica.split()
        vrstica = [float(x) for x in vrstica]
        matrika1.append(vrstica)
    return Matrika(matrika1)

@bottle.get("/")
def osnovna_stran():
    return bottle.template("Projekt-pri-predmetu-UVP-master/views/osnovna_stran.tpl")

@bottle.get("/sestevanje")
def sestevanje():
    return bottle.template("Projekt-pri-predmetu-UVP-master/views/operacije.tpl", operacija="/sestej", operator="+", operiraj="SEŠTEJ")

@bottle.post("/sestej")
def sestej():
    matrika1_besedilo = bottle.request.forms["matrika1"]
    matrika2_besedilo = bottle.request.forms["matrika2"]
    matrika1 = prepoznaj_matriko(matrika1_besedilo)
    matrika2 = prepoznaj_matriko(matrika2_besedilo)
    vsota = matrika1 + matrika2
    return bottle.template("Projekt-pri-predmetu-UVP-master/views/rezultat.tpl", rezultat=vsota)

@bottle.get("/odstevanje")
def odstevanje():
    return bottle.template("Projekt-pri-predmetu-UVP-master/views/operacije.tpl", operacija="/odstej", operator="-", operiraj="ODŠTEJ")

@bottle.post("/odstej")
def odstej():
    matrika1_besedilo = bottle.request.forms["matrika1"]
    matrika2_besedilo = bottle.request.forms["matrika2"]
    matrika1 = prepoznaj_matriko(matrika1_besedilo)
    matrika2 = prepoznaj_matriko(matrika2_besedilo)
    vsota = matrika1 - matrika2
    return bottle.template("Projekt-pri-predmetu-UVP-master/views/rezultat.tpl", rezultat=vsota)

@bottle.get("/mnozenje")
def mnozenje():
    return bottle.template("Projekt-pri-predmetu-UVP-master/views/operacije.tpl", operacija="/zmnozi", operator="*", operiraj="POMNOŽI")

@bottle.post("/zmnozi")
def zmnozi():
    matrika1_besedilo = bottle.request.forms["matrika1"]
    matrika2_besedilo = bottle.request.forms["matrika2"]
    matrika1 = prepoznaj_matriko(matrika1_besedilo)
    matrika2 = prepoznaj_matriko(matrika2_besedilo)
    zmnozek = matrika1 * matrika2
    return bottle.template("Projekt-pri-predmetu-UVP-master/views/rezultat.tpl", rezultat=zmnozek)


bottle.run(reloader=True, debug=True)
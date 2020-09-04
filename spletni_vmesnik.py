import bottle
from model import Matrika

def matrika_v_pravi_obliki(matrika):

    matrika = matrika.split("\n")
    matrika1 = []
    for vrstica in matrika:
        vrstica = vrstica.split()
        vrstica = [float(x) for x in vrstica]
        matrika1.append(vrstica)
    return Matrika(matrika1)

@bottle.get("/") 
def osnovna_stran():
    return bottle.template("views/osnovna_stran.tpl")

@bottle.get("/sestevanje")
def sestevanje():
    return bottle.template("views/operacije.tpl", operacija="/sestej", operator="+", operiraj="SEŠTEJ")

@bottle.post("/sestej")
def sestej():
    matrika1_besedilo = bottle.request.forms["matrika1"]
    matrika2_besedilo = bottle.request.forms["matrika2"]
    matrika1 = matrika_v_pravi_obliki(matrika1_besedilo)
    matrika2 = matrika_v_pravi_obliki(matrika2_besedilo)
    vsota = matrika1 + matrika2
    return bottle.template("views/rezultat.tpl", rezultat=vsota)

@bottle.get("/odstevanje")
def odstevanje():
    return bottle.template("views/operacije.tpl", operacija="/odstej", operator="-", operiraj="ODŠTEJ")

@bottle.post("/odstej")
def odstej():
    matrika1_besedilo = bottle.request.forms["matrika1"]
    matrika2_besedilo = bottle.request.forms["matrika2"]
    matrika1 = matrika_v_pravi_obliki(matrika1_besedilo)
    matrika2 = matrika_v_pravi_obliki(matrika2_besedilo)
    vsota = matrika1 - matrika2
    return bottle.template("views/rezultat.tpl", rezultat=vsota)

@bottle.get("/mnozenje")
def mnozenje():
    return bottle.template("views/operacije.tpl", operacija="/zmnozi", operator="*", operiraj="POMNOŽI")

@bottle.post("/zmnozi")
def zmnozi():
    matrika1_besedilo = bottle.request.forms["matrika1"]
    matrika2_besedilo = bottle.request.forms["matrika2"]
    matrika1 = matrika_v_pravi_obliki(matrika1_besedilo)
    matrika2 = matrika_v_pravi_obliki(matrika2_besedilo)
    zmnozek = matrika1 * matrika2
    return bottle.template("views/rezultat.tpl", rezultat=zmnozek)

@bottle.get("/sledenje")
def sledenje():
    return bottle.template("views/matrika.tpl", potek="/sled", kar_racunam="SLED")

@bottle.post("/sled")
def sled():
    matrika_besedilo = bottle.request.forms["matrika"]
    matrika = matrika_v_pravi_obliki(matrika_besedilo)
    sled = matrika.sled()
    return bottle.template("views/potek.tpl", rezultat=sled)

bottle.run(reloader=True, debug=True)
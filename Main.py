import time
import Intro
import Mini_games

Intro.intro()

paus = input("\nVajuta Enter, et jätkata...\n")

nimi = input("Vali oma nimi: ")

Intro.kirjuta(f"{nimi}: Kes see nüüd nii vara ustele koputab?\n")
time.sleep(1)
Intro.kirjuta(f"Kui {nimi} ukse avas nägi ta meeliva üllatusena kes seal on.")
paus

Intro.kirjuta(f"{nimi}: OI! Joe, mis sind nii vara siia toob? Kell pole isegi 9 veel.")
Intro.kirjuta(f"""Joe: Hea asi, et ma suu aadressi mäletasin {nimi}.
Aga minu tuleku põhjuseks on (kurat ära unustasin) hiljem räägin.""")
time.sleep(1)
Intro.kirjuta("""Joe: (Grrrr) Ma tunnen kuidas kõht koriseb, sellest rännakust
sinu juurde, sööme midagi ja samal ajal räägin oma külastuse põhjusest.\n""")
paus
Intro.puhasta()
Intro.kirjuta("Joe: Tead mis oleks hea idee?")
Intro.kirjuta(f"{nimi}: Noo lase aga käia.")
Intro.kirjuta("Joe: Me võiks mängida kivi, paber, kääre. Võitja valib hommikusöögi. Ja kui on viik, valin ikka mina.")

mängi_kpk = input("1 = (natuke ebaaus aga ok), 2 = (ei viitsi): \n")

joe_valib, meenutus = Mini_games.Joe_toidud()

#todo] Kivi, Paber, Käärid (ei ole korduv)

if mängi_kpk == "1":
    Intro.kirjuta(f"{nimi}: Natuke ebaaus aga ok")
    Mini_games.kivi_paber_käärid()
else:
    Intro.kirjuta(f"{nimi}: Ma ei viitsi su mänge mängida. Lihtsalt vali ise.")
    Intro.kirjuta(f"Joe: Teeme nii! Mind isutab {joe_valib}")
    Intro.kirjuta(f"{nimi}: Oke, ma kohe toon lauale.")
    time.sleep(4)
    Intro.kirjuta(f"{meenutus}")

paus
Intro.puhasta()
Intro.kirjuta(f"Joe: See tuletas mulle meelde, et miks ma üldse tulin siia.")
Intro.kirjuta(f"{nimi}: No sülita välja siis juba.")
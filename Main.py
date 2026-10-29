import time
import Intro
import Mini_games

nimi = input("Vali oma nimi: ")

Intro.kirjuta(f"{nimi}: Kes see nüüd nii vara ustele koputab?\n")
time.sleep(1)
Intro.kirjuta(f"Kui {nimi} ukse avas nägi ta meeliva üllatusena kes seal on")
input("\nVajuta Enter, et jätkata...\n")

Intro.kirjuta(f"{nimi}: OI! Joe, mis sind nii vara siia toob. Kell pole isegi 9 veel")
Intro.kirjuta(f"""Joe: Hea asi, et ma suu aadressi mäletasin {nimi}.
Aga minu tuleku põhjuseks on (kurat ära unustasin) hiljem räägin.""")
time.sleep(1)
Intro.kirjuta("""Joe: (Grrrr) Ma tunnen kuidas kõht koriseb, sellest rännakust
sinu juurde, sööme midagi ja samal ajal räägin oma külastuse põhjusest.\n""")
time.sleep(2)
Intro.kirjuta("Joe: Tead mis oleks hea idee?")
Intro.kirjuta(f"{nimi}: Noo lase aga käia.")
Intro.kirjuta("Joe: Me võiks mängida kivi, paber, kääre. Võitja valib hommikusöögi. Ja kui on viik, valin ikka mina.")

mängi_kpk = input("1 = (natuke ebaaus aga ok), 2 = (ei viitsi): \n")

joe_valib = Mini_games.Joe_isu()

if mängi_kpk == "1":
    Intro.kirjuta(f"{nimi}: Natuke ebaaus aga ok")
    Mini_games.kivi_paber_käärid()
else:
    Intro.kirjuta(f"{nimi}: Ma ei viitsi su mänge mängida. Lihtsalt vali ise.")
    Intro.kirjuta(f"Joe: Teeme nii! Mind isutab {joe_valib}")

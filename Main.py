import time
import Intro
import Mini_games

nimi = input("Vali oma nimi: ")

Intro.kirjuta(f"{nimi}: Kes see nüüd nii vara ustele koputab?\n")
time.sleep(1)
Intro.kirjuta(f"Kui {nimi} ukse avas nägi ta meeliva üllatusena kes seal on")
input("\nVajuta Enter, et jätkata...\n")

Intro.kirjuta(f"{nimi}: OI! Gundalf, mis sind nii vara siia toob. Kell pole isegi 9 veel")
Intro.kirjuta(f"""Gundalf: Hea asi, et ma suu aadressi mäletasin {nimi}.
Aga minu tuleku põhjuseks on (kurat ära unustasin) hiljem räägin.""")
time.sleep(1)
Intro.kirjuta("""Gundalf: (Grrrr) Ma tunnen kuidas kõht koriseb sellest rännakust,
sinu juurde, sööme midagi ja samal ajal räägin oma külastuse põhjusest.""")

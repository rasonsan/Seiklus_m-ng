
#! See osa on AI-ga tehtud
import time
import os

def puhasta():
    os.system("cls" if os.name == "nt" else "clear")

def kirjuta(tekst, viivitus=0.04):
    for taht in tekst:
        print(taht, end="", flush=True)
        time.sleep(viivitus)
    print()

def intro():
    puhasta()
    print("=== Vana tuttav ===\n")
    kirjuta("Ärkad soojas voodis, tuttavale helile.")
    time.sleep(1)
    kirjuta("Keegi koputab uksele...")
    time.sleep(1)
    input("\nVajuta Enter, et alustada...")
    puhasta()

intro()

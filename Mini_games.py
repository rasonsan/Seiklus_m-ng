from random import choice, randint

def numbri_mäng():
    arvuti = randint(1,100)
    mängja = int(input("Vali number 1-100: "))
    while mängja != arvuti:
        mängja = int(input("Vali uuesti: "))
        if mängja < arvuti:
            print("Liiga väike")
        elif mängja > arvuti:
            print("Liiga suur")

    print("arvasid õigesti")

def kivi_paber_käärid():
    arvuti_valik = ("kivi", "paber", "käärid")
    kivi = "1"
    paber = "2"
    käärid = "3"
    while True:
        arvuti = choice(arvuti_valik)
        mängja = input("Vali number: 1.(kivi), 2.(paber), 3.(käärid): ")
        if mängja == "1" and arvuti == "käärid":
            print(f"Võitsid, arvuti valis {arvuti}")
            break
        elif mängja == "2" and arvuti == "kivi":
            print(f"Võitsid, arvuti valis {arvuti}")
            break
        elif mängja == "3" and arvuti == "paber":
            print(f"Võitsid, arvuti valis {arvuti}")
            break
        else:
            print(f"uuesti, arvuti valis {arvuti}")

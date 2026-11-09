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

    return print("Arvatud!!")

def kivi_paber_käärid():
    arvuti_valik = ("kivi", "paber", "käärid")
    kivi = "1"
    paber = "2"
    käärid = "3"
    arvuti_toit = ("võileib", "peekon munaga", "puder", "müsli")
    arvuti_isu = choice(arvuti_toit)
    
    arvuti = choice(arvuti_valik)
    mängja = input("Vali number: 1.(kivi), 2.(paber), 3.(käärid): ")
    if mängja == "1" and arvuti == "käärid":
        print("Võitsid")
        mängja_isu = input("Mis toidu isu sul on?: ")
    elif mängja == "2" and arvuti == "kivi":
        print(f"Võitsid")
        mängja_isu = input("Mis toidu isu sul on?: ")
    elif mängja == "3" and arvuti == "paber":
        print(f"Võitsid")
        mängja_isu = input("Mis toidu isu sul on?: ")   
    else:
        print(f"Joe: Mind isutab {arvuti_isu}.")

def Joe_toidud():
    Joe_toit = "võileib", "peekon munaga", "puder", "müsli"
    Joe_isu = choice(Joe_toit)
    if Joe_isu == "võileib":
        meenutus = "Joe: Mhhhhhh, tuletab mulle ühte kohvikut meelde."
    elif Joe_isu == "peekon munaga":
        meenutus = "Joe: Täpselt nagu matkates, lapsena."
    elif Joe_isu == "puder":
        meenutus = "Joe: JEESUS!! See meenutab lapsepõlve vanaema juures."
    elif Joe_isu == "müsli":
        meenutus = "Joe: Mu lemmik kuu lõpu toit."
 
    return Joe_isu, meenutus


def varustus():
    riistad = "haamer", "nuga", "sai", "Coca-Cola", "labidas", "müts", "sall", "müstiline võti"
    haamer = 1, nuga = 2, sai = 3, Coca_Cola = 4, labidas = 5, müts = 6, sall = 7, müstiline_võti = 8
    riistade_valik = [1, 2, 3, 4, 5, 6, 7, 8]
    vali = int(input("""Vali üks asi mida kaasa võtta!
    1.(haamer)| 2.(nuga)| 3.(sai)| 4.(Coca-Cola)| 5.(labidas)| 6.(müts)| 7.(sall)| 8.(müstiline võti)"""))

    return vali


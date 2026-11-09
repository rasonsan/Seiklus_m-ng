from random import choice, randint

def numbri_mäng():      #!  Numbri äraarvamis mäng, mis tuleb kasutusse millalgi loo lõpus
    arvuti = randint(1,100)
    mängja = int(input("Vali number 1-100: "))
    while mängja != arvuti:
        mängja = int(input("Vali uuesti: "))
        if mängja < arvuti:
            print("Liiga väike")
        elif mängja > arvuti:
            print("Liiga suur")

    return print("Arvatud!!")

def kivi_paber_käärid():    #!  Kivi, Paber, Käärid, mis originaalselt oli lõpmatus tsüklis kuniks mõistsin et see ei sobiks mänguga kokku.
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

    return arvuti_isu

def Joe_toidud():   #^  Toidu valikud, mis mõjutavad kuidas lugu edasi läheb peale hommikusööki
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


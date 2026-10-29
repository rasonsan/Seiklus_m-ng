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
        print(f"Joe: Mind isutab {arvuti_isu}")

def Joe_isu():
    Joe_toit = ("võileib", "peekon munaga", "puder", "müsli")
    Joe_isu = choice(Joe_toit)
    return Joe_isu

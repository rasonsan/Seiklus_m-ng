
#~  Siin on asjad, mis on loole olulised, aga on liiga erinevad teistest funktsjoonidest
 
import time
import Intro
import Mini_games

Joe_valib, suva = Mini_games.Joe_toidud()

def varustus():    #? Saad ühe eseme valida mille seiklusele kaasa võtad
    haamer = 1
    nuga = 2
    sai = 3
    Coca_Cola = 4
    labidas = 5
    müts = 6
    sall = 7
    müstiline_võti = 8
   
    vali = input("Vali üks asi mida kaasa võtta! 1.(haamer)| 2.(nuga)| 3.(sai)| 4.(Coca-Cola)| 5.(labidas)| 6.(müts)| 7.(sall)| 8.(müstiline võti)")

    return vali


def peale_hommikut():   #todo]  See mõjutab hommikusöögi järgi kuidas lugu edasi liigub
    

    if Joe_valib == "võileib":
        Intro.kirjuta("""Joe: Ma kuulsin, et ühes kohvikus Plädrikul juhtus midagi. 
        Mõtlesin kuidas see oleks perfektne väike mõistatus mida lahendada.""")
    elif Joe_valib == "peekon munaga":
        Intro.kirjuta("Joe: Mõtlesin, et läheks kahekesi matkama.")
    elif Joe_valib == "puder":
        Intro.kirjuta("Joe: Vanaema soovis tasuta tööjõudu, ta tahtis et kutsuksin su kaasa.")
    elif Joe_valib == "müsli":
        Intro.kirjuta("""Joe: Mul rahad otsas. Ära muretse ma ei tulnud laenu küsima, see kord. 
        Aga mul on hea mõte kuidas raha teenida.""")
    

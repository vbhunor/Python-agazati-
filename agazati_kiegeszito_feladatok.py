def elso_ot_betu(string):
###Írd ki adott string első 5 betűjét!
    return string[0:5]
    
    

assert elso_ot_betu("Sziasztok!") == "Szias"


def utolso_ket_betu(string):
###Írd ki adott string utolso 2 betűjét!
    return string[-2:]

assert utolso_ket_betu("Sziasztok!") == "k!"


def mondatjel(szoveg):
###Tegyél adott szöveg végére egy felkiáltójelet!
    return szoveg + "!"


assert mondatjel("Szegény Jankó") == "Szegény Jankó!"

       
def diszkriminans(a, b, c):
    if b**2 - 4*a*c > 0:
        return "Az egyenletnek két megoldása van."
    elif b**2 - 4*a*c == 0:
        return "Az egyenletnek egy megoldása van."
    else:
        return "Az egyenletnek nincs megoldása."
    
assert diszkriminans(3, 5, -1) == "Az egyenletnek két megoldása van."
assert diszkriminans(4, 8, 4) == "Az egyenletnek egy megoldása van."
assert diszkriminans(7, 4, 20) == "Az egyenletnek nincs megoldása."
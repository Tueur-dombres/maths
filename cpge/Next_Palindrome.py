def next_palin(number):
    str_number = str(number)
    longueur = len(str_number)

    first_half = str_number[:longueur//2+longueur%2]

    i = 1
    pas_assez_grand = False
    while i<len(first_half)+1: #une comparaison inutilement compliquée
        if first_half[-i] < str_number[longueur//2+i-1]:
            pas_assez_grand = True
            break
        elif first_half[-i] > str_number[longueur//2+i-1]:
            break
        else:
            i+=1

    if i == len(first_half)+1:pas_assez_grand = True
    suivant = int(first_half)
    if pas_assez_grand:suivant+=1
    str_suivant = str(suivant)

    if len(str_suivant)!=len(first_half): #que des neufs
        if longueur % 2: str_suivant = str_suivant[:-1]
        longueur+=1


    retour = "".join([str_suivant,str_suivant[-1-(longueur%2)::-1]])
    return int(retour)

for x,y in (12345,12421),(11,22),(134,141),(9876543219123456789,9876543220223456789):
    a = next_palin(x)
    print(a==y, a, y)  
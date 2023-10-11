def trapped_cell(n:int, m:int) -> int:
    global size,matrice,pos
    size = 0
    matrice = [[-1]]
    pos = [0,0] #x,y
    def agrandissement():
        global matrice,size,pos
        size += 1
        pos = [pos[0]+1,pos[1]+1]
        matrice = [[0]*(2*size+1)]+[[0]+row+[0] for row in matrice]+[[0]*(2*size+1)]
        start = (2*size-1)**2
        for i in range(size*2):
            matrice[-2-i][-1] = start+i
            matrice[0][-2-i] = start+size*2+i
            matrice[1+i][0] = start+size*4+i
            matrice[-1][1+i] = start+size*6+i

    def cases():
        global pos
        while pos[0] < m or pos[1] < m or pos[0] > 2*size-m or pos[1] > 2*size-m:
            agrandissement()
        retour = []
        for x,y in (m,n),(m,-n),(n,-m),(-n,-m),(-m,-n),(-m,n),(-n,m),(n,m):
            if matrice[pos[1]+y][pos[0]+x] != -1:
                retour+=[[pos[0]+x,pos[1]+y]]
        return retour

    possibilites = cases()
    while possibilites:
        pos = min(possibilites,key = lambda elt:matrice[elt[1]][elt[0]])
        a=matrice[pos[1]][pos[0]]
        matrice[pos[1]][pos[0]] = -1
        possibilites = cases()
    return a
print(trapped_cell(1,2))
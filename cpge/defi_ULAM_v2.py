def trapped_cell(n:int, m:int) -> int:
    global pos,vus
    vus = [[0]*10**4 for _ in range(10**4)]
    vus[len(vus)//2][len(vus)//2] = 1
    pos = [0,0] #x,y
    def valeurs(posi):
        x,y = posi
        if x==y==0:return 0
        if y <= -abs(x):
            start = (2*y+1)**2-x+3*abs(y)-1
        elif x <= -abs(y):
            start = (2*x+1)**2+y+5*abs(x)-1
        elif y >= abs(x):
            start = (2*y-1)**2+x+7*abs(y)-1
        elif x >= abs(y):
            start = (2*x-1)**2-y+abs(x)-1
        return start
    """
    def agrandissement():
        global vus
        l = len(vus)+2
        vus = [[0]*l]+[[0]+elt+[0] for elt in vus]+[[0]*l]
    """
    def cases():
        global pos,vus
        retour = []
        #while max(abs(pos[0]),abs(pos[1]))*2>=len(vus)-2*m:agrandissement()
        for x,y in (m,n),(m,-n),(n,-m),(-n,-m),(-m,-n),(-m,n),(-n,m),(n,m):
            if not vus[pos[1]+y+len(vus)//2][pos[0]+x+len(vus)//2]:
                retour+=[[pos[0]+x,pos[1]+y]]
        return retour
        
    possibilites = cases()
    while possibilites:
        pos = min(possibilites,key = lambda elt:valeurs(elt))
        possibilites = cases()
        vus[pos[1]+len(vus)//2][pos[0]+len(vus)//2] = 1
    return valeurs(pos)
print(trapped_cell(1,2))
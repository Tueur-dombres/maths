def pal(n):
    cp = 0
    i = -1
    while cp < n:
        i+=1
        L = list(str(i))
        L.reverse()
        if str(i) == ''.join(L):
            cp+=1
    return i
print(pal(2021))
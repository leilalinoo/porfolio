def bekeres():
    szam = int(input("Egész pozitív szám: "))
    while not (szam > 0):
        szam = int(input("Hiba!\nPozitív egész szám: "))
    return szam


def fibonacci(listahossz):
    fibolist = []
    fibolist.append(bekeres())
    fibolist.append(fibolist[0])
    for i in range(listahossz):
        segedvaltozo = fibolist[i] + fibolist[i + 1]
        fibolist.append((segedvaltozo))
    print(fibolist)
    return fibolist

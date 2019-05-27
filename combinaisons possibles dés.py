MAX = 8

# Programme principal =========================================================
nbd = int(input("Nombre de dés [2 .. { :d}] :".format(MAX)))
while not(nbd >= 2and nbd <= MAX) :
    nbd = int(input("Nombre de dés [2 .. { :d}], s.v.p. :".format(MAX)))

s = int(input("Entrez un entier [{ :d} .. { :d}] :".format(nbd, 6*nbd)))
while not(s >= nbd and s <= 6*nbd) :
    s = int(input("Entrez un entier [{ :d} .. { :d}], s.v.p. :".format(nbd, 6*nbd)))

if s == nbd or s == 6*nbd :
    cpt = 1 # 1 seule solution
else :
    I = [1]*nbd # initialise une liste de <nbd> dés
    cpt, j = 0, 0
    while j < nbd :
        som = sum([I[k] for k in range(nbd)])

        if som == s :
            cpt += 1 # compteur de bonnes solutions
        if som == 6*nbd :
            break

        j = 0
        if I[j] < 6:
            I[j] += 1
        else :
            while I[j] == 6:
                I[j] = 1
                j += 1
            I[j] += 1

print("Il y a { :d} façons de faire { :d} avec { :d} dés.".format(cpt, s, nbd))
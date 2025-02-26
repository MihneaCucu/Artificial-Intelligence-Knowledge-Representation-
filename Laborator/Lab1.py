from collections import deque

class Nod:

    def __init__(self, info, parinte=None):
        self.informatie = info
        self.parinte = parinte
        self.succesori = []

    def __str__(self):
        drum = self.drumRadacina()
        drum_info = " -> ".join([str(nod.informatie) for nod in drum])
        return f"{self.informatie} ({drum_info})"

    def __repr__(self):
        return str(self)

    def drumRadacina(self):
        nod = self
        drum = []
        while nod:
            drum.append(nod)
            nod = nod.parinte
        return list(reversed(drum))

    def vizitat(self):
        nod = self.parinte
        while nod:
            if nod.informatie == self.informatie:
                return True
            nod = nod.parinte
        return False



class Graf:
    def __init__(self, nodStart, noduriScop, muchii):
        self.nodStart = Nod(nodStart)
        self.noduriScop = set(noduriScop)
        self.muchii = muchii

    def scop(self, nod):
        return nod.informatie in self.noduriScop

    def succesori(self, nod):
        lista_succesori = []
        if nod.informatie in self.muchii:
            for (info_vecin, cost) in self.muchii[nod.informatie]:
                nod_nou = Nod(info_vecin, nod)
                if not nod_nou.vizitat():
                    lista_succesori.append(nod_nou)
        return lista_succesori


from collections import deque


def BFS(graf, n):

    coada = deque([graf.nodStart])
    solutii_gasite = 0

    while coada and solutii_gasite < n:
        nod_curent = coada.popleft()

        if graf.scop(nod_curent):
            print(f"Solutia {solutii_gasite + 1}: {nod_curent}")
            solutii_gasite += 1

        for succesor in graf.succesori(nod_curent):
            coada.append(succesor)


def DFS(nod, graf, solutii_gasite, n):

    if solutii_gasite[0] >= n:
        return True

    if graf.scop(nod):
        print(f"Solutia {solutii_gasite[0] + 1}: {nod}")
        solutii_gasite[0] += 1


    for succesor in graf.succesori(nod):
        if DFS(succesor, graf, solutii_gasite, n):
            return True

    return False

if __name__ == "__main__":

    nod1 = Nod("A")
    nod2 = Nod("B", nod1)
    nod3 = Nod("C", nod2)


    print(nod1)
    print(nod2)
    print(nod3)


    print(nod3.vizitat())
    nod4 = Nod("A", nod3)
    print(nod4.vizitat())
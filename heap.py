class heap:
    def __init__(self, wprowadzane=[]):
        self.heap =[0]
        for i in wprowadzane:
            self.heap.append(i)
            self.floatup(len(self.heap)-1)

    #floatowanie elementu z dolu do opdowiedniej pozycji do gory
    def floatup(self,index):
        pindex=index//2 #pindex - index rodzica
        if pindex<2:
            return
        while pindex > 0 and self.heap[index]>self.heap[pindex]:
            self.heap[index], self.heap[pindex] = self.heap[pindex], self.heap[index]
            index = pindex
            pindex = index // 2

    # floatowanie elementu z gory do opdowiedniej pozycji na dole
    def floatdown(self,index):
        lewy = index*2 # lewe dziecko indexu
        prawy = index * 2 + 1  # prawe dziecko indexu
        najwiekszy = index
        rozm = len(self.heap) - 1
        if rozm >= lewy and self.heap[lewy] > self.heap[index]:
            najwiekszy = lewy
        if rozm >= prawy and self.heap[prawy] > self.heap[index]:
            najwiekszy = prawy
        if najwiekszy != index:
            self.heap[index], self.heap[najwiekszy] = self.heap[najwiekszy], self.heap[index]
            self.floatdown(index)

    def usun_max(self):
        rozm = len(self.heap) - 1
        self.heap[1], self.heap[rozm] = self.heap[rozm], self.heap[1]
        self.floatdown(1)
        return self.heap.pop(rozm)

    def wprowadz(self, wprowadzona):
        self.heap.append(wprowadzona)
        self.floatup(len(self.heap)-1)

    def pokaz_max(self):
        return self.heap[1]

    def wypisz(self):
        return self.heap[1:]
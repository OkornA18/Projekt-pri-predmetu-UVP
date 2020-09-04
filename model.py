class Matrika:

    def __init__(self, matrika):
        self.matrika = matrika
        self.vrstice = len(matrika)
        self.stolpci = len(matrika[0])
    
    def __str__(self):
        mat = ""
        for vrstica in self.matrika:
            mat += str(vrstica) + '\n'
        return mat
    
    def __repr__(self):
        return "Matrika({0})".format(self.matrika)

    def __eq__(self, other):
        return self.matrika == other.matrika

    def __getitem__(self, indeks):
        return self.matrika[indeks]

    def __setitem__(self, indeks, item):
        self.matrika[indeks] = item

    def __add__(self, other):
        """ Ta funkcija sešteje kvadratni matriki po komponentah. """

        if  self.vrstice != self.stolpci or other.vrstice != other.stolpci:
            raise Exception("Si prepričan, da sta vpisani matriki kvadratni?")

        elif self.vrstice != other.vrstice or self.stolpci != other.stolpci:
            raise Exception("Matriki sta različnih velikosti!")

        else:
            m = self.vrstice
            n = self.stolpci
            vsota = []
            for i in range(m):
                vrstica = []
                for j in range(n):
                    vrstica.append(self.matrika[i][j] + other.matrika[i][j])
                vsota.append(vrstica)
            return Matrika(vsota)

    def __sub__(self, other):
        return self + (-1) * other

    def transponiraj(self):
        """Ta funkcija mi transponira drugo matriko pri množenju"""
        m = self.vrstice
        n = self.stolpci
        novamatrika = []
        for i in range(n):
            vrstica = []
            for j in range(m):
                vrstica.append(self[j][i])
            novamatrika.append(vrstica)
        return Matrika(novamatrika)

    def __mul__(self, other):
        """ Ta funkcija mi bo pomnožila dve kvadratni matriki """

        if  self.vrstice != self.stolpci or other.vrstice != other.stolpci:
            raise Exception("Si prepričan, da so vpisane matrike kvadratne?")

        elif self.vrstice != other.vrstice or self.stolpci != other.stolpci:
            raise Exception("Matriki sta različnih velikosti!")

        elif isinstance(other, Matrika):
            if self.stolpci == other.vrstice:
                transponiranka = other.transponiraj() 
                zmnozek = []
                m = self.vrstice
                n = self.stolpci
                for i in range(m):
                    vrstica = []
                    for j in range(n):
                        vrstica.append(sum([item[0] * item[1] for item in zip(self.matrika[i], transponiranka.matrika[j])]))
                    zmnozek.append(vrstica)
                return Matrika(zmnozek)
        else:
            raise Exception("Si prepričan da so velikosti/tipi pravilni?")
    
    def __rmul__(self, other):
        """Ta funkcija pri mojem odštevanju pomnoži drugo matriko, torej to, ki jo odštevam, s skalarjem -1"""
        if isinstance(other, int) or isinstance(other, float):
            zmnozek = []
            m = self.vrstice
            n = self.stolpci
            for i in range(m):
                vrstica = []
                for j in range(n):
                    vrstica.append(self[i][j] * other)
                zmnozek.append(vrstica)
            return Matrika(zmnozek)

    def sled(self):
        """ Izračuna vsoto diagonalnih elementov le kvadratnim matrikam. """
        if not self.vrstice == self.stolpci:
            raise Exception("Sled računamo le kvadratnim matrikam, zato preveri, ali si vpisal kvadratno matriko.")
        else:
            sled = 0
            for i in range(self.vrstice):
                sled += self[i][i]
            return sled
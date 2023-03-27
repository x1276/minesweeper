import random as rd

class player:

    class map:
        dimx, dimy = 30, 20
        dat = []

        for i in range(dimy):
            res = []
            for j in range(dimx):
                res.append(False)
            dat.append(res)

        def create(self):
            for i in range(self.dimy-1):
                for j in range(self.dimx-1):
                    if(rd.randint(0,5) == 5):
                        self.dat[i][j] = True

        def display(self):
            res = ""
            for y in range(len(self.dat)):
                for x in range(len(self.dat[y])):
                    if self.dat[y][x] == 1:
                        res += "{" + "M" + "}"
                    else:
                        res += "[" + str(self.cell.nom(self, x, y)) + "]"
                res += "\n"
            print(res)

        class cell:
            def nom(self, x, y):
                res = 0
                for i in range(-1,2,1):
                    for j in range(-1,2,1):
                        try:
                            if(self.dat[y+i][x+j]):
                                res += 1
                        except Exception: pass
                return res


if __name__ == '__main__':
    player.map.create(player.map)
    player.map.display(player.map)

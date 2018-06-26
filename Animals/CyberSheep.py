from Animals.Animal import Animal
#from World import World

class CyberSheep(Animal):
    def __init__(self , w , x , y):
        self.force=11
        self.world=w
        self.initiative=4
        self.position_x = x
        self.position_y=y
        self.type='C'
        print(self.position_x)



    def CreatMe(self  , x ,y):
        print("creat me")
        newOne=CyberSheep(self.world, x, y)
        return newOne;

    def EatMe(self , placeX, placeY, position_x, position_y):
        print("eat me")
        self.world.organisms.remove(self)

    def Action(self):
        if self.world.findBarszcz()!=None:
            print("akacja cyber oecy")
            print(self.position_x, self.position_y)
            tab = []
            index = 0
            size = self.world.organisms.__len__();
            for a in range(0, size):
                if self.world.organisms[a].type == 'K':
                    tab.append(a)
                    index = index + 1
            distance = 50000
            number = -1
            for i in range(0, index):
                if distance > self.WartoscBezwgledna(
                                self.position_x - self.world.organisms[tab[i]].position_x) + self.WartoscBezwgledna(
                                self.position_y - self.world.organisms[tab[i]].position_y):
                    distance = self.WartoscBezwgledna(
                        self.position_x - self.world.organisms[tab[i]].position_x) + self.WartoscBezwgledna(
                        self.position_y - self.world.organisms[tab[i]].position_y)
                    number = i

            if self.position_x > self.world.organisms[tab[number]].position_x:
                if self.CheckPosition((self.position_x - 1), self.position_y):
                    self.position_x = self.position_x - 1
                else:
                    self.Collision(self.position_x - 1, self.position_y)
            elif self.position_x < self.world.organisms[tab[number]].position_x:
                if self.CheckPosition((self.position_x + 1), self.position_y):
                    self.position_x = self.position_x + 1
                else:
                    self.Collision(self.position_x + 1, self.position_y)

            else:
                if self.position_y > self.world.organisms[tab[number]].position_y:
                    if self.CheckPosition((self.position_x), self.position_y - 1):
                        self.position_y = self.position_y - 1
                    else:
                        self.Collision(self.position_x, self.position_y - 1)

                else:
                    if self.CheckPosition((self.position_x), self.position_y + 1):
                        self.position_y = self.position_y + 1
                    else:
                        self.Collision(self.position_x, self.position_y + 1)
        else:
            super(CyberSheep , self).Action()



    def WartoscBezwgledna(selfe ,x):
        if x < 0:
            return -x
        else:
            return x

    def IsResistance(self):
        return 1
from Animals.Animal import Animal
#from World import World

class Human(Animal):
    def __init__(self , w , x , y):
        self.force=5
        self.world=w
        self.initiative=4
        self.position_x = x
        self.position_y=y
        self.type='H'
        self.coldown=0




    def CreatMe(self  , x ,y):
        print("creat me")
        newOne=Human(self.world, x, y)
        return newOne;

    def EatMe(self , placeX, placeY, position_x, position_y):
        print("eat me")
        self.world.organisms.remove(self)



    def Action(self):
        if self.coldown > 5:
            size = self.world.organisms.__len__();
            x = self.position_x
            y = self.position_y
            tab = []
            for i in range(0, 6):
                tab.append(0)
            index = 0
            #spr=0
            for a in range(0, size):
                if self.world.organisms[a].position_x == x + 1 and self.world.organisms[a].position_y == y :
                  #  if isinstance(self.world.organisms[a], Animal):
                        print("killl")
                        tab[index] = a
                        index = index + 1
                elif self.world.organisms[a].position_x == x - 1 and self.world.organisms[a].position_y == y:
                  #  if isinstance(self.world.organisms[a], Animal):
                        print("killl")
                        tab[index] = a
                        index = index + 1
                elif self.world.organisms[a].position_x == x and self.world.organisms[a].position_y == y - 1:
                   # if isinstance(self.world.organisms[a], Animal):
                        print("killl")
                        tab[index] = a
                        index = index + 1
                elif self.world.organisms[a].position_x == x and self.world.organisms[a].position_y == y + 1:
                   # if isinstance(self.world.organisms[a], Animal):
                        print("killl")
                        tab[index] = a
                        index = index + 1
            for i in range(0, 4):
                for j in range(0, 4):
                    if tab[i] < tab[i + 1]:
                        t = tab[i + 1]
                        tab[i + 1] = tab[i]
                        tab[i] = t
            for t in range(0, index):
                print(self.world.organisms[tab[t]].type + "zostal zabity przez czlowieka")
                self.world.organisms.remove(self.world.organisms[tab[t]])
        if self.coldown > 0:
            self.coldown=self.coldown-1



    def setY(self , y):
        if y>0:
            if self.position_y<self.world.height-1:
                if super(Human , self).CheckPosition(self.position_x , self.position_y+y):
                    self.position_y=self.position_y+y
                else:
                    super(Human, self).Collision(self.position_x , self.position_y+y)
        else:
            if self.position_y>0:
                if super(Human , self).CheckPosition(self.position_x, self.position_y + y):
                    self.position_y = self.position_y + y
                else:
                    super(Human, self).Collision(self.position_x, self.position_y + y)


    def setX(self , x):
        if x>0:
            if self.position_x<self.world.width-1:
                if super(Human , self).CheckPosition(self.position_x +x, self.position_y):
                    self.position_x=self.position_x+x
                else:
                    super(Human, self).Collision(self.position_x +x, self.position_y)
        else:
            if self.position_x>0:
                if super(Human , self).CheckPosition(self.position_x+x, self.position_y ):
                    self.position_x = self.position_x+x
                else:
                    super(Human, self).Collision(self.position_x+x, self.position_y)


    def powerOn(self):
        if self.coldown==0:
            self.coldown=10
        else:
            print("poczekaj jeszcze troche")

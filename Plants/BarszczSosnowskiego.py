import types

from Plant import Plant
from Animals.Animal import Animal



class BarszczSosnowksiego(Plant):
    def __init__(self , w , x , y):
        self.force=10
        self.world=w
        self.initiative=0
        self.position_x = x
        self.position_y=y
        self.type='K'
        print(self.position_x)



    def CreatMe(self  , x ,y):
        print("creat me")
        newOne=BarszczSosnowksiego(self.world, x, y)
        return newOne;

    def EatMe(self , placeX, placeY, position_x, position_y):
        print("eat me")
        self.world.organisms.remove(self)

    def Action(self):
        self.KillAll()
        super(BarszczSosnowksiego , self).Action()

    def KillAll(self):
      #  print("spr kogo zabil")
        size = self.world.organisms.__len__();
        x = self.position_x
        y = self.position_y
        tab = []
        for i in range(0,6):
            tab.append(0)
        index=0
        for a in range(0, size):
            if self.world.organisms[a].position_x==x+1 and self.world.organisms[a].position_y==y:
                if isinstance(self.world.organisms[a], Animal):
                    print("killl")
                    tab[index]=a
                    index=index+1
            elif self.world.organisms[a].position_x==x-1 and self.world.organisms[a].position_y==y:
                if isinstance(self.world.organisms[a], Animal):
                    print("killl")
                    tab[index] = a
                    index = index + 1
            elif self.world.organisms[a].position_x==x and self.world.organisms[a].position_y==y-1:
                if isinstance(self.world.organisms[a], Animal):
                    print("killl")
                    tab[index] = a
                    index = index + 1
            elif self.world.organisms[a].position_x==x and self.world.organisms[a].position_y==y+1:
                if isinstance(self.world.organisms[a], Animal):
                    print("killl")
                    tab[index] = a
                    index = index + 1
        for i in range(0 ,4):
            for j in range(0,4):
                if tab[i]<tab[i+1]:
                    t=tab[i+1]
                    tab[i+1]=tab[i]
                    tab[i]=t
        for t in range(0 , index):
            if self.world.organisms[tab[t]].IsResistance():
                print("cyber owca zaraz zje barszcz")
            else:
                print(self.world.organisms[tab[t]].type + "zostal zabity przez barszcz sosnowskiego")
                self.world.organisms.remove(self.world.organisms[tab[t]])
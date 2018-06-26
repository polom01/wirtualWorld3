import random

from Organism import Organism


class Animal(Organism):


    def __init__(self):
        print("konstruktor nr 2")


    def Skills(self, x,y):
        print("skills Animal")
        return 1



    def Action(self):
        number = random.randint(0 , 3)
        print("Action Animeal")

        if number == 0:
            if self.CheckPosition((self.position_x - 1), self.position_y):
                if self.position_x > 0:
                    self.position_x=self.position_x-1
            else:
                self.Collision(self.position_x - 1, self.position_y)

        if number == 1:
            if self.CheckPosition((self.position_x), self.position_y+1):
                if self.world.height-1 > self.position_y:
                    self.position_y=self.position_y+1
            else:
                self.Collision(self.position_x, self.position_y+1)

        if number == 2:
            if self.CheckPosition((self.position_x+1), self.position_y):
                if self.world.width-1 > self.position_x:
                    self.position_x=self.position_x+1
            else:
                self.Collision(self.position_x+1, self.position_y)

        if number == 3:
            if self.CheckPosition((self.position_x), self.position_y-1):
                if 0 < self.position_y:
                    self.position_y=self.position_y-1
            else:
                self.Collision(self.position_x, self.position_y-1)






    def Collision(self,x, y):
        for a in range(0, self.world.organisms.__len__()):
            if self.world.organisms[a].position_x == x and self.world.organisms[a].position_y == y:
                print(self.type , self.world.organisms[a].type )
                if (self.world.organisms[a].type == self.type):
                    self.NewAnimal(x, y)
                    break
                else:
                    self.Fight(x, y)
                    break



#ok
    def NewAnimal(self,PositionXParent,PositionYParent):

        NewPositionX = -1;
        NewPositionY = -1;
        count = 0;
        number = random.randrange(2) - 1
        if PositionYParent==self.position_y:
            if self.position_x>PositionXParent:
                if self.CheckPosition((self.position_x+1), self.position_y)and self.position_y <self.world.height-1:
                    self.world.organisms.append(self.CreatMe(self.position_x+1 , self.position_y))
                    return
                elif  self.CheckPosition((self.position_x), self.position_y+1)and self.position_x >0:
                    self.world.organisms.append(self.CreatMe(self.position_x , self.position_y+1))
                    return
                elif self.CheckPosition((self.position_x), self.position_y -1)and self.position_y>0:
                    self.world.organisms.append(self.CreatMe(self.position_x, self.position_y -1))
                    return
            else:
                if self.CheckPosition((PositionXParent + 1), self.position_y) and self.position_x <self.world.width-1:
                    self.world.organisms.append(self.CreatMe(PositionXParent + 1, self.position_y))
                    #self.world.set_organisms(self.CreatMe(PositionXParent + 1, self.position_y))
                    return
                elif self.CheckPosition((PositionXParent), self.position_y + 1) and self.position_x >0:
                    self.world.organisms.append(self.CreatMe(PositionXParent, self.position_y + 1))
                    #self.world.set_organisms(self.CreatMe(PositionXParent, self.position_y + 1))
                    return
                elif self.CheckPosition((PositionXParent), self.position_y - 1)and self.position_y < self.world.height-1:
                    self.world.organisms.append(self.CreatMe(PositionXParent, self.position_y - 1))
                  #  self.world.set_organisms(self.CreatMe(PositionXParent, self.position_y - 1))
                    return

        elif PositionXParent==self.position_x:
            if self.position_y > PositionYParent:
                if self.CheckPosition((self.position_x + 1), self.position_y) and self.position_y <self.world.height-1:
                    self.world.organisms.append(self.CreatMe(self.position_x + 1, self.position_y))
                    return
                elif self.CheckPosition((self.position_x -1 ), self.position_y ) and self.position_x >0:
                    self.world.organisms.append(self.CreatMe(self.position_x-1 , self.position_y))
                    return
                elif self.CheckPosition((self.position_x), self.position_y + 1) and self.position_y>0 :
                    self.world.organisms.append(self.CreatMe(self.position_x, self.position_y + 1))
                    return
            else:
                if self.CheckPosition((self.position_x + 1), PositionYParent) and self.position_x <self.world.width-1:
                    self.world.organisms.append(self.CreatMe(self.position_x + 1, PositionYParent))
                    return
                elif self.CheckPosition((self.position_x -1 ), PositionYParent ) and self.position_x >0:
                    self.world.organisms.append(self.CreatMe(self.position_x-1 , PositionYParent))
                    return
                elif self.CheckPosition((self.position_x), PositionYParent + 1) and self.position_y < self.world.height-1:
                    self.world.organisms.append(self.CreatMe(self.position_x, PositionYParent + 1))
                    return





    def Fight(self,placeX,placeY):
        size = self.world.organisms.__len__()
        for organism_ in self.world.organisms:
         #   print( organism_.position_x,  organism_.position_y )
            if organism_.position_x == placeX and  organism_.position_y == placeY:
                if organism_.Skills(self.position_x , self.position_y):
                    if organism_.force<self.force:
                        organism_.EatMe(placeX, placeY, self.position_x, self.position_y);
                        self.position_x = placeX;
                        self.position_y = placeY;
                        break
                    else:
                        self.EatMe(placeX , placeY ,self.position_x , self.position_y )
                        break

  #  def CreatMe(self , position_x , position_y):
   #     pass


    def CheckPosition(self , x , y):
        for a in range( 0, self.world.organisms.__len__()):
          if self.world.organisms[a].position_x == x and  self.world.organisms[a].position_y == y:
             return 0
        return 1

    def IsResistance(self):
        return 0
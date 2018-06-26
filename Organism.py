#from World import World
class Organism:


    def __init__(self ,w):
        print("konstruktor organismu")
        self.world=w
        self.force = -1
        self.initiative = -1
        self.position_x = -1
        self.position_y = -1
        self.type='N'


    def  Action(self):
        pass
    def SetWorld(self , wor):
        self.world=wor
    def Collision(self, x,  y):
        pass
    def EatMe(self,x, y, EaterX, EaterY):
        pass
    def Skills(self, o):
        pass

    def CheckPosition(self , x , y):
        for a in range( 0, self.world.organisms.__len__()):
          if self.world.organisms[a].position_x == x and self.world.organisms[a].position_y == y:
             return 0
        return 1


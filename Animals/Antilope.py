import random
from Animals.Animal import Animal
#from World import World

class Antilope(Animal):
    def __init__(self , w , x , y):
        self.force=4
        self.world=w
        self.initiative=4
        self.position_x = x
        self.position_y=y
        self.type='A'
        print(self.position_x)



    def CreatMe(self  , x ,y):
        print("creat me")
        newOne=Antilope(self.world, x, y)
        return newOne;

    def EatMe(self , placeX, placeY, position_x, position_y):
        print("eat me")
        self.world.organisms.remove(self)
    def Action(self):
        self.goto=2
        super(Antilope, self).Action()

    def Skills(self , x,y):
        number = random.randint(0, 3)
        if number == 0:
            PlaceX = x
            PlaceY = y
            org=self.world.get_organism_by_xy(x,y)
            org.position_x=self.position_x
            org.position_y = self.position_y
            self.position_x=PlaceX
            self.position_y=PlaceY
            return 0
        return 1


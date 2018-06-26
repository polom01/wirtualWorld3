import random

from Animals.Animal import Animal
#from World import World

class Turtle(Animal):
    def __init__(self , w , x , y):
        self.force=2
        self.world=w
        self.initiative=1
        self.position_x = x
        self.position_y=y
        self.type='T'
        print(self.position_x)



    def CreatMe(self  , x ,y):
        print("creat me")
        newOne=Turtle(self.world, x, y)
        return newOne;

    def EatMe(self , placeX, placeY, position_x, position_y):
        print("eat me")
        self.world.organisms.remove(self)

    def Skills(self , x,y):
        if self.world.get_organism_by_xy(x,y).force < 5:
            return 0
        return 1

    def Action(self):
        number=random.randint(0 , 2)
        if number==0:
            super(Turtle , self).Action()

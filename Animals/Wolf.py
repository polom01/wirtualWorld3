from Animals.Animal import Animal
#from World import World

class Wolf(Animal):
    def __init__(self , w , x , y):
        self.force=9
        self.world=w
        self.initiative=5
        self.position_x = x
        self.position_y=y
        self.type='W'



    def CreatMe(self  , x ,y):
        print("creat me")
        newOne=Wolf(self.world, x, y)
        return newOne;

    def EatMe(self , placeX, placeY, position_x, position_y):
        self.world.organisms.remove(self)

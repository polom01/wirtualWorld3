from Animals.Animal import Animal
#from World import World

class Sheep(Animal):
    def __init__(self , w , x , y):
        self.force=4
        self.world=w
        self.initiative=4
        self.position_x = x
        self.position_y=y
        self.type='S'
        print(self.position_x)



    def CreatMe(self  , x ,y):
        print("creat me")
        newOne=Sheep(self.world, x, y)
        return newOne;

    def EatMe(self , placeX, placeY, position_x, position_y):
        print("eat me")
        self.world.organisms.remove(self)


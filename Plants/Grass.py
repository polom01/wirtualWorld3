from Plant import Plant




class Grass(Plant):
    def __init__(self , w , x , y):
        self.force=0
        self.world=w
        self.initiative=0
        self.position_x = x
        self.position_y=y
        self.type='G'
        print(self.position_x)



    def CreatMe(self  , x ,y):
        print("creat me")
        newOne=Grass(self.world, x, y)
        return newOne;

    def EatMe(self , placeX, placeY, position_x, position_y):
        print("eat me")
        self.world.organisms.remove(self)


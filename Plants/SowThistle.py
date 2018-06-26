from Plant import Plant




class SowThistle(Plant):
    def __init__(self , w , x , y):
        self.force=0
        self.world=w
        self.initiative=0
        self.position_x = x
        self.position_y=y
        self.type='U'
        print(self.position_x)



    def CreatMe(self  , x ,y):
        print("creat me")
        newOne=SowThistle(self.world, x, y)
        return newOne;

    def EatMe(self , placeX, placeY, position_x, position_y):
        print("eat me")
        self.world.organisms.remove(self)

    def Action(self):
        for a in range(0 ,3 ):
            super(SowThistle , self).Action()

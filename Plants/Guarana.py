from Plant import Plant




class Guarana(Plant):
    def __init__(self , w , x , y):
        self.force=0
        self.world=w
        self.initiative=0
        self.position_x = x
        self.position_y=y
        self.type='U'
        print(self.position_x)



    def CreatMe(self  , x ,y):
     #   print("creat me")
        newOne=Guarana(self.world, x, y)
        return newOne;

    def EatMe(self , placeX, placeY, EaterX, EaterY):
        print("eat me , i m Guarana")
        self.world.organisms.remove(self)

        size = self.world.organisms.__len__()

        for a in range(0,size):
            if self.world.organisms[a].position_x == EaterX and self.world.organisms[a].position_y == EaterY:
                self.world.organisms[a].force=self.world.organisms[a].force+3
                break




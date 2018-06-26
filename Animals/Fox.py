from Animals.Animal import Animal
#from World import World

class Fox(Animal):
    def __init__(self , w , x , y):
        self.force=3
        self.world=w
        self.initiative=7
        self.position_x = x
        self.position_y=y
        self.type='L'
        print(self.position_x)



    def CreatMe(self  , x ,y):
        print("creat me")
        newOne=Fox(self.world, x, y)
        return newOne;

    def EatMe(self , placeX, placeY, position_x, position_y):
        print("eat me")
        self.world.organisms.remove(self)

    def Collision(self,x, y):
        size=self.world.organisms.__len__()
        for a in range(0 , size):
            if self.world.organisms[a].position_x==x and self.world.organisms[a].position_y==y:
                if self.world.organisms[a].type==self.type:
                    self.NewAnimal(x,y)
                    break
                else:
                    if self.world.organisms[a].force<=self.force:
                        super(Fox, self).Fight(x,y)
                    else:
                        print("lis uniknal walki")
                        break
            if size > self.world.organisms.__len__():
                break
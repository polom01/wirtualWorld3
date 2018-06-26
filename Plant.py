from Organism import Organism
import random
class Plant(Organism):
    def Action(self):
        number = random.randint(0, 3)
     #   print("Action Plant")
        if number == 0:
            number = random.randint(0, 3)
            if number==0:
                if self.CheckPosition((self.position_x - 1), self.position_y):
                    if self.position_x>0:
                        self.world.organisms.append(self.CreatMe(self.position_x - 1, self.position_y))
            elif number==1:
                if self.CheckPosition(self.position_x, self.position_y + 1):
                    if self.position_y < self.world.height- 1:
                        self.world.organisms.append(self.CreatMe(self.position_x , self.position_y+1))
            elif number==2:
                if self.CheckPosition(self.position_x, self.position_y - 1):
                    if self.position_y >0:
                        self.world.organisms.append(self.CreatMe(self.position_x , self.position_y-1))
            elif number==3:
                if self.CheckPosition(self.position_x+1, self.position_y ):
                    if self.position_x<self.world.width- 1:
                        self.world.organisms.append(self.CreatMe(self.position_x +1, self.position_y))






    def CreatMe(self , position_x , position_y):
          pass

    def Skills(self , x , y):
        print("skills Animal")
        return 1
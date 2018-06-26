import sys

import pickle

from Animals.Antilope import Antilope
from Animals.CyberSheep import CyberSheep
from Animals.Fox import Fox
from Animals.Human import Human
from Animals.Sheep import Sheep
from Animals.Turtle import Turtle
from Animals.Wolf import Wolf
from Plants.Guarana import Guarana
from Plants.SowThistle import SowThistle
from Plants.WolfBerry import WolfBerry
from Plants.BarszczSosnowskiego import BarszczSosnowksiego

class World:
    organisms=[]
    map=[]
    def pri(self):
        print("class funcion world")

    def __init__(self):
        print("konstruktor World")
        self.organisms=[]
        self.map=[]
        self.height=20
        self.width=20
    def get_organism_by_xy(self, x, y):
        for tmporganism in self.organisms:
            if tmporganism.position_x== x and tmporganism.position_y == y:
                return tmporganism
        return None

    def set_organisms(self, new_organisms):
        self.organisms = new_organisms

    def delete_organism(self, organism):
        try:
            self.organisms.remove(organism)
        except ValueError:
            pass


    def DrawWorld(self):
        for a in range(0,self.height+2):
            for b in range(0, self.width+2):
                spr=0
                if a==0 or b==0 or a==self.height+1 or b==self.width + 1:
                    sys.stdout.write('X')
                else:
                    if self.get_organism_by_xy(b,a) !=None:
                        sys.stdout.write(self.get_organism_by_xy(b,a).type)
                    else:
                        sys.stdout.write(' ')

            print()

    def DoTour(self):
        size=self.organisms.__len__()
        print(size)
        for a in range(0 , size):
            if a >= self.organisms.__len__():
                break
            #print(self.organisms[a].position_x , self.organisms[a].position_y)
            self.organisms[a].Action()



    def findHuman(self):
        for tmporganism in self.organisms:
            if tmporganism.type=='H':
                return tmporganism
        return None


    def findBarszcz(self):
        for tmporganism in self.organisms:
            if tmporganism.type=='K':
                return tmporganism
        return None



    def makeMap(self):
        self.map=[]
        for i in range(0,20):
            for j in range(0 ,20):
                if self.get_organism_by_xy(j,i)==None:
                    self.map.append(" ")
                else:
                    self.map.append(self.get_organism_by_xy(j,i).type)


    def save(self):
        file = open("savedWorld.txt", "w")
        file.write(str(self.organisms.__len__()))
        file.write(" ")
        for org in self.organisms:
            file.write(org.type)
            file.write(" ")
            if org.position_x<10:
                file.write(" ")
            file.write(str(org.position_x) )
            file.write(" ")
            if org.position_y <10:
                file.write(" ")
            file.write(str(org.position_y))
            file.write(" ")
            if org.force <10:
                file.write(" ")
            file.write(str(org.force))
            file.write(" ")
            file.write(str(org.initiative))
            file.write(" ")
            if org.type=='H':
                if org.coldown <10:
                    file.write(" ")
                file.write(str(org.coldown))
                file.write(" ")





    def load(self):
        self.organisms=[]
        file = open("savedWorld.txt", "r")
        index=2
        self.string=file.readline(index)
        self.string = self.string.strip()
        count=int(self.string)

      #  for a in range(0, count):
        #    print(file.readline(index))
        #


        for a in range(0,count):
            index = 2
            self.string = file.readline(index)
            self.string = self.string.strip()
            type_=self.string
            index = 3
            self.string = file.readline(index)
            print(self.string)

            self.string = self.string.strip()
            poz_x=int(self.string)

            self.string = file.readline(index)

            self.string = self.string.strip()
            poz_y = int(self.string)

            self.string = file.readline(index)
            index=2
            self.string = self.string.strip()
            force_= int(self.string)

            self.string = file.readline(index)

            self.string = self.string.strip()
            ini = int(self.string)
            if type_=='H':
                index=3
                self.organisms.append(Human(self , poz_x ,poz_y))
                self.string = file.readline(index)

                self.string = self.string.strip()
                coll = int(self.string)
                self.get_organism_by_xy(poz_x, poz_y).coldown=coll
            elif type_=='A':
                self.organisms.append(Antilope(self, poz_x, poz_y))
            elif type_ == 'W':
                self.organisms.append(Wolf(self, poz_x, poz_y))
            elif type_ == 'B':
                self.organisms.append(WolfBerry(self, poz_x, poz_y))
            elif type_ == 'L':
                self.organisms.append(Fox(self, poz_x, poz_y))
            elif type_ == 's':
                self.organisms.append(Sheep(self, poz_x, poz_y))
            elif type_ == 'Z':
                self.organisms.append(Turtle(self, poz_x, poz_y))
            elif type_ == 'K':
                self.organisms.append(BarszczSosnowksiego(self, poz_x, poz_y))
            elif type_ == 'U':
                self.organisms.append(Guarana(self, poz_x, poz_y))
            elif type_ == 'O':
                self.organisms.append(SowThistle(self, poz_x, poz_y))
            elif type_ == 'C':
                self.organisms.append(CyberSheep(self, poz_x, poz_y))
            if   self.get_organism_by_xy(poz_x, poz_y)!=None:
                self.get_organism_by_xy(poz_x, poz_y).force = force_
                self.get_organism_by_xy(poz_x, poz_y).initiative = ini




    def Killnewline(self, adress_list):
        for x in range(len(adress_list)):
                adress_list[x].replace(' ', '')

        return adress_list
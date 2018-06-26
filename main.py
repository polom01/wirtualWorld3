#from Animals.Animal import Animal
from Animals.CyberSheep import CyberSheep
from Animals.Human import Human
from Animals.Sheep import Sheep
from Animals.Fox import Fox
from Animals.Antilope import Antilope
from Animals.Turtle import Turtle
from Frame import Frame
from World import World
from Animals.Wolf import Wolf
from Plants.Grass import Grass
from Plants.Guarana import Guarana
from Plants.SowThistle import SowThistle
from Plants.BarszczSosnowskiego import BarszczSosnowksiego

print("ok")

#y= Animal()
#x=World()
#
#s.createMe(x ,4 ,4);

WORLD=World()
s=CyberSheep(WORLD , 3 ,4)
WORLD.organisms.append(s)
s=Human(WORLD , 13 ,14)
WORLD.organisms.append(s)
s=BarszczSosnowksiego(WORLD , 10 ,10)
WORLD.organisms.append(s)
#WORLD.save()

s=Fox(WORLD , 3 ,4)
WORLD.organisms.append(s)
s=Sheep(WORLD , 11 ,4)
#WORLD.organisms.append(s)
s=Turtle(WORLD , 13 ,4)
WORLD.organisms.append(s)
s=Wolf(WORLD , 7 ,4)
WORLD.organisms.append(s)

s=SowThistle(WORLD , 14 ,4)
WORLD.organisms.append(s)
F=Frame(WORLD)

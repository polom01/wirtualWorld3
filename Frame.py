import pygame
import sys


class Frame(object):
    def __init__(self , world):
        pygame.init()
        self.FrameWorld=world
        screen = pygame.display.set_mode((900, 500))
        done = False
        self.FrameWorld.makeMap()
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    if self.FrameWorld.findHuman() != None:
                        self.FrameWorld.findHuman().setY(1)
                    self.FrameWorld.DoTour()
                    self.FrameWorld.makeMap()

                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    if self.FrameWorld.findHuman() != None:
                        self.FrameWorld.findHuman().setY(-1)
                    self.FrameWorld.DoTour()
                    self.FrameWorld.makeMap()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    print("down")
                    if self.FrameWorld.findHuman() != None:
                        self.FrameWorld.findHuman().setX(-1)
                    self.FrameWorld.DoTour()
                    self.FrameWorld.makeMap()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    print("right")
                    if self.FrameWorld.findHuman()!=None:
                        self.FrameWorld.findHuman().setX(1)
                    self.FrameWorld.DoTour()
                    self.FrameWorld.makeMap()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    self.FrameWorld.save()
                    self.FrameWorld.makeMap()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                    print("load")
                    self.FrameWorld.load()
                    self.FrameWorld.makeMap()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    print("power")
                    self.FrameWorld.findHuman().powerOn()
                    self.FrameWorld.findHuman().Action()
                    self.FrameWorld.makeMap()


            x = 0
            y = 1

            for a in range(0, 400):
                x = x + 1
                if x == 21:
                    y = y + 1
                    x = 1
                pygame.draw.rect(screen, self.takeColor(self.FrameWorld.map[a]),
                                 pygame.Rect(20 * x, 20 * y, 30, 30))  #10 10 20 20
            pygame.display.flip()









    def takeColor(self , sign):

        if sign == 'A':
            return (184, 183, 153)
        elif sign == 'W':
            return (198, 166, 100)
        elif sign=='B':
            return (255, 117, 20)
        elif sign=='L':
            return (120,120,120)
        elif sign=='S':
            return (34, 113, 179)
        elif sign=='H':
            return (123,123,123)
        elif sign=='Z':
            return (160, 52, 114)
        elif sign=='K':
            return (53, 104, 45)
        elif sign=='G':
            return (10, 52, 114)
        elif sign=='U':
            return (230, 50, 68)
        elif sign=='O':
            return (28, 50, 68)
        elif sign=='C':
            return (234 , 34, 100)
        else:
            return (255,255,255)


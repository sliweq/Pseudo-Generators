import pygame
from Points import Points
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class Main():
    # parameters for pseudonumber generator is in file Points.py
    def __init__(self, points):
        self.points = points
    
    def run():
        pass
    
if(__name__ == "__main__"):
    points = []
    #main = Main(points)
    p = Points(100)
    p.createRandomPoints()
    print(p.getPointsArray())
    
    
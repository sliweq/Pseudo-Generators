import pygame
from Points import Points
from pygame.locals import *

from Settings import Settings
from Gui import Gui

from OpenGL.GL import *
from OpenGL.GLU import *

class Main():
    def __init__(self, points,settings):
        self.settings = settings
        self.points = points
        self.axiX = [((settings.axes_lenght/2),0,0),(-(settings.axes_lenght/2),0,0)]
        self.axiY = [(0,(settings.axes_lenght/2), 0),(0,-(settings.axes_lenght/2),0)]
        self.axiZ = [(0,0,(settings.axes_lenght/2)),(0,0,-(settings.axes_lenght/2))]
        
        self.moves_x = 0
        self.moves_y = 0
        self.moves_z = 0
       
        self.rotate_x = 0
        self.rotate_y = 0
        self.rotate_z = 0
        
    
    def drawAxis(self):
        glBegin(GL_LINES)
        glColor3f(self.settings.color[self.settings.axes_color][0],self.settings.color[self.settings.axes_color][1],self.settings.color[self.settings.axes_color][2])
        glVertex3fv(self.axiX[0])
        glVertex3fv(self.axiX[1])
        glVertex3fv(self.axiY[0])
        glVertex3fv(self.axiY[1])
        glVertex3fv(self.axiZ[0])
        glVertex3fv(self.axiZ[1])
        glEnd()
        glFlush()
    
    def drawPoints(self):
        glColor3f(self.settings.color[self.settings.points_color][0],self.settings.color[self.settings.points_color][1],self.settings.color[self.settings.points_color][2]) 
        glBegin(GL_POINTS)
        for point in self.points:
            glVertex3fv(point)    
        glEnd()
        glFlush()
    
    def run(self):
        pygame.init()
        pygame.display.set_mode((800,600), OPENGL|DOUBLEBUF)
        pygame.display.set_caption("Pseudo Random Number Generator")
        
        gluPerspective(100,(800/600),0.1,3000.0) 
        glTranslatef(-200,-100,-500)
        glEnable(GL_DEPTH_TEST)
                
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    self.keyPressed(event)
                if event.type == pygame.KEYUP:
                    self.keyRelased(event)
                   
            glTranslatef(self.moves_y,self.moves_z,self.moves_x)
            
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            
            #glRotatef(1,self.rotate_y, self.rotate_z, self.rotate_x)
            glRotatef(self.rotate_y, 1, 0, 0)  # Obrót wokół osi X
            glRotatef(self.rotate_z, 0, 1, 0)  # Obrót wokół osi Y
            glRotatef(self.rotate_x, 0, 0, 1)  # Obrót wokół osi Z
            self.drawAxis()
            self.drawPoints()
            
            
            pygame.display.flip()
            pygame.time.wait(settings.speed)

            
    
    def keyPressed(self,event):
        # camera moves
        if event.key == pygame.K_a:
            self.moves_y  = -1
        if event.key == pygame.K_d:
            self.moves_y = 1
        if event.key == pygame.K_s:
            self.moves_x = 1
        if event.key == pygame.K_w:
            self.moves_x = -1
        if event.key == pygame.K_LSHIFT:
            self.moves_z = -1
        if event.key == pygame.K_SPACE:
            self.moves_z = 1 

        # camera rotations
        
        if event.key == pygame.K_LEFT:
            self.rotate_z = 1
        if event.key == pygame.K_RIGHT:
            self.rotate_z = -1
        if event.key == pygame.K_UP:
            self.rotate_y = 1
        if event.key == pygame.K_DOWN:
            self.rotate_y = -1
            
        if event.key == pygame.K_q:
            pygame.quit()
            quit()


    def keyRelased(self,event):
        # moves
        if event.key == pygame.K_a:
            self.moves_y  = 0
        if event.key == pygame.K_d:
            self.moves_y = 0
        if event.key == pygame.K_s:
            self.moves_x = 0
        if event.key == pygame.K_w:
            self.moves_x = 0
        if event.key == pygame.K_LSHIFT:
            self.moves_z = 0
        if event.key == pygame.K_SPACE:
            self.moves_z = 0 
        # rotations
        if event.key == pygame.K_LEFT:
            self.rotate_z = 0
        if event.key == pygame.K_RIGHT:
            self.rotate_z = 0
        if event.key == pygame.K_UP:
            self.rotate_y = 0
        if event.key == pygame.K_DOWN:
            self.rotate_y = 0
            
    
if(__name__ == "__main__"):
    settings = Settings()
    g = Gui(settings)
    tmp = g.run()
    
    if(tmp != None):
        points = []
        p = Points(settings.points_amount,tmp)
        points = p.getPointsArray()
        print(points)
        main = Main(points,settings)
        
        main.run()
    
    
    
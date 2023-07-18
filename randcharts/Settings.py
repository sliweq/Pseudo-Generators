class Settings():
    def __init__(self):
        #default sttings
        self.points_amount = 1
        self.axes_lenght = 2000
        self.speed = 10 #1-15 (1 - the fastest/ 15 - the slowest)
        
        self.color =[(0,0,0),(0,1,0),(1,1,0),(1,0,0),(0,0,1),(1,0,1)]
        
        self.axes_color = 0 #0-white 1-green 2-yellow 3-red 4-blue 5-purple
        
        self.points_color = 1 #0-white 1-green 2-yellow 3-red 4-blue 5-purple
        
    def set_points_color(self, color):
        self.points_color = color
        
    def set_axes_color(self, color):
        self.axes_color = color
        
    def set_speed(self, speed):
        self.speed = speed
    
    def set_axes_length(self, length):
        self.axes_lenght = length
    
    def set_points_amount(self, amount):
        self.points_amount = amount
        
class Points():
    def __init__(self, amount) -> None:
        self.points = []
        self.amount = amount
    
    def getRandomNumber(self, x):
        m = 1000 #the modulus
        a = 2 # the multiplier 
        c = 0 # the increment
        seed = 69 
        
        if(x == None):
            return ((a*seed + c)%m)
        else: 
            return ((a*x + c)%m) 
        
    def createRandomPoints(self):
        x = None
        for i in range(0,self.amount):
            tmp1 = self.getRandomNumber(x)
            tmp2 = self.getRandomNumber(tmp1)
            tmp3 = self.getRandomNumber(tmp2)
            x = tmp3
            self.points.append((tmp1,tmp2,tmp3))
            
    def getPointsArray(self):
        return self.points
            
            
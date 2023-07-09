class Points():
    def __init__(self, amount):
        self.points = []
        self.amount = amount
    
    def linearCongruentialGenerator(self, x):
        m = 257  #the modulus
        a = 75 # the multiplier 
        c = 74 # the increment
        seed = 2 
        
        if(x == None):
            return ((a*seed + c)%m)
        else: 
            return ((a*x + c)%m) 
        
    def createRandomPoints(self):
        x = None
        for i in range(0,self.amount):
            tmp1 = self.linearCongruentialGenerator(x)
            tmp2 = self.linearCongruentialGenerator(tmp1)
            tmp3 = self.linearCongruentialGenerator(tmp2)
            x = tmp3
            self.points.append((tmp1,tmp2,tmp3))
            
    def getPointsArray(self):
        self.createRandomPoints()
        return self.points
            
            
class Points():
    def __init__(self, amount, option, modulo, a, c, seed):
        self.points = []
        self.amount = int(amount)
        self.option = option
        self.modulo = modulo
        self.a = a #in middle square it is used as number of digits #j
        self.c = c #k
        self.seed = seed
            
    def getPointsArray(self):
        self.points.clear()
        match self.option:
            case 1:
                self.create1()
            case 2:
                self.create2()
            case 3: 
                self.create3()
            case 4:
                self.create4()
        self.points = list(set(self.points))
        return self.points
            
    #option 1
    def linearCongruentialGenerator(self, x):
        return ((self.a*x + self.c)%self.modulo) 
        
    def create1(self):
        self.seed = int(self.seed)
        self.a = int(self.a)
        self.c = int(self.c)
        self.modulo = int(self.modulo)
        
        x = self.seed 
        for i in range(0,self.amount):
            tmp1 = self.linearCongruentialGenerator(x)
            tmp2 = self.linearCongruentialGenerator(tmp1)
            tmp3 = self.linearCongruentialGenerator(tmp2)
            x = tmp3
            self.points.append((tmp1,tmp2,tmp3))
            
    #option2
    def middleSquaregenerator(self, x):
        tmp = x**2
        if(len(str(tmp)) >= self.a):
            tmp = str(tmp)
            return int(tmp[(len(tmp)-self.a)//2:(((len(tmp)-self.a)//2)+self.a)])
        else:
            return tmp
    
    def create2(self):
        self.seed = int(self.seed)
        self.amount = int(self.amount)
        self.a = int(self.a)
        
        x = self.seed
        for i in range(0,self.amount):
            tmp1 = self.middleSquaregenerator(x)
            tmp2 = self.middleSquaregenerator(tmp1)
            tmp3 = self.middleSquaregenerator(tmp2)
            x = tmp3
            self.points.append((tmp1,tmp2,tmp3))
    
    #option3
    def create3(self):
        self.seed = int(self.seed)  
        self.a = int(self.a)
        self.modulo = int(self.modulo)
        
        
        
        x = self.seed
        for i in range(0,self.amount):
            tmp1 = self.lehmerCongruentialGenerator(x)
            tmp2 = self.lehmerCongruentialGenerator(tmp1)
            tmp3 = self.lehmerCongruentialGenerator(tmp2)
            x = tmp3
            self.points.append((tmp1,tmp2,tmp3))
            
    def lehmerCongruentialGenerator(self,x):
        return ((self.a*x)%self.modulo) 
        
    #option4
    def create4(self):
        self.seed = int(self.seed)
        self.a = int(self.a)
        self.c = int(self.c)
        self.modulo = int(self.modulo)
        
        x = [int(i) for i in str(self.seed)] 
        for i in range(0,self.amount):
            tmp1 = self.laggedFibonacciGenerator(x)
            tmp2 = self.laggedFibonacciGenerator(tmp1[1])
            tmp3 = self.laggedFibonacciGenerator(tmp2[1])
            x = tmp3[1]
            self.points.append((tmp1[0],tmp2[0],tmp3[0]))
        
    def laggedFibonacciGenerator(self,x):
        x = list(x)
        if(len(x)) >= max(self.a, self.c):
            point = (x[self.c] * x[self.a] )%self.modulo
            x.remove(x[0])
            x.append(point)
            return (point,x)
            
        else:
            raise CreatingGenerator4Exception()
            
class CreatingGenerator4Exception(Exception):
    def __init__(self):
        super().__init__("k or j is greater than seed")
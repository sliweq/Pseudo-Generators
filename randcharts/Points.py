class Points():
    def __init__(self, amount, option, modulo, a, c, seed):
        self.points = []
        self.amount = amount
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
                self.create4
        self.points = list(set(self.points))
        return self.points
            
    #option 1
    def linearCongruentialGenerator(self, x):
        if(x == None):
            return ((self.a*self.seed + self.c)%self.modulo)
        else: 
            return ((self.a*x + self.c)%self.modulo) 
        
    def create1(self):
        x = None
        for i in range(0,self.amount):
            tmp1 = self.linearCongruentialGenerator(x)
            tmp2 = self.linearCongruentialGenerator(tmp1)
            tmp3 = self.linearCongruentialGenerator(tmp2)
            x = tmp3
            self.points.append((tmp1,tmp2,tmp3))
            
    #option2
    def middleSquaregenerator(self, x):
        if(x == None):
            tmp = self.seed**2
            if(len(str(tmp)) >= self.a):
                tmp = str(tmp)
                return int(tmp[(self.a-len(tmp))//2:((self.a-len(tmp)//2)+len(tmp)+1)])
            else:
                return tmp
        else:
            tmp = x**2
            if(len(str(tmp)) >= self.a):
                tmp = str(tmp)
                return int(tmp[(self.a-len(tmp))//2:((self.a-len(tmp)//2)+len(tmp)+1)])
            else:
                return tmp
    
    def create2(self):
        x = None
        for i in range(0,self.amount):
            tmp1 = self.middleSquaregenerator(x)
            tmp2 = self.middleSquaregenerator(tmp1)
            tmp3 = self.middleSquaregenerator(tmp2)
            x = tmp3
            self.points.append((tmp1,tmp2,tmp3))
    
    #option3
    def create3(self):
        x = None
        for i in range(0,self.amount):
            tmp1 = self.lehmerCongruentialGenerator(x)
            tmp2 = self.lehmerCongruentialGenerator(tmp1)
            tmp3 = self.lehmerCongruentialGenerator(tmp2)
            x = tmp3
            self.points.append((tmp1,tmp2,tmp3))
            
    def lehmerCongruentialGenerator(self,x):
        if(x == None):
            return ((self.a*self.seed)%self.modulo)
        else: 
            return ((self.a*x)%self.modulo) 
        
    #option4
    def create4(self,x):
        x = None
        for i in range(0,self.amount):
            tmp1 = self.laggedFibonacciGenerator(x)
            tmp2 = self.laggedFibonacciGenerator(tmp1)
            tmp3 = self.laggedFibonacciGenerator(tmp2)
            x = tmp3
            self.points.append((tmp1,tmp2,tmp3))
        
    def laggedFibonacciGenerator(self,x):
        if(x == None):
            if(len(str(self.seed)) >= max(self.a, self.c)):
                #i chose addition but it could be also mul,sub,xor 
                tmp = str(self.seed)[self.c] + str(self.seed)[self.a]
                tmp = (self.seed%(10**(len(str(self.seed))-1)))*10 + tmp
                return tmp
            else:
                #TODO 
                #throw new error
                pass
        else:
            if(len(str(x)) >= max(self.a, self.c)):
                tmp = str(x)[self.c] + str(x)[self.a]
                tmp = (x%(10**(len(str(x))-1)))*10 + tmp
                return tmp
            else:
                #TODO 
                #throw new error
                pass
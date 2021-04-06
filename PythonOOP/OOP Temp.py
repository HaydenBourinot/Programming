class Temperature:
    def __init__ (self, mode='C', temp=0):
        self.mode = mode
        self.temp = temp

    def getTemp(self):
        if self.mode == 'C':
            return self.temp
        if self.mode == 'F':
            return 1.8*self.temp + 32

    def setMode(self, mode):
        self.mode = mode
        
t1 = Temperature ('C', 0)

print (t1.getTemp())
t1.setMode('F')
print (t1.getTemp())
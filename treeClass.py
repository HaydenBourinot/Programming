class Tree:
    def __init__ (self, n = 4, char = "*", decor = True):
        self.n = n
        self.char = char
        self.decor = decor

    def display(self, n = 4):    
        for x in range (1, self.n+1):
            for j in range (1, x+1): 
                for i in range (0,self.n-j):
                    print (" ", end="")
            
                if j!=x:
                    for i in range (0,(j*2)-1): 
                        print (self.char, end="")
                    print ();

                else: 
                    print (self.decor,end="")
                    for i in range (1,(j*2)-2):
                        print (self.char, end="")

                    if (x!=1):
                        print (self.decor);

                    else:
                        print ()

    def getSize (self):
        if self.n == 4:
            return self.n
        else:
            return self.n

    def setSize (self, n):
        self.n = n

    def getChar (self):
        if self.char == "*":
            return self.char
        else:
            return self.char
    
    def setChar(self, char):
        self.char = char

    def getDecor(self):
        if self.decor == "0":
            return self.decor
        else:
            return self.decor
    
    def setDecor(self, decor):
        self.decor = decor




s1 = Tree (4)


s1.display()
print(s1.getSize())
s1.setSize(6)
print(s1.getSize())
s1.display()

print(s1.getChar())
s1.setChar("#")
print(s1.getChar())
s1.display()

s1.setDecor("0")
s1.display()

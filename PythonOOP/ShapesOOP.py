class Square:
    def __init__ (self, sides = 4, length = 4, xpos = 0, ypos = 0, color = "white"):
        self.sides = sides
        self.length = length
        self.xpos = xpos
        self.ypos = ypos
        self.color = color

    def getSides (self):
        return self.sides

    def setSides (self, sides):
        self.sides = sides

    def getLength (self):
        return self.length

    def getXpos (self):
        return self.xpos

    def setXpos (self, xpos):
        self.xpos = xpos

    def getYpos (self):
        return self.ypos

    def setYpos (self, ypos):
        self.ypos = ypos

    def getColor (self):
        return self.color
    
    def setColor (self, color):
        self.color = color

    def getArea (self):
        return (self.length * self.length)

    def getPerimeter (self):
        return (self.length * self.sides)


class Triangle:
    def __init__ (self, sides = 3, xpos = 1, ypos = 1, color = "black", base = 10, height = 15):
        self.sides = sides
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.base = base
        self.height = height


    def getSides (self):
        return self.sides

    def setSides (self, sides):
        self.sides = sides

    def getXpos (self):
        return self.xpos

    def setXpos (self, xpos):
        self.xpos = xpos

    def getYpos (self):
        return self.ypos

    def setYpos (self, ypos):
        self.ypos = ypos

    def getColor (self):
        return self.color

    def setColor (self, color):
        self.color = color

    def getArea (self):
        return (self.base * self.height /2)
    
    def getBase (self):
        return self.base

    def setBase (self, base):
        self.base = base

    def getHeight (self):
        return self.height
    
    def setHeight (self, height):
        self.height = height

    def getPerimeter (self):
        return (self.base * 3)


class Rectangle:
    def __init__ (self, sides = 4, xpos = 2, ypos = 2, color = "yellow", length = 10, width = 5):
        self.sides = sides
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.length = length
        self.width = width

    def getSides (self):
        return self.sides

    def setSides (self, sides):
        self.sides = sides

    def getXpos (self):
        return self.xpos

    def setXpos (self, xpos):
        self.xpos = xpos

    def getYpos (self):
        return self.ypos

    def setYpos (self, ypos):
        self.ypos = ypos

    def getColor (self):
        return self.color
    
    def setColor (self, color):
        self.color = color

    def getArea (self):
        return (self.width * self.length)


    def getLength (self):
        return self.length
    
    def setLength (self, length):
        self.length = length

    def getWidth (self):
        return self.width

    def setWidth (self, width):
        self.width = width

    def getPerimeter (self):
        return ((self.width * 2) + (self.length * 2))



class Circle:
    def __init__ (self, sides = 0, xpos = 3, ypos = 3, color = "blue", radius = 20):
        self.sides = sides
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.radius = radius

    def getSides (self):
        return self.sides

    def setSides (self, sides):
        self.sides = sides

    def getXpos (self):
        return self.xpos

    def setXpos (self, xpos):
        self.xpos = xpos

    def getYpos (self):
        return self.ypos

    def setYpos (self, ypos):
        self.ypos = ypos

    def getColor (self):
        return self.color
    
    def setColor (self, color):
        self.color = color

    def getArea (self):
        return ((self.radius * self.radius) * 3.14159)

    def getCircumference (self):
        return (2 * self.radius * 3.14159)
    

    def getRadius (self):
        return self.radius
    
    def setRadius (self, radius):
        self.radius = radius


class Oval:
    def __init__ (self, sides = 0, xpos = 4, ypos = 4, color = "green", radiusone = 10, radiustwo = 15):
        self.sides = sides
        self.xpos = xpos
        self.ypos = ypos
        self.color = color
        self.radiusone = radiusone
        self.radiustwo = radiustwo

    def getSides (self):
        return self.sides

    def setSides (self, sides):
        self.sides = sides

    def getXpos (self):
        return self.xpos

    def setXpos (self, xpos):
        self.xpos = xpos

    def getYpos (self):
        return self.ypos

    def setYpos (self, ypos):
        self.ypos = ypos

    def getColor (self):
        return self.color

    def setColor (self, color):
        self.color = color

    def getArea (self):
        return (self.radiusone * self.radiustwo * 3.14159)

    def getCircumference (self):
        return (2 * 3.14159 * self.radiusone)
    

c1 = Circle ()
r1 = Rectangle ()
t1 = Triangle ()
s1 = Square ()
o1 = Oval ()

print (s1.getArea())
print (t1.getArea())
print (t1.getPerimeter())
print (o1.getArea())
print (o1.getCircumference())
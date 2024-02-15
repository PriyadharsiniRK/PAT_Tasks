class Test:
    #declaring pi as private variable
    __pi=3.141
    #constructor with radius parameter
    def __init__(self, radius):
        self.radius = radius
    #creating classmethod with argument radius
    @classmethod
    def areaCircle(a, radius):
        
        return Test.__pi*(radius*radius)
    @classmethod
    def perimeterCircle(p, radius):
        
        return 2*Test.__pi*radius

#getting radius value from user
radius = int(input("Enter radius value:"))
#calling area and perimeter function with radius parameter 
print("Area of circle:", Test.areaCircle(radius))
print("Perimeter of circle:", Test.perimeterCircle(radius))
    
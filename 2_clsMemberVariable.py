class Test:
    #declaring pi as private variable
    __pi=3.141
    #creating constructor with argument radius
    def __init__(self,radius):
        self.radius=radius
        #print(radius)
        self.areaOfCircle=Test.__pi*(radius*radius)
        #getting radius value from user
radius=int(input("Enter radius value:"))
#creating instance 
test_instance = Test(radius)
#calling areaOfCircle variable with className to print 
print("Area of circle:", test_instance.areaOfCircle)
    

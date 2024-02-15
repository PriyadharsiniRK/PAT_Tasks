#Creating Class Circle which have argument circle_listOfElements as List
class Circle:
    #Creating constructor for class Circle
    def __init__(self, circle_listOfElements):
        self.circle_listOfElements = circle_listOfElements
    #repr() function returns a printable string of object
    def __repr__(self):
        return f"{self.circle_listOfElements}"


# List to hold Circle instances
circle_listOfElements = []

# Append Circle instances with specified elements to the list
circle_listOfElements.append(Circle(1))
circle_listOfElements.append(Circle(2))
circle_listOfElements.append(Circle(3))
circle_listOfElements.append(Circle(5))

# Accessing the first element of the list and printing its representation
print("circle_list[0] :",circle_listOfElements[0])
print("circle_list[1] :",circle_listOfElements[1])
print("circle_list[3] :",circle_listOfElements[3])
print("circle_list[2] :",circle_listOfElements[2])

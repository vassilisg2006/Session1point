class Point:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    #creates a reference for points
  def __str__(self):
    return f"P<{self.x}, {self.y}>"
    #creates a string of x and y
  def __repr__(self):
    return self.__str__()

  def distance_origin(self):
    #calculate the distance between point and origin.
    #:return: float, distance between point and origin.
    return (self.x ** 2 + self.y ** 2) ** 0.5

  def distance_to(self,point):
    #calculates the distance between point and other point
    #returns float, distance between point and origin
    return((self.x - point.x)**2 +(self.y - point.y)**2)**0.5

  def __lt__(self, other):
    #Returns true if self is less than the other point.
    #param other: the other point to compare against
    #return: true or false
    return self.distance_origin()< other.distance_origin()

p1=Point(1,2)
p2=Point(3,4)

print(p1.x,p1.y)
print(p2.x,p2.y)
print(p1,p2)
print(f"{p2} distance to origin is {p2.distance_origin()}")
p3=Point(12,5)
print(f"{p3} distance to origin is {p3.distance_origin()}")
p1=Point(6,10)
p2=Point(6,15)
print(f"Distance between{p1} and {p2} is {p1.distance_to(p2)}")
p4= Point(1,1) # Define p4 before it's used in the list
points= [p1,p2,p3,p4] #list of points
print("Original points:", points)
points.sort()
print("Sorted points:", points) # Print the sorted list

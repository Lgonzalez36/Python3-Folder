
import math

class Point:
    """ class for representing a point """
    def __init__(self, xVal, yVal):
        """Initialize a Point obj’s coordinate """
        self.x = xVal
        self.y = yVal
        self.dist = math.sqrt(xVal**2 + yVal**2)
        
        
        
        
        
        
pts = [None] * 3
pts[0] = Point(10,20)
pts[1] = Point(100,200)
pts[2] = Point(1,2)


for i in range(3):
    print (pts[i].dist)
    
    
for j in range (len(pts)):
    for k in range (len(pts) - 1):
        if (pts.dist[j] == math.sqrt(pts.x[k]**2 + pts.y[k]**2)):
            
            Temp_X =  pts.x[k] 
            Temp_Y =  pts.y[k] 
            
            pts.x[k] =  pts.x[j + 1]
            pts.y[k] =  pts.y[j + 1]
                
            pts.x[j + 1] = Temp_X
            pts.y[j + 1] = Temp_Y
    
print("--------------------------------------------------")
print("your new Coordinates from accending order are: ")
for i in range(len(pts)):
    print("(", pts.x[i], ",", pts.y[i],")")
print("--------------------------------------------------")

#prints out nicely the new sorted arrays from the X and Y coordinates
    





PI = 3.14
def Circle():
 rad = float(input("Enter the radius of the circle: ")) 
 area = PI * rad * rad  
 print("Area of a circle = %.2f" %area)
 return input;
 

def Rectangle():            # width x height
 width = float(input("Enter width: "))
 length = float(input("Enter length: "))
 area = width * length 
 print("Area of Rectangle = %.2f" %area )
 return input;

def Triangle():             #Area of a triangle = (peri*(peri-x)*(peri-y)*(peri-z))-1/2
 x = float(input("Enter Base size: "))
 y = float(input("Enter Height: "))
 area = (x * y)*0.5
 print("Area of Triangle = %.2f" %area)
 return input;
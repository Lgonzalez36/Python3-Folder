print("1. Rectangle")
print("2. Circle")
print("3. Triangle")
option = input("Enter your choice:  ")
option = float(option)
option = int(option)

if (option ==1):
    print("You chose to work with a rectangle")
    len = input ("Enter lenght:  ")
    len = float(len)
   
    
    if (len <= 0):
        print("Invalid lenght")
        exit()
        
    wid = input("Enter width:  ")
    wid = float(wid)
    
    if (wid <=  0):
        print("Invalid width,")
        exit()
        
    area = len * wid
    peri = len + len + wid + wid
    
    print("lenght   Width   Area   Perimeter")
    print(len,"   ",wid, "   ", area, "    ",  peri,)


    
elif (option == 2):
    print("You chose to work with a circle")
    radius = input ("enter raduis:  ")
    radius = float(radius)
    
    if (radius <= 0):
        print("Invalid radius")
        exit()
    
    circum = 2 * 3.14 * radius
    area = 3.14 * radius* radius
    
    print("Circumference     Radius")
    print(circum, "  ", area)
    
elif(option == 3):
    print("You chose to worlk with a triangle")
     
    base = input("Enter the base length:  ")
    base = float(base)
     
    if (base <= 0):
         print("Invalid variable")
         exit()
         
    hieght = input("Enter Hieght of the triagnle:  ")
    hieght = float(hieght)
         
    if (hieght <= 0):
             print("Invaild hieght, please enter another one")
             exit()
    print("Area")
    print (hieght * base * 0.5)
             
    
    
else:
    print("Invaild option, please try again")
    
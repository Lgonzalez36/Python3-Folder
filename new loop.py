while (True):
    print("1. Rectangle")
    print("2. Circle")
    print("3. Quit")
    option = input("Enter your choice:  ")
    option = float(option)
    option = int(option)
    if (option == 1):
        while (True):
            len = input("enter length:  ")
            len = float(len)
            if (len <=0):
                print("Invalid length:  ")
            else:
                break
        while (True):
            wid = input("enter width:  ")
            wid = float(wid)
            if (wid <=0):
                print("Invalid width:  ")
            else:
                break
        area = len * wid
        peri = len + len + wid + wid
        print("length", len, "width", wid, "area", area, "peri", peri)
    elif (option == 2):
        while(True):
            radius = input ("enter radius:  ")
            radius = float(radius)
            if (radius <= 0):
                print("Invalid radius")
            else:
                break
        circum = 2 * 3.14 * radius
        area = 3.14 * radius* radius
        print("Circumference     Radius")
        print(circum, "  ", area)
    elif (option == 3):
        break
    else:
        print("Invalid Response")
    #### The end of the loop #####

        

 
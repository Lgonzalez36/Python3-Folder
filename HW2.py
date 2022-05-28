# CSCE 160 - Prof. Kim - HW2 
# Luis Gonnzalez and Merna Saad
# DO NOT MOVE, ERASE or MODIFY ANY of the existing code in the template.
# Also, DO NOT move things around.
import math
#################################################################################################
#-------------------  function definitions --------------------		  
#################################################################################################

def get_area (aa, bb, zz):
	# returns the area of a triangle given the length
	#  of two sides aa & ab  
	#   and the angle zz in radians
    area = 0.0
    area = ((aa * bb) * (math.sin(zz))/2)

	#calculate area

    return area

#################################################################################################
    
def rad2deg (rad):
	# converts the angle rad in radians and 
	#    returns the angle in degrees
    deg = 0.0
    deg = (rad * (180 / math.pi ))
    
    
    return deg

#################################################################################################	

def get_angle (aa, bb, cc):
	#  given three sides of a triangle aa, bb & cc
	#    returns the angle opposite of the side with length cc
	#    in radians
    angle = 0.0
    angle = math.acos(((aa ** 2) + (bb ** 2) - (cc ** 2)) / (2 * aa * bb))
    
    return angle
    

#################################################################################################	

def isNotValidTriangle (aa, bb, cc):
	# given three sides of a triangle aa, bb & cc
	#    determines whether or not it is a valid triangle.
	# returns true if it IS NOT a valid triangle
	# returns false if it IS a valid triangle

    if (aa + bb > cc and  cc > aa and cc > bb and cc >= 0):
        invalid = False
        
    elif (aa + cc > bb and bb > aa and bb > cc and bb >= 0):
        invalid = False
        
    elif(bb + cc > aa and aa > bb and aa > cc and aa >= 0):
        invalid = False
        
    else:
        invalid = True
    
    return invalid

#################################################################################################
#################################################################################################
#-------------------  Start of the main program --------------------		
    
while (True):
    print ("-----------------------")
    print ("Program Modes")
    print ("(1) Enter sides")
    print ("(2) Quit")
    user_choice = input ("Enter Mode: ")
    user_choice = int(user_choice)

    if(user_choice == 1):
   
        # ask user for sides and read the values in 
        a = float (input("Enter side a: ") )
        b = float (input("Enter side b: ") )
        c = float (input("Enter side c: ") )
    
        # determine if it's a valid triangle using the function validTriangle
        # learn the use of this function: validTriangle and how it is used
      	# as a conditional statement along with the ! (not) operator. 
   		# What is it doing??
            
        
        
        if ((isNotValidTriangle(a,b,c)) != False):
            print ("Not a valid triangle!\n")
            continue
            
        else:
            print("your triangle is vaild")
        
        
         # learn how to use CONTINUE.
	        # continue forces the program to go back to the beginning
	        # of the most immediate loop that contains this command 
            
#################################################################################################

    		# get all three angles using the function get_angle
            x = get_angle (b, c, a)  # x is opposite a
            y = get_angle (c, a, b)
            z = get_angle (a, b, c)
    		# ... # y is opposite ___
    		# ... # z is opposite ___
          
#################################################################################################
            
    		# get the area using get_area function
    		# area can be calculated using any valid combination of sides and angle
    		# and only needs to be done once.. 
            area = get_area (b, c, x)
          
############################################################################################  
            
            # convert the angles from radians to degrees using rad2deg function
            x = rad2deg(x)
            y = rad2deg(y)
            z = rad2deg(z)
            
            print("Angle one is   ", x)
            print("Angle two is   ", y)
            print("Angle three is ", z)
            print ("area = ", area)

            

    		# ...  what about y and z?
    
          	# print out the results
          	# print angle x,y,z and the area
 
############################################################################################
              
    elif (user_choice == 2):
        break
    else:
        print ("Invalid choice")


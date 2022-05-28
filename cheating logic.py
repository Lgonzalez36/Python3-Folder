# Prof. Kim
# 9/25/2019
# min , max
import random

values = [None] * 10

#values[0] = random.randint(1,1001)
#values[1] = random.randint(1,1001)
#values[2] = random.randint(1,1001)
# ...
#values[49] = random.randint(1,1001)

for i in range(0,10,1):
    values[i] = random.randint(1,10)

#print (values)

#print(values[0])
#print(values[1])
#print(values[2])
#...
#print(values[49])

for i in range(0,10,1):
    print(values[i])


# assume that the 1st element is the min
min = values[0]

# see if we could find a smaller value

for i in range(0,10,1):
    if (values[i] < min):
        min = values[i]
    
print (values)

print("Min=", min)



max = values[0]
# see if we could find a larger value
for i in range(0,10,1):
    if (values[i] > max):
        max = values[i]

print("Max=", max)



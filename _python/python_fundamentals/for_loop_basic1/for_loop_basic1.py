for x in range(0, 151, 1):
    print(x, end=" ") # i put (end= " ") just to print in one line
else:
    print("*****************************************************************")


for x in range(5, 1001, 5):
    print(x, end=" ") # i put (end= " ") just to print in one line
else:
    print("*****************************************************************")

for x in range(1, 101):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding")
    else:
        print(x) 
print("***********************************************************************")       # python for_loop_basic1.py


y = 0
for x in range(1, 500001, 2):
    y = y + x
print(y)
print("**************************************************************************")


for x in range(2018, 0, -4):
    print(x) 
print("*********************************************************************************")


low = 2 
high = 9 
mult = 3
for i in range (low, high+1):
        if i % mult == 0:
            print (i)




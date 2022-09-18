def Countdown(num):
    list=[]
    for x in range(num, -1, -1):
        list.append(x)
        continue
    return(list)
result = Countdown(5)
print(result)
print("*******************************************************")



def print_and_return(list):
    if len(list) > 2:
        print("Please enter just two element")
    else:
        print(list[0])
        return(list[1])



def first_plus_length(list):
    return(list[0] + len(list))


def Values_Greater_than_Second(list):
    newList = []
    if len(list) < 2:
        return False
    else:
        for x in range(len(list)):
            if list[x] > list[1]:
                newList.append(list[x])
        print(len(newList))
    return(newList)    



def length_and_value(size,value):
    newList = []
    for x in range(size):
        newList.append(value)
    return newList





# 1) Biggie Size 
def biggie_size(list):
    for x in range(len(list)):
        if list[x] > 0:
            list[x] = "big"
    return(list)
print(biggie_size([-1,3,5,-5]))


#  2) Count Positives
def Count_Positives(list):
    count = 0
    for x in range (len(list)):
        if list[x] > 0:
            count +=1
    list[len(list)-1] = count
    return(list)
print(Count_Positives([1,6,-4,-2,-7,-2]))

#  3)Sum Total
def sum(list):
    return(sum(list))
print(sum([1,2,3,4,5]))

#  for loop to find summation
def sum(list):
    total = 0
    for x in range(len(list)):
        total +=list[x]
        continue
    return(total)
                        #why built in function sum doesn't exsist??

#  4) Average
def avg(list):
    total = 0
    for x in range(len(list)):
        total +=list[x]
        continue
    return(total/(len(list)))



#  5) Length
def length(list):
    return(len(list))

#  6)Minimum
def Minimun (list):
    if len(list)==0:
        return False
    else:
        Min = list[0]
        for x in range (1,len(list)):
            if list[x]< Min:
                Min=list[x]
        return(Min)

#  7) Maximum
def Maximum (list):
    if len(list)==0:
        return False
    else:
        max = list[0]
        for x in range (1,len(list)):
            if list[x]> max:
                max=list[x]
        return(max)


# 8)Ultimate Analysis
def Ultimate_Analysis (list):
    dictionary = {"sumtotal":0, "average":0, "minimum":list[0], "maximum":list[0],"length":len(list)}
    for x in range(len(list)):
        if list[x]> dictionary["maximum"]:
            dictionary["maximum"]=list[x]
        elif list[x]< dictionary["minimum"]:
            dictionary["minimum"]=list[x]
        dictionary["sumtotal"]+=list[x]
        dictionary["average"]= dictionary["sumtotal"]/len(list)
    return dictionary

# 9)Reverse List
#  a) with  for loop
def Reverse_List (list):
    for i in range (int(len(list)/2)):
        New =list[i]
        list[i]=list[len(list)-i-1]
        list[len(list)-i-1] = New
    return list

# b) using built_in_function 
def ReverseList (list):
    list.reverse()
    return list








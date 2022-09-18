import random
def randInt(min=0, max=100):
    if min>max:
        return False
    else:
        num = random.random()*(max-min) + min
        num = round (num)
        return num
result = randInt(min=50, max=80)
print (result)
import random
n = random.randint(29,45)
h = random.randint(50,70)
while 1:
    if ((n>=35) and (n<=45))and ((h>=50)and (h<=60)):
        print("ALERT!!"+str(n)+"degree and "+str(h)+"% humidity detected")
        break
    else:
        print("Normal temperature")
    n = random.randint(29,45)
    h = random.randint(50,70)

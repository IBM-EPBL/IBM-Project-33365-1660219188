import random
temp = random.randint(26,40)
humidity = random.randint(50,80)
while 1:
    if ((temp>=35) and (temp<=45))and ((humidity>=50)and (humidity<=60)):
        print("ALERT!!"+str(temp)+"degree and "+str(humidity)+"% humidity detected")
        break
    else:
        print("Normal temperature")
    temp = random.randint(26,40)
    humidity = random.randint(50,80)

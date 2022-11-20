import random
t = random.randint(26,40)
h = random.randint(50,80)
while True:
    if(t in range (35,40,1)) and (h in range (50,80,1)):
        print("ALERT! High temperature of "+str(t)+" degree and "+str(h)+"% humidity is detected")
        break
    else:
        print("Normal temperature of "+str(t)+" degree and "+str(h)+"% humidity is detected")
        t = random.randint(26,40)
        h = random.randint(50,80)
         
    
     
     
          
        
            
       

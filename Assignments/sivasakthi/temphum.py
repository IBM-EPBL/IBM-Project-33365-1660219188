import random
n = random.randint(26,46)
m = random.randint(50,80)
while True:
    if(n in range (35,46,1)) and (m in range (50,80,1)):
        print("ALERT! High temperature of "+str(n)+" degree and "+str(m)+"% humidity is detected")
        break
    else:
        print("Normal temperature of "+str(n)+" degree and "+str(m)+"% humidity is detected")
        n = random.randint(26,46)
        m = random.randint(50,80)
         
    
     
     
          
        
            
       

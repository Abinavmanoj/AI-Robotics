def check_obstacle(distance):
    
     if distance < 30:
      return "stop"
        
     elif 30 <= distance <= 70:
        return "move slow"
     else:
        return "move fast"
while True:
  distance = int(input("Enter the distance to the obstacle: "))
  decision = check_obstacle(distance)
  print(decision)
  if decision == "stop":
     break


 

 
 
 

 

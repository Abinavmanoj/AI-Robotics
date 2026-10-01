while True:
 try:
 
       sensor_reading = int(input("Enter sensor reading: "))

       with open("senseor_logger.txt","a") as file:
        file.write(str(sensor_reading) + "\n")
       
       if sensor_reading < 30:
        print("stop.")
       elif 30 <= sensor_reading < 60:
        print("slow down.")
       else:
        print("go fast.")
        print("sensor reading saved.")
    
 except ValueError:
    print("Enter a number.")
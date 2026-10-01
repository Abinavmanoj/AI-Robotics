sensor_reading = int(input("Enter sensor reading: "))
with open("senseor_logger.txt","a") as file:
    file.write(str(sensor_reading) + "\n")
    print("sensor reading saved.")

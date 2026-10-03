def get_battery():
    while True:
        try:
            battery = int(input("Enter battery level (0-100): "))
            if 0 <= battery <= 100:
                return battery
            else:
                print("Battery level must be between 0 and 100.")
        except ValueError:
            print("please enter the number")

def get_distance():
    while True:
        try:
            distance = int(input("Enter distance to obstacle (in cm): "))
            if distance >= 0:
                return distance
            else:
                print("Distance cannot be negative.")
        except ValueError:
            print("Please enter a valid number.")
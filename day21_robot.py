class robot:
    def __init__(self, name, battery, speed):
        self.name = name
        self.battery = battery
        self.speed = speed

    def show_status(self):
        print("Robot Name:", self.name)
        print("Battery:", self.battery)
        print("Speed:", self.speed)

    def move(self,distance):
        if self.battery <= 20:
            print(self.name, "cannot move. Battery is low.")
        elif distance < 30:
            print(self.name, "cannot move. Distance is too short.") 
            
        else:
            self.battery = self.battery - 10
            print(self.name, "is moving.")
            print("Battery", self.battery)
robot1 = robot("Robo1", 110, 10)
robot2 = robot("Robo2", 70, 15)
robot3 = robot("Robo3", 40, 20)
robot1.move(100)
robot1.move(50)
robot1.move(20)
robot2.move(100)
robot2.move(100)
robot3.move(100)
robot3.move(100)

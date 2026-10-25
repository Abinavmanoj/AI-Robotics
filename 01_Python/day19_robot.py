class robot:
    def __init__(self, name, battery, speed):
        self.name = name
        self.battery = battery
        self.speed = speed

    def show_status(self):
        print("Robot Name:", self.name)
        print("Battery:", self.battery)
        print("Speed:", self.speed)
    def move(self):
        if self.battery <= 20:
            print(self.name, "cannot move. Battery is low.")
            
        else:
            self.battery = self.battery - 10
            print(self.name, "is moving.")
            print("Battery", self.battery)

robot1 = robot("Robo1", 30, 10)
robot1.show_status()
robot1.move()   
robot1.move()
robot1.move()
robot1.move()
robot1.show_status()
           
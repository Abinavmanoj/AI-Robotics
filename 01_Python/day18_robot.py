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
        print(self.name,"is moving at speed")
robot1 = robot("Robo1", 100, 10)
robot2 = robot("Robo2", 80, 15)
robot3 = robot("Robo3", 13, 10)
robot1.show_status()
robot2.show_status()
robot3.show_status()

robot1.move()
robot2.move()
robot3.move()

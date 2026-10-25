class robot:
    def __init__(self, name,battery,speed):
        self.name = name
        self.battery = battery
        self.speed = speed

    def move(self,distance):
        if self.battery <= 20:
            print(self.name, "cannot move. Battery is low.")    
        elif distance < 30:
            print(self.name,"cannot move.Distance is too short")
           
        else:
            self.battery = self.battery - 10
            print(self.name, "is moving.")
            print("battery", self.battery)
robot1 = robot("Robo1", 50, 10)
robot2 = robot("Robo2", 20, 10)
robot3 = robot("Robo3", 40, 10)
robot1.move(50)
robot1.move(20)
robot1.move(100)
robot2.move(100)
robot3.move(100)
robot3.move(100)
robot3.move(100)

class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
        self.speed = 0
        self.distance = 0  
    def read_sensor(self, distance):
        self.distance = distance
        print(self.name, "sensor reading:", self.distance, "cm")
    def decide(self):
        if self.distance < 20:
            self.speed = 0
            print(self.name, "decision: STOP")
        elif self.distance < 50:
            self.speed = 20
            print(self.name, "decision: SLOW")
        else:
            self.speed = 50
            print(self.name, "decision: FAST")
    def move(self):
        if self.speed == 0:
            print(self.name, "cannot move")
        else:
            self.battery -= 10
            print(self.name, "is moving")
            print("Battery left:", self.battery)
robot1 = Robot("Robo1", 110)
robot1.read_sensor(15) 
robot1.decide()
robot1.move()
robot1.read_sensor(60)
robot1.decide()
robot1.move()
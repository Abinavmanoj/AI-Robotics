class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
        self.speed = 0
        self.distance = 0  
    def read_sensor(self, distance):
        self.distance = distance
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
    def show_state(self):
        print("-----Robot state-----")
        print("Robot Name:", self.name)
        print("Battery:", self.battery)
        print("Speed:", self.speed)
        print("Distance:", self.distance)
robot1 = Robot("Robo1", 110)
robot2 = Robot("Robo2", 90)
robot3 = Robot("Robo3", 80)

robot1.read_sensor(15)
robot2.read_sensor(60)
robot3.read_sensor(80)


robot1.decide()
robot2.decide()
robot3.decide()

robot1.show_state()
robot2.show_state()
robot3.show_state()



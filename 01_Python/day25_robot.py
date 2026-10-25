class robot:
    def __init__(self, name, battery,):
        self.name = name
        self.battery = battery
        self.speed = 0
        self.distance = 0
    def read_sensor(self,distance):
        self.distance = distance
        print(self.name,"sensor reading:", self.distance, "cm")
    def decide(self):
        if self.distance < 20:
            self.speed = 0
            print(self.name,"decision:STOP")
        elif self.distance <50:
            self.speed = 20
            print(self.name, "decision:SLOW")
        else:
            self.speed = 50
            print(self.name,"decision:FAST")
    def show_state(self):
        print("-----Robot state-----")
        print("Robot Name:", self.name)
        print("Battery:", self.battery)         
        print("Speed:", self.speed)
        print("Distance:", self.distance)
robot1 = robot("Robo1", 110)
robot1.read_sensor(80)  
robot1.decide()
robot1.show_state()

robot1.read_sensor(15)
robot1.decide() 
robot1.show_state()

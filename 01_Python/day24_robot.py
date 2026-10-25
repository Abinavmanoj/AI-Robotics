class robot:
    def __init__(self, name, battery,):
        self.name = name
        self.battery = battery
        self.speed = 0
    def read_sensor(self,distance):
        self.distance = distance
        print(self.name,"sensor reading:", self.distance, "cm")
    def decide(self):
        if self.distance < 20:
            print(self.name,"decision:STOP")
        elif self.distance <50:
            print(self.name, "decision:SLOW")
        else:
            print(self.name,"decision:FAST")
robot1 = robot("Robo1", 110)
robot1.read_sensor(80)  
robot1.decide()
robot1.read_sensor(45)
robot1.decide() 
robot1.read_sensor(15)
robot1.decide() 

    
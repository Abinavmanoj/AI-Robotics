class robot:
    def __init__(self, name, battery, ):
        self.name = name
        self.battery = battery
        self.speed = 0

    def read_sensor(self,distance):
        self.distance = distance
        if distance < 20:
            print(self.name,"stop! obstacle is close", distance, "cm")
        elif distance <50:
            print(self.name, "slow! obstacle detected", distance, "cm")
        else:
            print(self.name,"fast.distance:",distance, "cm")
robot1 = robot("Robo1", 110)
robot1.read_sensor(80)
robot1.read_sensor(45)
robot1.read_sensor(15)
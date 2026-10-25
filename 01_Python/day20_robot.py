class Robot:
    def __init__(self,name,battery,speed):
        self.name = name
        self.battery = battery
        self.speed = speed
    def move(self,distance):
        if self.battery  <=20:
            print(self.name,"cannot move.Battery is low")
        elif distance < 30:
            print(self.name,"cannot move.obstacle is close")
        else:
            self.battery = self.battery - 10
            print(self.name, "is moving")
            print("Battery:", self.battery)
robot1 = Robot("robot1", 80, 10)
distance = int(input("enter the distance"))
robot1.move(distance)
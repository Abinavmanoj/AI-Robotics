def move(self):
        if self.battery <= 20:
            print(self.name, "cannot move. Battery is low.")
            
        else:
            self.battery = self.battery - 10
            print(self.name, "is moving.")
            print("battery", self.battery)
robot1 = robot("Robo1", 30, 10)
robot1.show_status()
robot1.move()
robot1.move()
robot1.move()
robot1.move()
robot1.show_status()
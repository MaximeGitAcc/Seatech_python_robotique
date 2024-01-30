	
from abc import ABCMeta,abstractmethod

class vehicule(metaclass=ABCMeta):

    @property
    @abstractmethod
    def vehicule_type(self):
        pass

    def Connection(self):
        print("I'm connected")
    
    def Moove(self):
        print("I'm mooving")

    @property
    @abstractmethod
    def SpeedInfo(self):
        pass

class Unmanned(metaclass=ABCMeta):

    def Human_Control(self):
        print("I'm in human control mode")
    
    def Autonomous_Control(self):
        print("I'm in autonomous mode")
    
    def Mission(self):
        print("I've a mission !")

    @property
    @abstractmethod
    def Name(self):
        pass

    @Name.setter
    @abstractmethod
    def Name(self,name):
        pass

class UUV(Unmanned,vehicule):

    def vehicule_type(self):
        print("I'm an UUV ")

    def SpeedInfo(self):
        print("I'm going at 5.4 knots")
    
    @property
    def Name(self):
        return 'UUV '+self.name

    @Name.setter
    def Name(self,name):
        self.name = name
        


class UAV(Unmanned,vehicule):

    def vehicule_type(self):
        print("I'm an UAV ")

    def SpeedInfo(self):
        print("I'm flying mach 3 speed") 
    
    def Mission(self):
        print("My mission is to eliminate the enemy !")
    
    @property
    def Name(self):
        return 'UAV ' +self.name

    @Name.setter
    def Name(self,name):
        self.name = name

class UGV(Unmanned,vehicule):
    name = 'unkown'
    def vehicule_type(self):
        print("I'm an UGV ")

    def SpeedInfo(self):
        print("I'm riding at 120 Miles per hour")
    
    @property
    def Name(self):
        return 'UGV ' +self.name

    @Name.setter
    def Name(self,name):
        self.name = name
    
class UAGV(UGV,UAV):
    pass




drone = UAV()

drone.Name = 'Drone'
print("\nI'm", drone.Name)
drone.vehicule_type()
drone.Mission()

submarine = UUV()

submarine.Name = 'submarine'
print("\nI'm", submarine.Name)
submarine.Moove()
submarine.SpeedInfo()

motorbike = UGV()

motorbike.Name = 'motorbike'
print("\nI'm", motorbike.Name)
motorbike.Human_Control()
motorbike.Connection()

plane = UAGV()

plane.Name = 'plane'
print("\nI'm", plane.Name)
plane.Autonomous_Control()
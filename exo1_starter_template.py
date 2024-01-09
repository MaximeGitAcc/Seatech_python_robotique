class Robot():
    __name = ""
    __power = False
    __current_speed = 0
    __battery_level = 0
    __states = ['shutown', 'running']
    __if_charge = 0

    def __init__(self, name):
	
      self.__name = name
      self.__current_speed = 0
      self.__battery_level = 0
      self.power = False
    
    def allumer (self):
       self.power = self.__states[1]
       print("%s s'allume "%(self.__name))
      
    def eteindre (self):
       self.power = self.__states[0]
       print("%s s'éteint "%(self.__name))
    def charge (self):
       
      if self.__if_charge == 1 :
          while (self.__battery_level <100):
           for i in range (100):
              self.__battery_level += 1

         
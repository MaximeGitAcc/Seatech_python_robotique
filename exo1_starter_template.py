import time

class Robot():   
    

   def __init__(self, name):
	
      self.__name = name
      self.__current_speed = 0
      self.__battery_level = 0
      self.__states = ['shutown', 'running']
      self.power = False
    
   def allumer (self):
       self.power = self.__states[1]
       print("%s s'allume "%(self.__name))
      
   def eteindre (self):
       self.power = self.__states[0]
       print("%s s'éteint "%(self.__name))

   def charge (self):
       
      if self.__if_charge == 1 :
          T = 0
          while (self.__battery_level <100):
           for i in range (100) and T <=10:
              self.__battery_level += 1
              time.sleep(1)
              T += 1
   
   def decharge (self):
       while (self.__battery_level >0):
          for i in range(self.__battery_level):
             self.__battery_level -= 1

   @property
   def power(self):
       return self.__power

   @power.setter
   def power(self, power):
       self.__power = power

   @property
   def action(self):
      if self.__power:
         return self.action


if __name__ == '__main__':
   r1 = Robot()
   print(r1.power)



   

         
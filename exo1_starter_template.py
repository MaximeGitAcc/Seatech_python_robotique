import time
import math


class Robot():     

   def __init__(self):
	
      self.__name = input("Le temps est venue de lui donner un petit nom : ")
      self.__current_speed = 0
      self.__battery_level = 0
      self.__states = ['shutown', 'running']
      self.power = False
      self.__vitesse = 0
      self.__direction = ['Avance','Recule']
      print("Bonjour, je suis votre nouveau robot. J'aime beaucoup le prénom que vous m'avez donnée :", self.__name)
    
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
              time.sleep(0.5)
              T += 1
   
   def decharge (self):
       while (self.__battery_level >0):
          for i in range(self.__battery_level):
             self.__battery_level -= 1

   def Avancer (self):
      self.__vitesse = input("Entrez une vitesse (Max 20 kmH ")
      if self.__vitesse < 20:
         self.__direction = self.__direction[0]

   def Reculer (self):
      self.__vitesse = abs(input("Entrez une vitesse (Max 5 kmH en arrière) "))
      if -self.__vitesse > -5:
         self.__direction = self.__direction[1]
    

      

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
   pass






   

         
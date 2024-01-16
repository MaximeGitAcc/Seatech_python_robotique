import time
import math


class Robot():     

   __slots__ = ("__name","__current_speed","__battery_level","__states","__power","__vitesse","__direction","__EnCharge")

   def __init__(self,name):
	
      self.__name = name
      self.__current_speed = 0
      self.__battery_level = 20
      self.__states = ['shutown', 'running']
      self.power = False
      self.__vitesse = 0
      self.__direction = ['Avance','Recule']
      self.__EnCharge = 0
      print("Bonjour, je suis votre nouveau robot. J'aime beaucoup le prénom que vous m'avez donnée :", self.__name)
    
   def allumer (self):
       if self.__battery_level >= 20:
          self.power = self.__states[1]
          print("%s s'allume "%(self.__name))


         #  if (self.__battery_level >5):
         #            for i in range(self.__battery_level):
         #                 self.__EnCharge = 0
         #                 self.__battery_level -= 1
         #                 print("Mon niveau de batterie est de ", self.__battery_level, "%", end='\r', flush=True)
         #                 time.sleep(0.5)
                         
       else :
          print("Désolé le robot n'a pas assez de batterie.")
      
   def eteindre (self):
       self.power = self.__states[0]
       print("%s s'éteint "%(self.__name))

   def charge (self):
       
      if self.__battery_level <5:
          print("Ma batterie est faible je vais me recharger !")
          T = 0
          while (self.__battery_level <100):
           for i in range (100):
            if T <=10:
               self.__EnCharge = 1
               self.__battery_level += 1
               time.sleep(0.5)
               T += 1
               print("Mon niveau de batterie est de ", self.__battery_level, "%", end='\r', flush=True)
      else:
         print("batterie Full !")

            
   
   def Avancer (self):
      if self.power == 'running':
         self.__vitesse = int(input("Entrez une vitesse (Max 20 kmH) : "))
         if self.__vitesse <= 20:
            self.__direction = self.__direction[0]
            print("Le robot se déplace à une vitesse de ", self.__vitesse, "vers l'avant")
      else :
         print("Le robot ne bouge pas, il ne semble pas être allumé")

   def Reculer (self):
      if self.power == 'running':
         self.__vitesse = abs(int(input("Entrez une vitesse (Max 5 kmH en arrière) : ")))
         if -self.__vitesse >= -5:
            self.__direction = self.__direction[1]
            print("Le robot se déplace à une vitesse de ", self.__vitesse, "vers l'arrière")
      else :
         print("Le robot ne bouge pas, il ne semble pas être allumé")
    
   def Carac (self):
      if self.power == 'running':
         print("Voici mes caractéristiques :\n- Mon nom : ", self.__name, "\n- Mon deplacement : ", self.__direction , "\n- Vitesse :", self.__vitesse , "\n- En Charge : ", self.__EnCharge )
      else :
         print("Le robot ne bouge pas, il ne semble pas être allumé")

   def Stop (self):
      if self.power == 'running':
         self.__vitesse = self.__vitesse - self.__vitesse
         print("je me suis arrêté, ma vitesse est donc à ", self.__vitesse)
      else :
         print("Le robot ne bouge pas, il ne semble pas être allumé")
   
   def AffichBatterie (self):
      if self.__EnCharge == 1:
         print("Mon niveau de batterie est de ", self.__battery_level, "%", end='\r', flush=True)
      else :
         print("Le robot n'est pas en charge")

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









   

         
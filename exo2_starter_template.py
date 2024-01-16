from exo1_starter_template import Robot


class Human():
    
    #__slots__ = ("__sexe","__diet")
    
    def __init__(self,sexe,diet):
      self.__sexe = sexe
      self.__diet = diet
      self.__food = []
      
    def eat(self,food):
        print("Eating a ", food)

    def digest(self):
        print("The banana will be easy to digest, rather than coca and chips !")

    @property
    def sexe(self):
        if self.__sexe:
            return self.__sexe
    @property
    def diet(self):
        if self.__diet:
            return self.__diet

class Cyborg(Robot, Human):   

    __slots__ = ()

    def __init__(self, name, sexe,diet):  
        Robot.__init__(self, name)
        Human.__init__(self, sexe, diet)

    def BigJump (self):
        print("The Cyborg Jump Hard thanks to his legs !")


cyborg = Cyborg('Deux Ex Machina', 'M', 'Omnivorous')

print('name :',cyborg.name, '\nsexe :', cyborg.sexe, '\ndiet :', cyborg.diet)
print('Charging battery...')
cyborg.charge()
cyborg.Carac()
cyborg.allumer()
cyborg.Carac()
cyborg.eat('banana')
cyborg.eat(['coca', 'chips'])
cyborg.digest()
cyborg.BigJump() #C'est le truc fun 
#                           |
#                           v       
#
#                         ██████                      
#     ████            ██████░░░░██                    
#   ██▒▒▒▒██        ██▒▒░░░░██░░░░██          ████    
# ██▒▒▒▒▒▒▒▒██    ██▒▒▒▒▒▒▒▒▒▒████████      ██▒▒▒▒██  
# ██▒▒▒▒▒▒████    ██▒▒▒▒▒▒▒▒▒▒██░░░░▒▒██  ██▒▒▒▒▒▒▒▒██
#   ██▒▒▒▒██▒▒████░░▒▒▒▒▒▒▒▒▒▒▒▒████▒▒██  ████▒▒▒▒▒▒██
#     ██▒▒▒▒▒▒▒▒██░░▒▒▒▒        ▒▒▒▒  ████▒▒██▒▒▒▒██  
#       ██▒▒▒▒▒▒██░░▒▒      ████  ██  ██▒▒▒▒▒▒▒▒██    
#         ████▒▒░░██▒▒      ████  ██  ██▒▒▒▒▒▒██      
#           ██░░░░██▒▒                ░░▒▒████        
#             ██░░░░██▒▒    ██████  ██░░░░██          
#               ██░░░░██  ██████████░░░░██            
#               ██░░░░░░██  ██████░░░░██              
#                 ██░░░░░░░░░░░░░░░░████              
#                 ██░░░░░░░░░░░░░░░░██                
#                 ██░░░░░░░░░░░░░░░░██████            
#                 ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░██          
#                 ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░██        
#                 ██░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░██        
#                 ██░░░░░░░░████████░░░░░░░░██        
#                 ██░░░░░░██        ██▒▒▒▒▒▒▒▒██      
#                 ██░░░░▒▒██        ██▒▒▒▒▒▒▒▒▒▒██    
#                 ██▒▒▒▒▒▒██        ████▒▒▒▒▒▒▒▒██    
#                 ██▒▒▒▒▒▒▒▒██          ████████      
#                   ██▒▒▒▒▒▒██                        
#                   ██▒▒▒▒▒▒██                        
#                   ██▒▒▒▒▒▒██                        
#                   ██▒▒▒▒▒▒██                        
#                   ██▒▒▒▒▒▒██                        
#                     ██████                          

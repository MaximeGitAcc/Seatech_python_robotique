from exo1_starter_template import Robot


class Human():
    
    #__slots__ = ("__sexe","__diet")
    
    def __init__(self,sexe,diet):
      self.__sexe = sexe
      self.__diet = diet
      self.__food = []
      
    def eat(self,food):
        print("You ate a ", food)

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

    #__slots__ = ()

    def __init__(self, name, sexe,diet):  
        Robot.__init__(self, name)
        Human.__init__(self, sexe, diet)



cyborg = Cyborg('Deux Ex Machina', 'M', 'Omnivorous')

print(cyborg.name, 'sexe', cyborg.sexe)
print('Charging battery...')
cyborg.charge()
cyborg.Carac()
cyborg.eat('banana')
cyborg.eat(['coca', 'chips'])
cyborg.digest()

# cyborg.truc_fun()
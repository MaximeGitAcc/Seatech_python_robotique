from exo1_starter_template import Robot


class Human():
    
    __slots__ = ("__sexe","__diet")
    
    def __init__(self,sexe):
      self.__sexe = sexe
      self.__diet = ['Carnivorous', 'Vegan', 'Vegetarian', 'Omnivorous']
      
    def eat(self):
        print("You are a ", self.__diet)

    def digest(self):
        print("The banana will be easy to digest, rather than coca and chips !")


class Cyborg(Robot, Human):   

    __slots__ = ()
    
    def __init__(self, name, sexe):  
        Robot.__init__(self, name)
        Human.__init__(self, sexe)



cyborg = Cyborg('Deux Ex Machina', 'M')

print(cyborg.name, 'sexe', cyborg.sexe)
print('Charging battery...')
cyborg.charge()
cyborg.Carac()
cyborg.eat('banana')
cyborg.eat(['coca', 'chips'])
cyborg.digest()

# cyborg.truc_fun()
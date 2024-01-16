from exo1_starter_template import Robot
r1 = Robot()

CreationRobot = input("Bienvenue chez Aperture, voulez-vous créer un nouveau robot ? ")
if CreationRobot == "Oui" or CreationRobot == "oui":
      r1 = Robot()

else :
      print("Vous n'avez pas l'argent c'est ça ? Sortez tous de suite de notre magasin !")
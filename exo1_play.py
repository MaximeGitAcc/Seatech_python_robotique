import keyboard
from exo1_starter_template import Robot

CreationRobot = input("Bienvenue chez Aperture, voulez-vous créer un nouveau robot ? ")
if CreationRobot == "Oui" or CreationRobot == "oui":
      r1 = Robot()

else :
      print("Vous n'avez pas l'argent c'est ça ? Sortez tous de suite de notre magasin !")

print("Voici les fonctionnalités dont je dispose :\n- M'allumer (Allumer ou 'a')\n- M'éteindre (Eteindre ou 'e')\n- Aller me mettre en charge (Charge ou 'r')\n- Afficher mon pourcentage de Batterie en charge(Batterie ou 'b')\n- Avancer avec une certaine vitesse (Avancer ou 'z')\n- Reculer avec une certaine vitesse (Reculer ou 's')\n- S'arrêter net sur demande (Stop ou 'space')\n- Donner les caractéristiques du robot (Carac ou 'c')")

Quefaire = input("Que voulez-vous que je fasses : ")

if Quefaire == 'Allumer' or Quefaire == 'allumer':
     r1.allumer()
     r1.decharge()
elif Quefaire == 'Eteindre' or Quefaire == 'eteindre':
     r1.eteindre()
elif Quefaire == 'Charge' or Quefaire == 'charge':
     r1.charge()
elif Quefaire == 'Batterie' or Quefaire == 'Batterie':
     r1.AffichBatterie()
elif Quefaire == 'Avancer' or Quefaire == 'avancer':
     r1.Avancer()
elif Quefaire == 'Reculer' or Quefaire == 'reculer':
     r1.Reculer()
elif Quefaire == 'Stop' or Quefaire == 'stop':
     r1.Stop()
elif Quefaire == 'Carac' or Quefaire == 'carac':
     r1.Carac()


# def on_key_press_a(event):
#       print(f"You pressed {event.name}")

# def on_key_press_e(event):
#      print(f"You pressed {event.name}")

# def on_key_press_r(event):
#      print(f"You pressed {event.name}")

# def on_key_press_b(event):
#      print(f"You pressed {event.name}")

# def on_key_press_z(event):
#      print(f"You pressed {event.name}")

# def on_key_press_s(event):
#      print(f"You pressed {event.name}")

# def on_key_press_space(event):
#      print(f"You pressed {event.name}")

# def on_key_press_c(event):
#      print(f"You pressed {event.name}")

# keyboard.add_hotkey('a', on_key_press_a)
# keyboard.add_hotkey('e', on_key_press_e)
# keyboard.add_hotkey('r', on_key_press_r)
# keyboard.add_hotkey('b', on_key_press_b)
# keyboard.add_hotkey('z', on_key_press_z)
# keyboard.add_hotkey('s', on_key_press_s)
# keyboard.add_hotkey('space', on_key_press_space)
# keyboard.add_hotkey('c', on_key_press_c)
# keyboard.wait()
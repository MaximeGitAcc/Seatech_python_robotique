import keyboard
from exo1_starter_template import Robot

CreationRobot = input("Bienvenue chez Aperture, voulez-vous créer un nouveau robot ? ")
if CreationRobot == "Oui" or CreationRobot == "oui":
      r1 = Robot()

else :
      print("Vous n'avez pas l'argent c'est ça ? Sortez tous de suite de notre magasin !")

print("Voici les fonctionnalités dont je dispose :\n- M'allumer (allumer avec 'a')\n- M'éteindre (eteindre avec 'e')\n- Aller me mettre en charge (charge avec 'r')\n- Afficher mon pourcentage de Batterie en charge(Batterie avec 'b')\n- Avancer avec une certaine vitesse (Avancer avec 'z')\n- Reculer avec une certaine vitesse (Reculer avec 's')\n- S'arrêter net sur demande (Stop avec 'space')\n- Donner les caractéristiques du robot (Carac avec 'c')")

def on_key_press_a(event):
      print(f"You pressed {event.name}")

def on_key_press_e(event):
     print(f"You pressed {event.name}")

def on_key_press_r(event):
     print(f"You pressed {event.name}")

def on_key_press_b(event):
     print(f"You pressed {event.name}")

def on_key_press_z(event):
     print(f"You pressed {event.name}")

def on_key_press_s(event):
     print(f"You pressed {event.name}")

def on_key_press_space(event):
     print(f"You pressed {event.name}")

def on_key_press_c(event):
     print(f"You pressed {event.name}")

keyboard.add_hotkey('a', on_key_press_a)
keyboard.add_hotkey('e', on_key_press_e)
keyboard.add_hotkey('r', on_key_press_r)
keyboard.add_hotkey('b', on_key_press_b)
keyboard.add_hotkey('z', on_key_press_z)
keyboard.add_hotkey('s', on_key_press_s)
keyboard.add_hotkey('space', on_key_press_space)
keyboard.add_hotkey('c', on_key_press_c)
keyboard.wait()
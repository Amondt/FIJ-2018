#import de la fct 'randrange' de la librairie random
from random import randrange

#init diff var
reponse = randrange(1,10) #génère un nombre aléatoire entre 1 et 10
entree = 0
compteur = 10

#tant que entree est dif de reponse et que compteur est plus grand que 0, la boucle continue
while entree != reponse and compteur > 0:

  entree = int(input('Entre un nombre entre 1 et 10 :')) #attend une entree de l'utilisateur
  compteur -= 1

  if entree < reponse:
    print('La réponse est plus grande')
  elif entree > reponse:
    print('La réponse est plus petite')
  else:
    print('Bravo !')

if compteur == 0:
  print('Tu as perdu !')

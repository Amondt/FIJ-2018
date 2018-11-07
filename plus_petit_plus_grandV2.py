from random import randrange

def mauvaise_entree(nombre):
  if nombre > 10:
    return False
  elif nombre < 1: 
    return False
  else: return True

continuer = 'o'
while continuer == 'o':

  reponse = randrange(1, 10)
  entree = -1
  essai_max = 5
  erreur = False
  while reponse != entree and essai_max > 0:

    while not erreur :
      entree = int(input('Tappez un nombre entre 1 et 10 : '))
      erreur = mauvaise_entree(entree)

    if entree < reponse:
      print('La réponse est plus grande\n')
    elif entree > reponse:
      print('La réponse est plus petite\n')
    else:
      print('Bravo, vous avez trouvé la bonne réponse !\n')
    
    erreur = False
    essai_max -= 1

  if essai_max == 0 and reponse != entree:
    print('Vous avez perdu, le nombre était', reponse, '\n')

  print('Voulez vous rejouer ? o/n')
  continuer = input()
  print('\n')

Liste = []
valeurInput = input("Entrez vos valeurs : ")
if valeurInput != "": # tant que l'utilisateur ne rentre pas d'entrée (espace vide)
       Liste.append(valeurInput) # on entre l'input dans la liste
print(sorted(Liste))

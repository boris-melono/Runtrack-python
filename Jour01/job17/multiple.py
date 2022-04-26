for i in range(1, 100):                    # Entiers de 1 à 100
    if ((i % 3) == 0) and ((i % 5) == 0):  # Multiple de 3 *et* de 5
        print('FIZZ BUZZ!', end=' ')       # Affichage sans retour à la ligne
    elif (i % 3) == 0:                     # Multiple de 3 uniquement
        print('Fizz!', end=' ')
    elif (i % 5) == 0:                     # Multiple de 5 uniquement
        print('Buzz!', end=' ')
    else:
        print(i, end=' ')
print()   
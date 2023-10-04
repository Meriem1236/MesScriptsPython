#Ecrire un programme qui choisi le plus grand nombre parmi deux nombre saisi a partir du clavier
nombre1 = int(input("Entrez le premier nombre :\n "))
nombre2 = int(input("Entrez le deuxième nombre :\n "))

# Compare les deux nombres
if nombre1 > nombre2:
    print ("le nombre le plus grand est :" ,nombre1)
elif nombre1 < nombre2:
    print ("le nombre le plus grand est :" ,nombre2)
else:
    print ("les nombres sont egaux")

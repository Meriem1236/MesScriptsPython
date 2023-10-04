#ecrire un programme qui va trouver le plus grand nombre parmi 3 nombres saisi a partir du clavier
nombre1 = int(input("Entrez le premier nombre : "))
nombre2 = int(input("Entrez le deuxième nombre : "))
nombre3 = int(input("Entrez le troisième nombre : "))


if nombre1 >= nombre2 and nombre1 >= nombre3:
    print("Le plus grand nombre est :", nombre1)
elif nombre2 >= nombre1 and nombre2 >= nombre3:
    print("Le plus grand nombre est :", nombre2)
else:
    print("Le plus grand nombre est :", nombre3)


# Découpage d'une cjaine de caractères (Slicing)
college = "Collège Bois de Boulogne "
print(college[0])
print(college[8])
print(college[21])
  #Afficher les caractères dans le sens inverse
print(college[-1])
print(college[-2])

 #Afficher un moceau de caractère
print(college[8:12])
print(college[16:24])
print(college[-9:-1])

 #Afficher les caractères de 0 à 20 avec un pas=2
print(college[0:20:2])

 #Afficher les caractères de 0 à 20 avec un pas=3
print(college[0:20:3])

 #Afficher la taille de la chaine de caractère "len"
print(len(college))

 #Afficher toute la chaine de caractére inversée
print(college[:])
#print(college[start:end:step])
print(college[::])

 #Afficher toute la chaine de caractére inversée
print(college[::-1])


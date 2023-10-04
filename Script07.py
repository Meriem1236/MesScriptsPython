#ecrire un programme qui va lire les données d'un employé a partir du clavier puis les afficher
#identifiant, nom, salaire, adresse, marié ou nom

#Solution Meriem:
identifiant = input("Entrez l'identifiant de l'employé : ")
nom = input("Entrez le nom de l'employé : ")
salaire = float(input("Entrez le salaire de l'employé : "))
adresse = input("Entrez l'adresse de l'employé : ")
est_marie = input("L'employé est-il marié (Oui/Non) : ")
#est_marie = bool(input("est ce que vous etes marié? [true|false]"))

# Afficher les informations de l'employé
print("\nInformations de l'employé :")
print("l'indetifiant est :" ,identifiant)
print("Le nom est :" ,nom)
print("Le salaire est :" ,salaire)
print("L'adresse est :" ,adresse)
print("Marié! :" ,est_marie)



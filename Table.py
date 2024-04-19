from prettytable import PrettyTable

# Spécifiez les noms de colonnes lors de l'initialisation du tableau
myTable = PrettyTable(["Nom de l'étudiant", "Classe", "Section", "Pourcentage"])

# Ajoutez des lignes
myTable.add_row(["Leonard", "X", "B", "91.2 %"])
myTable.add_row(["Penny", "X", "C", "63.5 %"])
myTable.add_row(["Howard", "X", "A", "90.23 %"])
myTable.add_row(["Bernadette", "X", "D", "92.7 %"])
myTable.add_row(["Sheldon", "X", "A", "98.2 %"])
myTable.add_row(["Raj", "X", "B", "88.1 %"])
myTable.add_row(["Amy", "X", "B", "95.0 %"])

print(myTable)

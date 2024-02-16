# Fonction 
def est_pair (nombre):
    return nombre % 2 == 0

nombre = int(input("entrez un nombre: "))
if est_pair(nombre):
    print("Le nombre est pair.")
else: print("Le nombre est impair. ")
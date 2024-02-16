# Playground to execute py codeBattle exercices

# EXERCICE 13:
#
# user_to_upper = str(input("Texte à passer en majuscules: "))
#
# for letter in user_to_upper:
#     print(letter.upper())

# EXERCICE 14:
#
# n = 10
#
# for i in range(n, 0, -1):
#     print(i)


# EXERCICE 15
#
# user_number_choice = int(input("Nombre de fin de séquence: "))
# firstValue = 1
#
# while firstValue <= user_number_choice:
#       print(firstValue)
#       firstValue += 2

# EXERCICE 16
#
# user_password = "someWord"
# password_prompt = str(input("Mot de passe : "))
#
# while user_password != password_prompt:
#    print("Mot de passe incorrect.")
#    password_prompt = str(input("Mot de passe : "))

# EXERCICE 17
#
# def aire_rectangle(longueur, largeur):
#    aire = longueur*largeur
#    return aire
#
# rectangle_longueur = int(input("Longueur : "))
# rectangle_largeur = int(input("Largeur : "))
#
# rectangle_one = aire_rectangle(rectangle_longueur, rectangle_largeur)
# print(rectangle_one)

# EXERCICE 18
# someFloat = 0.0

# def est_pair(number):
#    if number % 2 == 0:
#        # print("Pair")
#        return True
#    else:
#        # print("Impair")
#        return False
#
# some_number = float(input("Nombre ? : "))
#
# checkUser = est_pair(some_number)
# print(checkUser)

# EXERCICE 19
#
# def est_mot_valide(somePanty):
#   if somePanty.isalpha() == True:
#       return True
#   else:
#       return False
#
# userWord = input("Saisir le mot: ")
# checkWordInput = est_mot_valide(userWord)
# print(checkWordInput)

# EXERCICE 20
# def celsius_vers_fahrenheit(celsius):
#    fahrenheit = celsius * 9 / 5 + 32
#    return fahrenheit
#
# tempInCelsus = float(input("Température en Celsius : "))
# computedTemp = celsius_vers_fahrenheit(tempInCelsus)
# print(computedTemp)

# EXERCICE 21

oasis = ["mangue", "ananas", "framboise", "fraise"]
print(oasis)

# EXERCICE 22

chineseDict = {"fanguan": "restaurant", "guojia": "hometown", "erzi": "fils"}
print(chineseDict)

# EXERCICE 23

chineseDict["fanbianmian"] = "nouilles instantanées"
print(chineseDict)

oasis.append("kaki")
print(oasis)

# EXERCICE 24

oasis.append("banane")
print(oasis)
del oasis[5]
print(oasis)
oasis.remove("kaki")
print(oasis)

# EXERCICE 25

extractElement = oasis[2]
print(extractElement)

# EXERCICE 26
oasis.append("pomme")
print(oasis)
oasis[4] = "poire"
print(oasis) 

# EXERCICE 27

for fruit in oasis:
    print(fruit)

# EXERCICE 28
    
if "fraise" in oasis:
    print("Elle ramène sa fraise") 

# EXERCICE 29

# for item in chineseDict:
#    print(item) 
# for value in chineseDict.values():
#    print(value)

# for cle in chineseDict:
#    keyPair = cle.items()
#    print(keyPair)
    
for cle, value in chineseDict.items():
    print(cle, value)

# EXERCICE 30
    
chineseDict["zhongguo"] = "Chine"
print(chineseDict)

# EXERCICE 31

del chineseDict["zhongguo"]
print(chineseDict)

# EXERCICE 32

print(len(oasis))
print(oasis)

# EXERCICE 33

for key, value in chineseDict.items():
    print(key) 
print(chineseDict)

# Méthode donnée par la solution : on prend seulement la première valeur (la clé) et on n'a pas besoin de la fonction items():
for key in chineseDict:
    print("La clé : ", key)

# EXERCICE 34

for key, value in chineseDict.items():
    print("La valeur est : ", value)

# La correction donne la méthode suivante:
    
for value in chineseDict.values():
    print("Correction - value = ", value)

# EXERCICE 35

print('chien' in chineseDict)
# On peut aussi faire avec if...in... 

# EXERCICE 36
print(oasis)
oasisInOne = ' '.join(oasis)
print(oasisInOne)

# EXERCICE 37
print(oasis)
oasis.clear()
print(oasis)

# EXERCICE 38
print(chineseDict)
chineseDict.clear()
# Marche mais je me suis compliqué la vie: dict.clear(chineseDict)
print(chineseDict)

# EXERCICE 39

def ajouter_element_list(liste, element):
    liste.append(element)
    return liste
    # return newList

someValue = [1, 2, 3, 4, 5]
# newValues = someValue().ajouter_element_list()

newValue = ajouter_element_list(someValue, 6)
print(f"Liste: {newValue}")

# EXERCICE 40


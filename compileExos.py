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

def est_pair(number):
    if number % 2 == 0:
        print("Pair")
        return True
    else:
        print("Impair")
        return False

some_number = float(input("Nombre ? : "))

checkUser = est_pair(some_number)
print(checkUser)
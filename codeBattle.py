# EXERCICE 1

myName = "mon Prénom"
myAge = 37

introduceMyself = "J'ai {} ans et je m'appelle {}.".format(myAge, myName)
print(introduceMyself) 

# EXERCICE 2

userAge = int(input("Quel est votre âge ? "))

if userAge >= 18:
    print("Majeur")
else:
    print("Mineur")

# EXERCICE 3
    
todaysWeather = str(input("Quelle météo aujourd'hui ? "))

if todaysWeather == "soleil":
    print("En maillot")
elif todaysWeather == "pluie":
    print("Parapluie")
elif todaysWeather == "nuage":
    print("Couvre toi")
elif todaysWeather == "neige":
    print("Reste chez toi")
elif todaysWeather == "brouillard":
    print("Feux anti-brouillard")
else:
    print("ZzzZZzz")

# EXERCICE 4:

whatsDayToday = str(input("Quel jour de la semaine ? "))
whatsDayTodayParsed = whatsDayToday.lower()

if whatsDayTodayParsed == "lundi":
    print("PHP 01")
elif whatsDayTodayParsed == "mardi":
    print("PHP 02")
elif whatsDayTodayParsed == "mercredi":
    print("PHP 03")  
elif whatsDayTodayParsed == "jeudi":
    print("PYTHON 04")  
elif whatsDayTodayParsed == "vendredi":
    print("PYTHON 05")  
elif whatsDayTodayParsed == "samedi":
    print("Dormir")  
else:
    print("Dimanche: encore dormir") 

# EXERCICE 5: 

offerProducts = ["thé", "café", "jus de fruits"]
userChoice = input("Choix de boisson :") # f{.join(offerProducts)}

if userChoice in offerProducts:
    print(userChoice)
else:
    print("Choix de boisson non disponible")

# EXERCICE 6:
from enum import Enum

class Mood(Enum):
    HAPPY = "Heureux".lower()
    SAD = "Triste".lower()
    AWKWARD = "Comme çi comme ça".lower()
userMoodInput = input("Quelle est votre humeur ? ")
userMood = userMoodInput.lower()

if userMood in Mood:
    # print("Votre humeur est disponible ici")
    if userMood == Mood.HAPPY.value:
        print(f"{Mood.HAPPY.value}: c'est cool, faites du sport !")
    elif userMood == Mood.SAD.value:
        print(f"{Mood.SAD.value}: c'est pas cool, regardez Netflix !")
    else:
        print(f"{Mood.AWKWARD.value}: allez ça va le faire ! Un petit exo en Python ?")
else:
    print("Nouvelle saisie")

# EXERCICE 7:
    
class Meal(Enum):
    PIZZA = "pizza"
    SANDWICH = "sandwich"
    SALAD = "salade"

userMealInput = input("Choix du plat: pizza / sandwich / salade ")
userMeal = userMealInput.lower()

if userMeal == Meal.PIZZA.value:
    print(f"Okay, {Meal.PIZZA.value} !")
elif userMeal == Meal.SANDWICH.value:
    print(f"Okay, {Meal.SANDWICH.value}")
else:
    print(f"Okay, {Meal.SALAD.value}")

# EXERCICE 8:

userDayInput = input("Jour de la semaine ? ")
userDaySelect = userDayInput.lower()

if userDaySelect == "Lundi".lower():
    print("Breaking Bad")
elif userDaySelect == "Mardi".lower():
    print("Koh Lanta")
elif userDaySelect == "Mercredi".lower():
    print("Les experts")
elif userDaySelect == "Jeudi".lower():
    print("Taken")
elif userDaySelect == "Vendredi".lower():
    print("DALS")
elif userDaySelect == "Samedi".lower():
    print("The Voice")
elif userDaySelect == "Dimanche".lower():
    print("Le film du dimanche soir")
else:
    print("Erreur")

# EXERCICE 9:

selectAnimal = input("Chat chien ou poisson ? ")
print("Vous avez sélectionné ", selectAnimal)

# EXERCICE 10:
userInputSelectBook = input("Aventure, Romance, Science Fiction ? ")
selectBook = userInputSelectBook.lower()
# print("Je vous recommande des livres dans le thème de: ", selectBook)

class BookType(Enum):
    AVENTURE = "Aventure"
    ROMANCE = "Romance"
    SCFI = "Science Fiction"

if selectBook == BookType.AVENTURE.value.lower():
    print("Je vous recommande de lire Moby Dick")
elif selectBook == BookType.ROMANCE.value.lower():
    print("Je vous recommande de lire \"Et soudain tu es là\" de Cécile Violette")
elif selectBook == BookType.SCFI.value.lower():
    print("Je vous recommande de lire Hunger Games")
else:
    print("Découverte par sérendipité ON !")

# EXERCICE 11:

allVowels = ["a", "e", "i", "o", "u", "y"]
userWordInput = input("Mot à parser: ")

for i in userWordInput:
    if i in allVowels: # ajouter .lower() à i et on peut passer les voyelles direct après "in"
        print(i)

# EXERCICE 12:
        
user_number = int(input("Jusqu'à quel chiffre passer à l'affichage ? "))
i = 1

while i <= user_number:
    print(i)
    i += 1

# EXERCICE 13:

user_to_upper = str(input("Texte à passer en majuscules: "))

for letter in user_to_upper:
    print(letter.upper())

# EXERCICE 14:

n = 10

for i in range(n, 0, -1):
    print(i)

# EXERCICE 15

user_number_choice = int(input("Nombre de fin de séquence: "))
firstValue = 1

while firstValue <= user_number_choice:
    print(firstValue)
    firstValue += 2

# EXERCICE 16

user_password = "someWord"
password_prompt = str(input("Mot de passe : "))

while user_password != password_prompt:
    print("Mot de passe incorrect.")
    password_prompt = str(input("Mot de passe : "))
print("Accès OK")

# EXERCICE 17

def aire_rectangle(longueur, largeur):
    aire = longueur*largeur
    return aire

rectangle_longueur = int(input("Longueur : "))
rectangle_largeur = int(input("Largeur :"))

rectangle_one = aire_rectangle(rectangle_longueur, rectangle_largeur)
print(rectangle_one)

# EXERCICE 18


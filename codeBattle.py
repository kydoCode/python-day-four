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
    HAPPY = "Heureux"
    SAD = "Triste"
    AWKWARD = "Comme çi comme ça"

userMood = input("Quelle est votre humeur ? ")

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



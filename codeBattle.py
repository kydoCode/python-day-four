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
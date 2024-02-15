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
elif todaysWeather == "neige":
    print("Reste chez toi")
elif todaysWeather == "brouillard":
    print("Feux anti-brouillard")
else:
    print("ZzzZZzz")
    

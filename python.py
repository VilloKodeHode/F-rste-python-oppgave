import random

first_name = "Joakim"
last_name = "Villo"
full_name = first_name + ' ' + last_name
print(full_name)

def make_pizza(topping ='bacon'): print("Have a " + topping + " pizza!")
    
make_pizza()
make_pizza('pineapple')

randomNumber = random.randint(0,10)
if randomNumber > 5 : print("Number is less than 5")
elif randomNumber < 5 : print("Number is greater than 5")
else : print("Number is 5")

print("RandomNumber is: " + str(randomNumber))    
    
# num = 10
# print(num)

user_array = [
    {
    "name": "Jolyene", 
    "age" : "22"
    },
    {
    "name": "Bob", 
    "age" : "54"
    },
    {
    "name": "Walter", 
    "age" : "78"
    },
    ]

names = [person['name'] for person in user_array]
age = [person['age'] for person in user_array]

print(str(names[0]) + ' ' + str(age[0]))

for person in user_array:
    name = person['name']
    age = person['age']
    print(f"{name} is {age} years old")
    
user_to_find = "Bob"

for person in user_array:
    if person['name'] == user_to_find:
        name = person['name']
        age = person['age']
        print(f"{name} is {age} years old")
        break
    
# Første oppgave i Python:
    
#Oppgave 1
    
mathStatement = 40 + 10
if mathStatement == 50 : print("mathStatement with 'addition' is 50")    
elif mathStatement != 50 : print("mathStatement with 'addition' is NOT 50 ")
    

#Oppgave 2:

mathStatement = 40 % 10
if mathStatement == 0 : print("mathStatement with 'modulo' is 0")    
elif mathStatement != 0 : print("mathStatement with 'modulo' is NOT 0")

#Oppgave 3:

#allerede gjort i oppgave 1 og 2?

#Oppgave 4 og 5:
    
    
chosenNumber = 5
numberlist = [100,321,3432,4654,87865,786,7324,81231,9876,16540,1341,132422,12313,165464,13125,16564436]
randomNumberFromList = random.choice(numberlist)
if randomNumberFromList == chosenNumber : print("number is chosen by coder and will not be shown") 
else : print("number from list is " + str(randomNumberFromList))
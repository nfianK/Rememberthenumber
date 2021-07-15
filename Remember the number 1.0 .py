import os #to clean the screen
import time #import time to have a 'delay' as time.sleep()
import random #to generate a random number to remember
from sys import platform #to know which platform we are using

def cls(): #define clear screen
    if platform  == "win32": 
        os.system("cls") # Clear screen just for Windows
    else:
        os.system('clear')  # Clear screen for Mac or Linux
        
def choose_language():
    while True:
        try:
            language = int(input('Choose a language/Elige un idioma. 0 English/Ingles, 1 Spanish/Español: ')) 
            return language
        except: #fix error
            print('\nInput a number, not a word/Ingresa un numero, no una palabra')
            time.sleep(2)
            cls()

def play_english():
    cls()
    option = True
    streak = 0
    while True:
        try:
            digits = int(input('How many digits do you want at the beginning? '))
            break
        except:
            cls()
            print("Empty values and words are not valied. Your streak was {streak}")
            time.sleep(1)
    cls()
    while  (option):
        #generate a random number and show it on the screen
        number = random.randint(10**(digits-1), 10**digits - 1)
        print(f"\tUse your memory \t\tstreak: {streak}")
        print(f"\nRemeber this number {number}")
        during = int(len(str(number))/2) + 1 #define the time of 'delay'
        time.sleep(during)        
        cls()
        try:
            user_number = int(input("The number was... "))
        except:
            print(f"\nEmpty values and words are not valied. Your streak was {streak}") #fix a error
            input("\nPress 'enter' to exit")
            break
        option = number == user_number #define if the number is wrong or is correct
        if option:
                input("\nCongratulations! Press 'enter' for the next number")
                cls()
        else:
            print(f"\nYou failed .The number was {number}. Your streak was {streak}")
            input("\nPress 'enter' to exit")
            break
        digits +=1
        streak += 1
    

def play_spanish(): #the same than play_english but in spanish
    cls()
    option = True
    streak = 0
    while True:
        try:
            digits = int(input("Con cuantas cifras queres empezar?"))
            break
        except:
            cls()
            print("Valores vacios y palabras no son validos. Intenta devuelta\n")
            time.sleep(1)
    cls()
    while  (option):
        number = random.randrange(10**(digits-1), 10**digits - 1)
        print(f"\tUsa tu memoria \t\tracha: {streak}")
        print(f"\nRecuerda este numero {number}")
        during = int(len(str(number))/2) + 1
        time.sleep(during)
        cls()
        try:
            user_number = int(input("Cual era el numero?: "))
        except:
            print(f"\nValores vacios y palabras no son validos. Tu racha fue {streak}")
            input("Presiona enter para salir")
            break
        option = number == user_number
        if option:
                input("\nFelicitaciones!.Presiona 'enter' para el proximo numero ")
                cls()
        else:
            print(f"\nEl numero era {number}. Tu racha fue {streak}")
            input("\nPresiona 'enter' para salir'" )
            break
        digits +=1
        streak += 1

language = choose_language()

if language == 0:
    play_english()
elif language == 1:
    play_spanish()
else:
    print("\nThis option doesn't exist")

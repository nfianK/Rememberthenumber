import os #to clean the screen
import time #import time to have a 'delay' as time.sleep()
import random #to generate a random number to remember
from sys import platform #to know which platform we are using

def cls(): #define clean the screen
    if platform  == "win32": 
        os.system("cls") # Clear just for Windows
    else:
        os.system('clear')  # Clear for Mac or Linux
        
def chosse_langue():
    while True:
        try:
            langue = int(input('Chosse a langue/Elige un idioma. 0 English/Ingles, 1 Spanish/Español: ')) 
            return langue
        except: #fix error
            print('\nInput a number, not a word/Ingresa un numero, no una palabra')
            time.sleep(2)
            cls()

def play_english():
    cls()
    option = True
    during = 2 #define the time of 'delay'
    streak = 0
    digits = int(input('How many digits do you want at the beging? '))
    cls()
    while  (option):
        #generate a random number and show it on the screen
        number = random.randrange(10**(digits-1), 10**digits - 1)
        print(f"\tUse your memory \t\tstreak: {streak}")
        print(f"\nRemeber this number {number}")
        time.sleep(during)
        if during<5: during +=1
        cls()
        try:
            user_number = int(input("Which was the number: "))
        except:
            print(f"\nEmpty values are not valied. Your streak was {streak}") #fix a error
            input("\nPress 'enter' to exit")
            break
        option = number == user_number #define if the number is wrong or is correct
        if option:
                input("\nCongratulations! Press 'enter' for the next number")
                cls()
        else:
            print(f"\nThe number was {number}. Your streak was {streak}")
            input("\nPress 'enter' to exit")
            break
        digits +=1
        streak += 1
    

def play_spanish(): #the same than play_english but in spanish
    cls()
    option = True
    during = 2
    streak = 0
    digits = int(input("Con cuantas cifras queres empezar?"))
    cls()
    while  (option):
        number = random.randrange(10**(digits-1), 10**digits - 1)
        print(f"\tUsa tu memoria \t\tracha: {streak}")
        print(f"\nRecuerda este numero {number}")
        time.sleep(during)
        if during<5: during +=1
        cls()
        try:
            user_number = int(input("Cual era el numero?: "))
        except:
            print(f"\nValores vacios no son validos. Tu racha fue {streak}")
            input("Preciona enter para salir")
            break
        option = number == user_number
        if option:
                input("\nFelicitaciones!.Preciona 'enter' para el proximo numero ")
                cls()
        else:
            print(f"\nEl numero era {number}. Tu racha fue {streak}")
            input("\nPresiona 'enter' para salir'" )
            break
        digits +=1
        streak += 1

if chosse_langue() == 0:
    play_english()
else:
    play_spanish()

import colorama
from colorama import Fore, Back, Style
print(Back.BLACK + Fore.RED + Style.BRIGHT + "Welcome to BILL PAY ROULETTE!!!" + Style.RESET_ALL)
names_string = input(Style.BRIGHT + "Give me everybody's names, separated by a comma: \n")
names = names_string.split(", ")
friends_number = len(names) - 1
# print(len(names))
# print(friends_number)
import random
number_to_pay = random.randint( 0, friends_number)
# print(number_to_pay)
print(Fore.RED + Style.BRIGHT + "THE BILL IS ON: " + Back.BLACK + f"{names[number_to_pay]}" + Style.RESET_ALL)



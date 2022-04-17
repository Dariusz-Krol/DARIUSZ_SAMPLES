import colorama
from colorama import Fore, Back, Style
print(Back.BLACK + Fore.RED + Style.BRIGHT + "Welcome to the tip calculator!!!" + Style.RESET_ALL)
print(Fore.GREEN + "Please follow below instructions: ")
print(Fore.GREEN + "Enter digits for money and %, and TEXT for currency.")
print(Fore.GREEN + "Use a dot as a separator for decimal (cents) on the bill.")
print(Back.BLACK + Fore.RED + Style.BRIGHT + "LET's GO!!!" + Style.RESET_ALL)
print()
currency = str(input(Style.BRIGHT + "INPUT symbol of your currency: "))
total_bill = float(input(f"INPUT the total bill value in {currency}: "))
number_of_people = int(input("How many people to split the bill?: " + Style.RESET_ALL))
continue_calculating = True
while continue_calculating:
    tip_percent = float(input(Style.BRIGHT + "How many tip % would you would like to give? % = " + Style.RESET_ALL))
    print()
    # waiter need to get amount including the tip:
    total_bill_with_tip = total_bill * float(1 + tip_percent/100)
    #in case when float(1 + tip_percent/100) is not declared as float, we are getting wrong result i.e it's like INT
    total_bill_with_tip_rounded = round(total_bill_with_tip, 2 )
    total_bill_with_tip_rounded_format = "{:.2f}".format(total_bill_with_tip_rounded)
    print(Fore.RED + Style.BRIGHT + Back.BLACK + "CALCULATION RESULTS:"  + Style.RESET_ALL)
    print()
    print(Fore.RED + f"TOTAL BILL TO PAY INCLUDING TIP IS: " + Back.BLACK + f" {currency} {total_bill_with_tip_rounded_format}" + Style.RESET_ALL)
    share_per_person = float(total_bill_with_tip / number_of_people)
    share_per_person_rounded = round(share_per_person, 2 )
    share_per_person_rounded_formated = "{:.2f}".format(share_per_person_rounded)
    print(Fore.RED + f"Each person should pay: " + Back.BLACK + f"{currency} {share_per_person_rounded_formated}" + Style.RESET_ALL)
    print(Fore.RED + "...to pay the total sum properly including tip")
    tip_value = total_bill * tip_percent/100
    tip_value_formated = "{:.2f}".format(tip_value)
    print(f"TIP VALUE IS: "+ Back.BLACK + f"{currency} {tip_value_formated}" + Style.RESET_ALL)
    SUM_1 = total_bill + tip_value
    SUM_1_formated = "{:.2f}".format(SUM_1)
    print()
    print(Fore.BLUE + "JUST A DOUBLE-CHECK:")
    print(f"check 1: total_bill + tip_value = {currency} " + SUM_1_formated)
    SUM_2 = share_per_person * number_of_people
    SUM_2_formated = "{:.2f}".format(SUM_2)
    print(f"check 2: share_per_person * number_of_people = {currency} " + SUM_2_formated)
    print()
    response = input(Back.BLACK + Fore.RED + Style.BRIGHT + f"Type 'y', if you want to change TIP %, otherwise type: 'n' to stop this calculation.\n" + Style.RESET_ALL)
    print()
    response = response.lower()
    if response == "n":
        print()
        print(f"TIP VALUE WILL STAY AS IT IS: " + Fore.RED + f"{currency} {tip_value_formated}" + Style.RESET_ALL)
        print()
        print(Back.BLACK + Fore.GREEN + Style.BRIGHT + "THANK YOU FOR USING TIP CALCULATOR" + Style.RESET_ALL)
        continue_calculating = False
    elif response == "y":
        continue_calculating = True

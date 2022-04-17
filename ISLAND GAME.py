print()
print("WELCOME TO THE GAAAAAAAME!!! It's name is TREASURE ISLAND")
print('''
    0000000         000           000     000         00000000          
   00     00       00 00         00 00   00 00        0
   00             00   00       00   00 00    00      0000000
   00   0000     00 000 00     00     000      00     0
   00     00    00       00   00                00    0         
    0000000     00       00   00                00    00000000 
''')
print("Your aim is to find treasure on Treasure Island")
just_word = input("ARE YOU READY YES or NO? ")
just_word = just_word.lower()
if just_word == "yes":
    print()
    print("THEN GO !!! READ INSTRUCTIONS CAREFULLY AND INPUT YOUR RESPONSES WITHOUT MISTAKES and TYPOS")
    print('''
    ,adPPYb,d8  ,adPPYba,   
   a8"    `Y88 a8"     "8a  
   8b       88 8b       d8  
   "8a,   ,d88 "8a,   ,a8"  
    `"YbbdP"Y8  `"YbbdP"'   
            aa,                
      "Y8bbdP"       
    ''')
else:
    print()
    print("OK THEN COME BACK WHEN YOU ARE READY")
    exit()
print()
print("You have to start and every trip is starting from the first step, uahahahahaha!")
direction_1 = input("So? where you want to go: LEFT or RIGHT?\n").lower()
if direction_1 == "left":
   print()
   print("OK, you are still alive, so now you approaching a river.")
   direction_2 = input("Do you want to WAIT for a boat or SWIM?\n").lower()
   if direction_2 == "wait":
      print()
      print("Good choice! Now you arrived to the Treasure Island")
      print("On the enter to the Island you see big gates: RED, Yellow, and Blue")
      direction_3 = input("Which door you choose?\n").lower()
      if direction_3 == "yellow":
          print()
          print("WOW! GOOD CHOICE! You won and the treasure is yours. Congratulations")
          exit()
      elif direction_3 == "blue":
          print()
          print("You have been eaten by a big beast! Sorry: GAME OVER")
      #     exit()
      elif direction_3 == "red":
          print()
          print("You have been burned by fire! Sorry: GAME OVER")
      else:
          print()
          print("WrOnG InPuT: GAME OVER")
          # exit()
   else:
    print()
    print("You just met with a crocodile and you are now it's sandwich. ")
    print("GAME OVER")
    exit()
else:
   print()
   print("You just fall into a big WHOLE")
   print("GAME OVER")
   exit()





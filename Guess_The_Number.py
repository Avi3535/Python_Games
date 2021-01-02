# The computer generates a random number and the user will guess it.

import random as r

def guess_num():
  
  guess = int(input("Guess the temperature from 1 to : "))
  if (guess <= 0) : 
    print("Please Enter a Number greater than 1 ")
    guess_num()

  rand_num = r.randint(1,guess)

  inp_val = 0
  while(1):
    inp_val = int(input("Okay guess the number... "))
    if (inp_val < (rand_num/2)) : print("It's Freezing")
    elif (inp_val > (rand_num+(rand_num/2))) : print("It's burning hot")
    elif (inp_val < (rand_num)) : print("Colder")
    elif (inp_val > (rand_num)) : print("Warmer")
    elif  (inp_val == (rand_num)):

      print("THAT'S IT! It's comfortable")
      ans = input("Do you want to play again(y/n)/ " ).lower()
      if (ans == "y"): guess_num()
      elif (ans == "n"): return

guess_num()

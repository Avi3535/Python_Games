## The user will enter a number and the computer will try to guess it

import random as r

def comp_guess():
  ent_val = int(input("Enter value to be guesses by the computer : "))
  print("Okay you have enetered a value.")
  print("The computer is guessing...")
  low_val = 1
  high_val = 2*ent_val
  while (1) :
    get_ran = r.randint(low_val, high_val)
    print("Umm.. is ", get_ran, "high(h) or low(l) or is did I guess(c) it")
    inp_val = input("(h)/(l)/(c)").lower()
    if (inp_val == "l") : low_val = get_ran
    elif (inp_val == "h") : high_val = get_ran
    elif  (inp_val == "c"):
      print("The value was ", get_ran)
      print("I guessed it... This is just the beginning")
      ans = input("Do you want to play again(y/n)// " ).lower()
      if (ans == "y"): comp_guess()
      elif(ans == "n"): return  

comp_guess()

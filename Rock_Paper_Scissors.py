## Rock, Paper, Scissors

import random as r

def one_two_three():
  inp = input("Rock(r), Paper(p) or Scissors(s)// ").lower() 

  get_rand = r.choice(["r", "p", "s"])

  print("You chose", inp,"I chose ",get_rand)

  if(inp == get_rand):
    print("Ah! It's a tie... Let's settle this.")
    one_two_three()

  elif ((inp == "r") and (get_rand == "s")) or ((inp == "p") and (get_rand == "r")) or ((inp == "s") and (get_rand == "p")) :
    print("Okay. You won..")  
    print("Let me try again.")

  else :
    print("I Won!!! This is just the beginning...")
    print("Do you want to try again//")

  ans = input("Want to play again (y/n)// : ").lower()
  if (ans == "y"):
      one_two_three()
  elif (ans == "n"):
      return 0

one_two_three()

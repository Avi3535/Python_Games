def say_jumanji():
  ans = input("But did it/ ").upper()
  if(ans == "JUMANJI"):
    print("GREAT WORK! You have won.")
  else:
    say_jumanji()
def check_val():
  a = 1
  ans = int(input("Which number is missing..."))
  if(ans == 15): 
    print("Nice. You survived. The game should end...")
    print()
    say_jumanji()
  elif (a<=3) :
    a-=1
    print("Come On try again. Oh no the bandits...")
    check_val()
  else :
    print("You lost your life. You took too many try's")
    


def start():
  age = int(input("What is your age..."))

  if(age >= 18):
    print("Nice. This game isn't for children.")

  elif (age < 18 and age >= 0):
    print("Oh! Try again in ",(18-age), " year(s)")

  else : 
    print("Okay... That's funny!")

  ans = input("Wait! What's your name by the way... ")

  print("Hey ", ans,"!")

  print("This is an adventure game which ends at JUMANJI. Okay its similar to the Movie - Jumanji and is a a low budget one...")
  print("You have 3 lives...")
  lives = 3
  print("You've just woken up with an old wooden bridge at your right.")

  ans = input("Quickly decide you have bandits chasing you. Now do you want to go the right or left ").upper()

  if(ans == "RIGHT"):
    print(ans," Good Thinking. The wooden bridge had to be empty and the bandits were coming from the left.")

  elif (ans == "LEFT") :
    lives-=2
    print("Oh! you decided you fight 20 bandits. You lost 2 lives... Well fought")
  else :
    lives = 0
    print("You lost all your lives...")
  print("You have ", lives, "lives remaining.")

  if(lives>0):
    print("This activity checks if you give attention to detail.")
    print("The bandits have some how found their way...")
    print("You need find the correct number else you'll lose your last life.")
    
    ans = input("Are you ready/ ").lower()
    if(ans == "yes"):
      for x in range (0,20):
        if (x == 15): x +=1
        print(x)
      print("Hurry! ")
      check_val()
    elif(ans == "no"):
      print("Huh! There's no escape from the bandits")

  else:
    print("You have to be serious in some situations...")
    print("You lost.")

print(" This is a simple game")
ans = input("Do you want to play ").lower()
if(ans == "yes"):
  print("Let's see if you win. There's no turning back")
  start()

else:
  print("Anyways this game isn't for the faint hearted")


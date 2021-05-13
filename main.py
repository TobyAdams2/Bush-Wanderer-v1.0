import random
from time import sleep
import os

#this is just like a rules thing, the ---- thing is there to break up the rules into parts, just for readability and the look i suppose.
print("~~~~~~Bush Wanderer~~~~~~")
sleep(2)
print("The rules of the game are as follows:")
sleep(0.2)
print("-------------------------------------")
sleep(2)
print("1. You are a bush wanderer")
sleep(0.2)
print("- Your position on the board is marked by \033[1;32mx\033[0;0m")
sleep(0.2)
print("-------------------------------------")
sleep(2)
print("2. On the board there is a secret chest.")
sleep(0.2)
print("- You must work your way around the board to reach the chest.")
sleep(0.2)
print("- However, this chest is hidden from you, it is not marked on the board.")
sleep(0.2)
print("- If and when you land on the chest, you will win and the game will end.")
sleep(0.2)
print("-------------------------------------")
sleep(2)
print("3. Also on the board with you is a blind but dangerous dragon")
sleep(0.2)
print("- This dragon is represented by the symbol \033[1;31m@\033[0;0m")
sleep(0.2)
print("- This dragon will randomly teleport around the board.")
sleep(0.2)
print("- If the dragon lands on your position you will die and then the game will end.")
sleep(0.2)
print("-------------------------------------")
sleep(2)
print("4. You can move in 4 directions:")
sleep(0.2)
print("- North, East, South, West.")
sleep(0.2)
print("- You control yourself using W, A, S and D. If you put the same input twice you will sprint and move two spaces instead of one.")
sleep(2)
print("Good luck wanderer....")
sleep(0.2)
print("-------------------------------------")
sleep(0.2)
print("loading....")
sleep(0.2)
print("-------------------------------------")
print("")
sleep(2.5)
sleep(4)
os.system("clear")

#allows the player to set how large the map is
grid = int(input("How large do you want the map to be? Input a number. If you put in 5 the grid will be 5x5, etc."))

moves = 0
x = 0
y = 0

cx = random.randint(0,(grid-1))
cy = random.randint(0,(grid-1))

#explain rules and tells you what icons means what
print("You are \033[1;32mx\033[0;0m, the dragon is \033[1;31m@\033[0;0m, search through the bushes for the treasure and avoid the dragon!")
print("\n")

while(True):

  dx = random.randint(0,(grid-1))
  dy = random.randint(0,(grid-1))

  for i in range(grid):
      if i == dy and i == y:
        for u in range(grid):
          if u == dx:
            print("\033[1;31m@ \033[0;0m", end="")
          elif u ==  x:
            print("\033[1;32mx \033[0;0m", end="")
          else:
            print("# ", end="")
        print()
      elif i == y:
          print("# "* x, end="")
          print("\033[1;32mx \033[0;0m", end="")
          print("# "*((grid- x)-1))
      elif i == dy:
          print("# "*dx, end="")
          print("\033[1;31m@ \033[0;0m", end="")
          print("# "*((grid-dx)-1))
      else:  
        for i in range(grid):
          print("# ", end="")
        print()
        

  if dx == x and dy == y:
    if moves == 1:
      print("You died in", moves,"move!")
    elif moves > 1 or moves == 0:
      print("You died in", moves,"moves!")
    break
  elif cx == x and cy == y:
    if moves == 1:
      print("You won in", moves,"move!")
    elif moves > 1 or moves == 0:
      print("You won in", moves,"moves!")
    break

  (print("\n"))

  m = input("Which way would you like to move?(W,A,S,D or x2 to sprint) ").lower()

  if m == "w" and y > 0:
      y = y-1
  elif m == "d" and  x < (grid-1):
       x = x+1
  elif m == "s" and y < (grid-1):
      y = y+1
  elif m == "a" and  x >0:
       x = x-1
  elif m == "ww" and y > 0:
      y = y-2
  elif m == "dd" and  x < (grid-1):
       x = x+2
  elif m == "ss" and y < (grid-1):
      y = y+2
  elif m == "aa" and  x >0:
       x = x-2
  else:
      print("Invalid move")

  moves = moves + 1
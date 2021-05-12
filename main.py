import random

grid = 5

moves = 0

x = 0
y = 0

cx = random.randint(0,(grid-1))
cy = random.randint(0,(grid-1))

while(True):

  dx = random.randint(0,(grid-1))
  dy = random.randint(0,(grid-1))

  for i in range(grid):
      if i == dy and i == y:
        for u in range(grid):
          if u == dx:
            print('@ ', end='')
          elif u == x:
            print('x ', end='')
          else:
            print('# ', end='')
        print()
      elif i == y:
          print('# '*x, end="")
          print('x ', end="")
          print('# '*((grid-x)-1))
      elif i == dy:
          print('# '*dx, end="")
          print('@ ', end="")
          print('# '*((grid-dx)-1))
      else:  
        for i in range(grid):
          print('# ', end="")
        print()

  if dx == x and dy == y:
    if moves == 1:
      print('You died in', moves,'move!')
    elif moves > 1 or moves == 0:
      print('You died in', moves,'moves!')
    break
  elif cx == x and cy == y:
    if moves == 1:
      print('You won in', moves,'move!')
    elif moves > 1 or moves == 0:
      print('You won in', moves,'moves!')
    break

  m = input('Which way would you like to move?(N,E,S or W)').lower()

  if m == 'n' and y > 0:
      y = y-1
  elif m == 'e' and x < (grid-1):
      x = x+1
  elif m == 's' and y < (grid-1):
      y = y+1
  elif m == 'w' and x >0:
      x = x-1
  else:
      print('Invalid move')

  moves = moves + 1
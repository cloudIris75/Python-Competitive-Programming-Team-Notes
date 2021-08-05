h, w = map(int, input().split())
board = [[0 for j in range(h)] for i in range(w)]

n = int(input())

for i in range(n):
  l, d, x, y = map(int, input().split())
  x = x-1
  y = y-1
  if d==0:
    if (y+l)>h:
      for j in range(l):
        board[x][y] = 1
        y -= 1
    else:
      for j in range(l):
        board[x][y] = 1
        y += 1
  elif d==1:
    if (x+l)>w:
      for j in range(l):
        board[x][y] = 1
        x -= 1
    else:
      for j in range(l):
        board[x][y] = 1
        x += 1

for i in range(w):
  for j in range(h):
    print(board[i][j], end=' ')
  print()

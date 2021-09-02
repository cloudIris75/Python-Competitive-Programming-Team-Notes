# CodeUp No.6097
# Create w*h size grid
h, w = map(int, input().split())
board = [[0 for j in range(w)] for i in range(h)]

n = int(input())

# l:length, d:0(horizontal)/1(vertical), x:y-coordinate, y:x-coordinate
for i in range(n):
  l, d, x, y = map(int, input().split())
  x = x-1
  y = y-1
  if d==0:
    if (y+l)>w:
      for j in range(l):
        board[x][y] = 1
        y -= 1
    else:
      for j in range(l):
        board[x][y] = 1
        y += 1
  elif d==1:
    if (x+l)>h:
      for j in range(l):
        board[x][y] = 1
        x -= 1
    else:
      for j in range(l):
        board[x][y] = 1
        x += 1

for i in range(h):
  for j in range(w):
    print(board[i][j], end=' ')
  print()

# Input 2D list
board = []
for i in range(19):
    board.append(input().split())
    for j in range(19):
        board[i][j] = int(board[i][j])

n = int(input())

# Flipping go stones cross
for i in range(n):
  x, y = map(int, input().split())
  x -= 1
  y -= 1

  for j in range(19):
    if board[j][y] == 0:
      board[j][y] = 1
    else:
      board[j][y] = 0
    
    if board[x][j] == 0:
      board[x][j] = 1
    else:
      board[x][j] = 0

for i in range(19):
  for j in range(19):
    print(board[i][j], end=' ')
  print()

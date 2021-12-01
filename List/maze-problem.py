#CodeUp No.6098 성실한 개미
box = [list(map(int, input().split())) for _ in range(10)]

# x : y-coordinate, y : x-coordinate
x = 1
y = 1

while x<=9 and y<=9:
  if box[x][y] == 0:
    box[x][y] = 9
    y += 1
  elif box[x][y] == 1:
    y -= 1
    x += 1
  elif box[x][y] == 2:
    box[x][y] = 9
    break
  else:
    break

for i in range(10):
  for j in range(10):
    print(box[i][j], end=' ')
  print()

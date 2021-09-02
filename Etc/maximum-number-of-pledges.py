# CodeUp No.4016
a, b, c = map(int, input().split())

a_array = []
for i in range(1, a+1):
  if a%i==0:
    a_array.append(i)

b_array = []
for i in range(1, b+1):
  if b%i==0:
    b_array.append(i)

c_array = []
for i in range(1, c+1):
  if c%i==0:
    c_array.append(i)

max = []
for i in range(a+1):
  if (i in a_array) and (i in b_array) and (i in c_array):
    max.append(i)

print(max[-1])

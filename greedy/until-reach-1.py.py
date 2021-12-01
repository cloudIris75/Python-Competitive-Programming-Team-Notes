# Coding Test No.3-4 1이 될 때까지
n, k = map(int, input().split())
count = 0

while n >= k:
    while n % k != 0:
        n -= 1
        count += 1
    n //= k
    count += 1

while n > 1:
    n -= 1
    count += 1

print(count)

# N이 큰 수인 경우에도 효율적인 방법
while True:
    target = (n // k) * k
    count += (n - target)
    n = target
    if n < k:
        break
    n //= k
    count += 1

count += (n - 1)
print(count)

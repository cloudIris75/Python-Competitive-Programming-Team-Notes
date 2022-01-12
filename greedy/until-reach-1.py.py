# Coding Test No.3-4 1이 될 때까지
# N, K를 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())
count = 0

# N이 K 이상이라면 K로 계속 나누기
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
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    count += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    n //= k
    count += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
count += (n - 1)
print(count)

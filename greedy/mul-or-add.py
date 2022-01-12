# Coding Test No.11-2 곱하기 혹은 더하기
s = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(s[0])

for i in range(1, len(s)):
    # 두 수 중에서 하나라도 '0' 또는 '1'인 경우, 더하기 수행
    num = int(s[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

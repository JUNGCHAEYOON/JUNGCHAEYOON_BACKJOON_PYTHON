# 20220627 정채윤 백준 10430번

A, B, C = map(int,input().split())

print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)


# 20220627 정채윤 백준 10430번

inputstr = input()
arr = []

for i in inputstr:
    if(i != ' '):
        arr.append(int(i))
A = arr[0]
B = arr[1]
C = arr[2]

print((A + B) % C)
print((A % C) + (B % C) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)


# 20220627 정채윤 백준 10998번

total = 0
inputnum = input()
arr = []

for i in inputnum:
    if(i != ' '):
        arr.append(int(i))
        
print(arr[0] * arr[1])
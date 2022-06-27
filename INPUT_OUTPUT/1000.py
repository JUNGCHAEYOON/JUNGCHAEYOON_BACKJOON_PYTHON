# 20220627 정채윤 백준 1000번

total = 0
inputnum = input()

for i in inputnum:
    if(i != ' '):
        total += int(i)
        
print(total)
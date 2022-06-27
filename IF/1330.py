# 20220627 정채윤 백준 1330번

arr = []

A, B = map(int,input().split())

if(A < B):
    print("<")
elif(A > B):
    print(">")
else:
    print("==")
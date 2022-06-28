# 20220628 정채윤 백준 2577번

def check_numbers(_A, _B, _C):
    tmp = str(_A * _B * _C)
    
    arr = [0, 0, 0, 0, 0, 0, 0, 0 ,0, 0]
    for index in tmp:
        arr[int(index)] += 1
    
    for index in arr:
        print(index)

if __name__=="__main__":
    A = int(input())
    B = int(input())
    C = int(input())

    check_numbers(A, B, C)
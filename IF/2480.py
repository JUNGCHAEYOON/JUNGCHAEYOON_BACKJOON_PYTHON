# 20220627 정채윤 백준 2480번

def dice_three(_X, _Y, _Z):
    if(_X == _Y == _Z):
        print(10000 + _X * 1000)
    elif(_X == _Y != _Z):
        print(1000 + _X * 100)
    elif(_X != _Y == _Z):
        print(1000 + _Y * 100) 
    elif(_X == _Z != _Y):
        print(1000 + _X * 100)
    else:
        print(max(_X, _Y, _Z) * 100)
        

if __name__ == "__main__":
    X, Y, Z = map(int,input().split())

    dice_three(X, Y, Z)
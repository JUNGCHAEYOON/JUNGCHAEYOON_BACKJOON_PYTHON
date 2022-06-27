# 20220627 정채윤 백준 14681번

def check_4space(_X, _Y):
    if(_X > 0 and _Y > 0):
        print(1)
    elif(_X < 0 and _Y > 0):
        print(2)
    elif(_X < 0 and _Y < 0):
        print(3)
    elif(_X > 0 and _Y < 0):
        print(4)

if __name__ == "__main__":
    X = int(input())
    Y = int(input())

    check_4space(X, Y)
# 20220627 정채윤 백준 2739번

def call99(_X):
    for i in range(9):
        print(_X, "*", i + 1, "=", _X * (i + 1))

if __name__ == "__main__":
    X = int(input())

    call99(X)
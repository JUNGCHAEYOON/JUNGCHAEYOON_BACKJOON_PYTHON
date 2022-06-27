# 20220627 정채윤 백준 9488번

def checkGrade(_inputNum):
    if(_inputNum <= 100 and _inputNum >= 90):
        print("A")
    elif(_inputNum <= 89 and _inputNum >= 80):
        print("B")
    elif(_inputNum <= 79 and _inputNum >= 70):
        print("C")
    elif(_inputNum <= 69 and _inputNum >= 60):
        print("D")
    else:
        print("F")



if __name__ == "__main__":
    inputNum = int(input())
    checkGrade(inputNum)

# 20220627 정채윤 백준 2753번

def check_leap_year(_year):
    if((_year % 4) == 0 and (_year % 100) != 0):
         print(1)
    elif((_year % 400) == 0):
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    year = int(input())
    check_leap_year(year)
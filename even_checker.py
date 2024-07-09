import sys

def main(arrays):
    flag = True
    for number in arrays:
        if number % 2 == 0:
            continue
        else:
            print("숫자" + f"{number}" + "은 짝수가 아닙니다")
            flag = False
            break

if __name__ == "__main__":
    arrays = list(map(int, sys.argv[1:]))
    main(arrays)


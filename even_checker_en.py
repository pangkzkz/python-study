import sys

#실행할 때 숫자 넣어줘야 결과로 even 뽑아줌


def main(arrays):
    flag = True
    for index, number in enumerate(arrays, start =1): #1부터 카운트 하기 위해
        if number % 2 == 0:
            continue
        else:
            print(f"{index}" + "번째 숫자" + f"{number}" "은 짝수가 아닙니다")
            flag = False
            break

def extract_even_list(arrays):
    even_list = [ ] 
    for index, number in enumerate(arrays):
        if number % 2 == 0:
            even_list.append(number) #짝수면 even_list에 추가
    print(even_list + [16, 18])

def extract_even_set(arrays): #set 자료형: 출력 순서 랜덤
    even_set = set()
    for index, number in enumerate(arrays):
        if number % 2 == 0:
            even_set.add(number)
    print(even_set)


def extract_even_dict(arrays): #key의 값을 넣고 append를 꼭 해줘야 함
    even_dict = {"index": [], "number": []} #index는 자료에 번호 붙인거 
    for index, number in enumerate(arrays):
        if number % 2 == 0:
            even_dict["index"].append(index)
            even_dict["number"].append(number)
    print(even_dict)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python even_checker_en.py <1 2 3 5 6 7 8>") #<>는 parameter 뜻함
        sys.exit(1)
    else:
        arrays = list(map(int, sys.argv[1:])) #python에서는 list 사용; java에서 array 사용; 따라서 array말고 list넣어도 됨
        extract_even_dict(arrays)





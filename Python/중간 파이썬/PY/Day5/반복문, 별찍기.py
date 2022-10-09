# a = int(input())
# i = 0;
# while i < a :
#     print("Hello World")
#     i += 1

# i = 9;
# while i >= 1:
#     print(i*9)
#     i-=1
#
# i = 1;
# while i<10 :
#     print(i*9)
#     i+=1
marks = [90,10,20,30,20]
print(type(marks))
number = 0
cnt = 0
for i in marks:
    number +=1
    if i >= 60:
        print(f'{number}번 학생은 합격입니다.')
        cnt +=1
    else:
        print(f'{number}번 학생은 불합격 입니다.')
print(f'합격:{cnt} 불합격:{5-cnt}')

marks = [90,25,67,45,'겅']
number = 0

for i in marks:
    number +=1
    print(number)
    print(f'{i}님 합격 추카')

    evennumbers = [2, 4, 6, 8, 10]
    oddnumbers = [1, 3, 5, 7, 9]

    numbers = evennumbers + oddnumbers
    print(numbers)
    print(numbers * 4)

    print("============"*30)
    numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

    numbers[4] = 100
    print(numbers)

    numbers[2] = "hello"
    print(numbers)

    numbers[0] = numbers[9]  # 인덱스 9를 인덱스 0에 대입
    print(numbers)

    numbers[8] = ['a', 'b', 'c']  # 리스트 전체를 형태 유지하며 대입
    print(numbers)

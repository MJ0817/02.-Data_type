# 변수
a = b = 'python'
print(a, b)
c, d = 'hello', 'world'
print(c, d)

# 문자열(string): 작은 따옴표와 큰 따옴표로 구분. 문자열로 기재된 데이터가 아니라 빨간 밑줄
a = "Hello World"
print(a)

b = 'Hello World'
print(b)
# 문자열 더하기
name = '김민준'
age = ' 30'
c = name + '님, 반갑습니다.' + ' 나이는' + age + '살 이시군요.'
print(c)


print("father's favorite food is orange")
print('엄마가 말했다. "밥 먹고가"')

head = "python"
tail = " is fun!"
print(head + tail)

# 문자열 반복하기
print("=" * 50)
print("프로그램 소개")
print("=" * 50)


# 문자열 길이구하기.

contents = "자기소개서는 1,000줄 이내로 작성하시오. 지금까지 작성한 문자열의 길이가 몇인지 구하시오."
len(contents)
print(len(c)) #print를 써야 결과값이 출력이 됨.

# 문자열의 인덱싱(문자열마다 번호부여)과 슬라이싱(추출)

a = "Life is too shorts, You need python2"
print(a[0], a[-1])
# 인덱싱된 번호를 사용하여 선택한 문자열을 추출, 첫번쨰 0, 마지막 -1

print(a[0:4])
# a[0:4] 는 a 인덱스 번호 0번부터 4번까지를 출력하되, 4번은 포함하지 않고0번부터 3번까지 출력.

집 = "smart안전학과 강사 7월 강의 현황"
print(집[5:9])

#숫자형(변수에 따옴표 없이 숫자를 입력, type()함수는 변수의 자료형을 확인하기 위하여 사용,

a = 1
print(type(a))
b = 2.5
print(type(b))
print(a + b)

string = "1"
int = 1
print(string)
print(int)
print(type(string))

a = 1
b = 2
print(a + b, a - b, a * b, a / b)

number_1 = 11
number_2 = 5
print(number_1 // number_2)
print(number_1 ** number_2)

#리스트 -여러 값을 저장하는 배열, 리스트에 포함된 값은 요소

fruits = ["사과", "바나나", "딸기"]
print(fruits, type(fruits))

#연습문제
numbers = [1,2,3,4,5]
result = numbers[2] + numbers[-1]
print(result)
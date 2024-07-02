#리스트 -여러 값을 저장하는 배열, 리스트에 포함된 값은 요소

fruits = ["사과", "바나나", "딸기"]
print(fruits, type(fruits))

minjoon = ["김민준", '20', '010-21424-12321']
name = minjoon
age = minjoon[1]
phone = minjoon[2]
phone = minjoon[-1]
print(name, age, phone)

print(type(minjoon))
print(minjoon[-1])
print(minjoon[0])

names = [['강수경', '강혜나', '김민석'], ['20', '21', '22'], ['010', '011', '012']]
print(names[0][1])
print(names[1][0:2])
print(names[3][-1])


#연습문제
numbers = [1,2,3,4,5]
result = numbers[2] + numbers[-1]
print(result)

print(len(names[2]))

#리스트에 요소 추가하기(append)
last = [1,2,3]
last.append(30) #위 리스트에 30이라는 요소 추가
print(last)
#리스트에 요소 삭제하기(remove)

last.remove(3)
print(last)
print(type(last))

#딕셔너리( =key-value data, 딕셔너리 자료형은 키-값 쌍을 저장하는 데이터 타입, 증괄호 {} 로 둘러 쌓여 있으며, 각 키와 값은 : (콜론) 으로 구분
#키를 입력하여 Value 를 확인 ex> 이름(key) -  김민준(Value)
person = {"이름": "김민준", "나이" : 20}
print(person)

dic = {'김민준': 20, '하현수': 30}
print(dic['하현수'])

#딕셔너리 데이터 업데이트
dic['김민준'] = 22
print(doc['김민준'])
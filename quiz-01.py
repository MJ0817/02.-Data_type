# 첫 번째 회원의 정보 입력 받기
name1 = input("이름을 입력하세요.")
age1 = input("나이를 입력하세요.")
email1 = input("이메일 주소를 입력하세요")
phone1 = input("연락처: ")
person1 = {"이름": name1, "나이": age1, "이메일 주소": email1, "연락처": phone1}

# 두 번째 회원의 정보 입력 받기
name2 = input("이름을 입력하세요.")
age2 = input("나이를 입력하세요.")
email2 = input("이메일 주소를 입력하세요")
phone2 = input("연락처: ")
person2 = {"이름": name2, "나이": age2, "이메일 주소": email2, "연락처": phone2}

dic = {name1: {'나이': age, '이메일 주소': email, }}
print(dic1)
dic = {name2: {'나이': age, '이메일 주소': email, }}
print(dic2)

dic = {name: [age, email, ]}
print(dic)
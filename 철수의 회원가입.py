# 첫 번째 회원의 정보
name1 = input("이름: ")
age1 = input("나이: ")
email1 = input("이메일 주소: ")
phone1 = input("연락처: ")
person1 = {"이름": name1, "나이": age1, "이메일 주소": email1, "연락처": phone1}


# 두 번째 회원의 정보
name2 = input("이름: ")
age2 = int(input("나이: "))
email2 = input("이메일 주소: ")
phone2 = input("연락처: ")

data = {
    name1: [age1, email1, phone1],
    name2: [age2, email2, phone2]
}

#불린(Boolean) - 참 또는 거짓값을 나타내는 데이터 타입, 주로 조건문에서 사용(50이상 True, 이하 False 식으로 나타내어 안전율 구분)
is_true = True
is_false = False
print(is_true, is_false, type(is_true), type(is_false))
if is_true:
    print("이것은 참입니다.")
if is_false:
    print("이것은 거짓입니다.")
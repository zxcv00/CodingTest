# 9. enumerate를 사용하는 반복문 예시

num = ["one", "two", "three"]

for i, x in enumerate(num):
    print("{}번 째 값 => {}".format(i, x))
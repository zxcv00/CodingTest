# 7.리스트에서 특정 원소만 추출
# ex)  [1, 2, 2, 2, 3, 1, 1, 3, 2]에서 2만 추출

arr = [1, 2, 2, 2, 3, 1, 1, 3, 2]

result = list()

for x in arr:
    if x != 2:
        # 새로운 공간에 x 넣기
        result.append(x)

print(result)
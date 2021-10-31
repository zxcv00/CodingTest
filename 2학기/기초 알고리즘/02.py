# 2. 원소의 개수를 카운터하기
# ex) [1, 2, 2, 2, 3, 1, 1, 3, 2] 에서 2의 개수를 카운팅

arr = [1, 2, 2, 3, 1, 1, 3, 2]

# count 0으로 초기화
count = 0

# arr의 모든 요소들에 대해서
for x in arr:
    # 각각의 원소가 2이면
    if x == 2:
        # count에 1을 증가
        count += 1

print(count)

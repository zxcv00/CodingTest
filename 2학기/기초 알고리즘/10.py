# 10. 최댓값 혹은 최솟값을 구하는 알고리즘 직접 구현하기(max, min함수 쓰지 않고)
# ex) [3, 6, 2, 7]

num = [3, 6, 2, 7]

# 값의 범위를 0 ~ 100이라 가정할 때 (방법 1)
# => 범위의 최솟값 혹은 이보다 작은 수를 초기화
# max_num = -1

# 방법 2 
# => 배열의 첫 원소값을 초기화
max_num = num[0]

for x in num:
    if max_num < x:
        max_num = x

print("최댓값 =>", max_num)


# def find_max(x):
#     n = len(x)
#     max_num = x[0]
#
#     for i in range(1, n):
#         if x[i] > max_num:
#             max_num = x[i]
#
#     return max_num
#
# print("최댓값 = >", find_max(num))
# 4.Bubble Sort 구현

arr = [8, 5, 6, 3, 4]

for i in range(0, len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)



# 첫 번째
# if arr[0] > arr[1]:
#     arr[0], arr[1] = arr[1], arr[0]
#
# if arr[1] > arr[2]:
#     arr[1], arr[2] = arr[2], arr[1]
#
# if arr[2] > arr[3]:
#     arr[2], arr[3] = arr[3], arr[2]
#
# if arr[3] > arr[4]:
#     arr[3], arr[4] = arr[4], arr[3]
#
# 두 번째
# if arr[0] > arr[1]:
#     arr[0], arr[1] = arr[1], arr[0]
#
# if arr[1] > arr[2]:
#     arr[1], arr[2] = arr[2], arr[1]
#
# if arr[2] > arr[3]:
#     arr[2], arr[3] = arr[3], arr[2]
#
# 세 번째
# if arr[0] > arr[1]:
#     arr[0], arr[1] = arr[1], arr[0]
#
# if arr[1] > arr[2]:
#     arr[1], arr[2] = arr[2], arr[1]
#
# 네 번째
# if arr[0] > arr[1]:
#     arr[0], arr[1] = arr[1], arr[0]

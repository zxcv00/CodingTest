# 11. 숫자의 개수가 몇 개인지 카운팅
# ex) 93728499321에서 9의 개수 구하기 (문자열 사용하지 않고)

num = list(str(93728499321))
cnt = 0

for i in num:
    if i == str(9):
        cnt += 1
print(cnt)

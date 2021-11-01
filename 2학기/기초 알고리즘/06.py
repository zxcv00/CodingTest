# 6.어떤 문자열에 해당 단어가 몇 개 있는지 카운팅
# ex) "ILOVKEFLOVEE"에서 "LOV"가 몇 개 있는지 카운팅

t = "ILOVKEFLOVEE"
find = "LOV"
count = 0

for i in range(len(t)):
    # 첫 글자가 "L"인 경우 and 찾아야 하는 끝 글자의 범위 체크
    if t[i] == find[0] and i + len(find) <= len(t):
        if t[i + 1] == find[1]:
            if t[i + 2] == find[2]:
                count += 1

print(count)


# 6.어떤 문자열에 해당 단어가 몇 개 있는지 카운팅
# ex) "ILOVKEFLOVEE"에서 "LOV"가 몇 개 있는지 카운팅

t = "ILOVKEFLOVEE"
count = 0

for i in range(len(t)):
    if t[i] == "L":
        if t[i + 1] == "O":
            if t[i + 2] == "V":
                count += 1

print(count)


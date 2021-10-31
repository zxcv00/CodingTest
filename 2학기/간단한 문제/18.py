time = input("현재 시간 => ")

if time[-2:] == "00":
    print("정각")
else:
    print("정각 아님")
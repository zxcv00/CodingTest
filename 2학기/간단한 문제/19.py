list_f = ['intra.h', 'intra.c', 'define.h', 'run.py']

for i in list_f:
    split = i.split(".")

    if split[1] == "h":
        print(i)

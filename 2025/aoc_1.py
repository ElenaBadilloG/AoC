import pandas as pd

df = pd.read_csv("1_input.csv")
nlist = list(df["path"])
print(nlist)


def get_pwd(nlist):  # part 1
    cnt = 0
    init_n = 50
    for n in nlist:
        s = n[0]
        k = float(n[1:])
        if s == "L":
            init_n = init_n - k
            if init_n % 100 == 0:
                cnt += 1
        elif s == "R":
            init_n = init_n + k
            if init_n % 100 == 0:
                cnt += 1
    print("A: " + str(cnt))
    return cnt


def get_pwd_2(nlist):  # part 2
    cnt = 0
    init_n = 50
    for n in nlist:
        s = n[0]
        k = float(n[1:])

        if s == "L":
            for i in range(int(init_n) - 1, int(init_n - k) - 1, -1):
                if i % 100 == 0:
                    cnt += 1

            init_n -= k
        elif s == "R":
            for i in range(int(init_n) + 1, int(init_n + k) + 1):
                if i % 100 == 0:
                    cnt += 1
            init_n += k

    print("B: " + str(cnt))
    return cnt


get_pwd(nlist)
get_pwd_2(nlist)

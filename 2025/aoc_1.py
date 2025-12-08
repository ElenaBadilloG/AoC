import pandas as pd

df = pd.read_csv("input.csv")
nlist = list(df["path"])

def get_pwd(nlist):
    cnt = 0
    init_n = 50
    for n in nlist:
        s = n[0]
        k = float(n[1:])
        if s == "L":
            init_n = init_n - k
            if (init_n % 100 == 0):
                cnt += 1
        elif s == "R":
            init_n = init_n + k
            if (init_n % 100 == 0):
                cnt += 1
    print("A: " + str(cnt))
    return cnt

if 
%timeit get_pwd(nlist)

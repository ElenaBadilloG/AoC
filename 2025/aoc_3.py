import pandas as pd

df = pd.read_csv("3_input.csv", header=0)
d = df.to_dict()
d = d["bank"]


def fst_lgst_dg(strg):
    lstrg = list(strg)
    mx = 0
    ix = 0
    mx2 = 0
    ix2 = 0
    si_lst = [(i, int(s)) for i, s in enumerate(lstrg)]

    for i, s in si_lst:
        if s > mx and i < int(len(si_lst) - 1):
            mx = s
            ix = i

    si2_lst = [p for i, p in enumerate(si_lst) if i > ix]
    for s2 in si2_lst:
        if s2[1] > mx2:
            mx2 = s2[1]
    r = int(str(mx) + str(mx2))

    return r


ds = {}
for b, l in d.items():
    ds[b] = fst_lgst_dg(str(l))
print("A: " + str(sum([s for s in ds.values()])))

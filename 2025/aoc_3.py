import pandas as pd

df = pd.read_csv("3_input.csv", header=0)
d = df.to_dict()
d = d["bank"]


def get_maxsuf_dig(nstr, subseqN):
    mxsuf = -1
    wini = 0
    for i, s in enumerate(list(nstr)):
        if float(s) > mxsuf and len(nstr[i + 1 :]) >= subseqN:
            mxsuf = float(s)
            wini = i

    if mxsuf == -1:  # No valid digit found
        return None, nstr, -1

    fs = [s for j, s in enumerate(list(nstr)) if j > wini]
    ns = "".join(fs)

    return int(mxsuf), ns, wini


def fst_lgst_dg(lstrg, K):
    # Goal: find the max K-len LS not-necessarily-contiguous substring, respecting LS index order
    # 1 get the max digit such that there are enough (K-1)subsequent elements (helper func)
    # 2 keep that max, remove from seq every before it and it, add it to string result
    # repeat until string results is size K.
    # 3 however...
    # check if any of the digits in the discarded element list (final wrt original)
    # is larger than the minimum of final string in their relative position: that should not happen
    # if so, substitute at corresponding *relative* position

    lstrg_or = lstrg
    rn = ""
    selected_indices = []
    offset = 0

    for i, s in enumerate(lstrg):
        if len(rn) < K:
            r, lstrg, wini = get_maxsuf_dig(lstrg, K - len(rn) - 1)
            if r is None:  # No more valid digits
                break
            rn += str(r)
            selected_indices.append(offset + wini)
            offset += wini + 1
        else:
            break

    rds = [
        (j, s) for j, s in enumerate(list(lstrg_or)) if j not in selected_indices
    ]  # residual elements

    rn = list(rn)  # preliminary final string
    for result_pos in range(len(rn)):
        current_selected_idx = selected_indices[result_pos]
        current_digit = int(rn[result_pos])

        for orig_idx, digit in rds:
            if orig_idx > current_selected_idx and int(digit) > current_digit:
                if len(lstrg_or) - orig_idx - 1 >= K - result_pos - 1:
                    rn[result_pos] = digit  # swap
                    selected_indices[result_pos] = orig_idx
                    break

    rn = "".join(rn)  # definitive final string
    return int(rn)


ds = {}
for b, l in d.items():
    ds[b] = fst_lgst_dg(str(l), 2)
print("A1: " + str(sum([s for s in ds.values()])))


ds2 = {}
for b, l in d.items():
    ds2[b] = fst_lgst_dg(str(l), 12)
print("A2: " + str(sum([s for s in ds2.values()])))

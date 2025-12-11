input = "9100-11052,895949-1034027,4408053-4520964,530773-628469,4677-6133,2204535-2244247,55-75,77-96,6855-8537,55102372-55256189,282-399,228723-269241,5874512-6044824,288158-371813,719-924,1-13,496-645,8989806846-8989985017,39376-48796,1581-1964,699387-735189,85832568-85919290,6758902779-6759025318,198-254,1357490-1400527,93895907-94024162,21-34,81399-109054,110780-153182,1452135-1601808,422024-470134,374195-402045,58702-79922,1002-1437,742477-817193,879818128-879948512,407-480,168586-222531,116-152,35-54"
input = input.split(",")


def is_doub(n):  # for part 1
    n = str(n)
    if len(n) % 2 == 0:
        if n[0 : int((len(n) / 2))] == n[int((len(n) / 2)) : int(len(n))]:
            return True
        else:
            return False
    else:
        return False


def is_fus(fs):  # for part 2
    fs = str(fs)
    for i in range(1, int(len(fs))):
        f = fs[0:i]
        fn = f * int(len(fs) / len(f))
        if fn == fs:
            return True
    return False


def get_invalids(i, part=1):
    ends = i.split("-")
    sumn = 0
    for n in range(int(ends[0]), int(ends[1]) + 1):
        if part == 1:
            a = is_doub(n)
        if part == 2:
            a = is_fus(n)
        if a:
            sumn += n
    return sumn


tot = 0
for i in input:
    tot += get_invalids(i)
print("A1: " + str(tot))

tot = 0
for i in input:
    tot += get_invalids(i, part=2)
print("A2: " + str(tot))

def check_all_negative(arr):
    for i in arr:
        if (i > 0):
            return 0
    print(max(arr))
    return 1


def remove_negatives(arr):
    for i in range(0,arr.__len__()):
        if (arr[i] < 0):
            arr[i]=0

    return arr


def find_max_sum(arr):
    incl = []
    excl = []

    for i in arr:
        new_excl = excl[:] if sum(excl) > sum(incl) else incl[:]

        incl = excl[:]
        incl.append(i)
        excl = new_excl[:]


    if(sum(excl)==sum(incl)):
        if(min(excl)>min(incl)):
            return excl
        else:
            return incl

    return (excl if sum(excl) > sum(incl) else incl)


for i in range(int(input())):
    testcase = int(input())
    houseticket = list(map(int, input().split()))
    if (check_all_negative(houseticket)==0):
        res = remove_negatives(find_max_sum(houseticket))
        res.reverse()
        print(int("".join(map(str, res))))
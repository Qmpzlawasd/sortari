import random,time


def InsertionSort(l):
    if len(l) > 10**6:  # aiae
        return
    for i in range(1, len(l)):
        j = i-1
        c = l[i]
        while j >= 0 and c < l[j]:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = c


def CountingSort(l):
    frecventa = [0 for _ in range(max(l)+1)]
    for i in l:
        frecventa[i] += 1
    indx = 0
    for i in range(len(frecventa)):
        for j in range(frecventa[i]):
            l[indx] = i
            indx += 1


def MergeSort(l):
    if len(l) != 1:
        mijloc = len(l)//2
        left = l[:mijloc]
        right = l[mijloc:]
        MergeSort(left)
        MergeSort(right)
        i = 0
        j = 0
        indx = 0
        while j < len(right) and i < len(left):
            if left[i] > right[j]:
                l[indx] = right[j]
                j += 1
                indx += 1
            if j < len(right) and left[i] <= right[j]:
                l[indx] = left[i]
                indx += 1
                i += 1

        while i < len(left):
            l[indx] = left[i]
            indx += 1
            i += 1
        while j < len(right):
            l[indx] = right[j]
            j += 1
            indx += 1


def check(l):
    for i in range(1, len(l)):
        if l[i-1] > l[i]:
            return 0
    return 1


def RadixSort(l, baza=10):
    # 65536
    maxx = max(l)
    exp = 1
    n = len(l)
    while maxx // exp != 0:
        frecv = [0] * baza
        out = [0] * n

        for i in range(n):
            frecv[l[i] // exp % baza] += 1

        for i in range(1, baza):
            frecv[i] += frecv[i - 1]

        for i in range(len(l)-1, -1, -1):
            aux = l[i] // exp % baza
            out[frecv[aux] - 1] = l[i]
            frecv[aux] -= 1

        for i in range(len(l)):
            l[i] = out[i]

        exp *= baza


def RadixSortdivide(l, baza=65536):
    maxx = max(l)
    exp = 1
    n = len(l)
    while maxx // exp != 0:
        frecv = [0] * baza
        out = [0] * n

        for i in range(n):
            frecv[l[i] // exp % baza] += 1

        for i in range(1, baza):
            frecv[i] += frecv[i - 1]

        for i in range(len(l)-1, -1, -1):
            aux = l[i] // exp % baza
            out[frecv[aux] - 1] = l[i]
            frecv[aux] -= 1

        for i in range(len(l)):
            l[i] = out[i]

        exp *= baza


def RadixSortShift(l, baza=65536):
    # 65536
    maxx = max(l)
    exp = 0
    n = len(l)
    while (maxx >> exp) != 0:
        frecv = [0] * (baza)
        out = [0] * n

        for i in range(n):
            frecv[(l[i] >> exp) & (baza-1)] += 1

        for i in range(1, baza):
            frecv[i] += frecv[i - 1]

        for i in range(len(l)-1, -1, -1):
            aux = (l[i] >> exp) & (baza-1)
            out[frecv[aux] - 1] = l[i]
            frecv[aux] -= 1

        for i in range(len(l)):
            l[i] = out[i]
        if exp == 0:
            exp = 1
        exp += 10


def ShellSort(l, gaps):
    n = len(l)
    for gap in gaps:
        for i in range(gap, n):
            aux = l[i]
            j = i
            while j - gap >= 0 and l[j - gap] > aux:
                l[j] = l[j - gap]
                j -= gap

            l[j] = aux


shellarray = []
shellarray.append([44782196, 19903198, 8845866, 3931496, 1747331, 776591, 345152, 153401,
                  68178, 30301, 13467, 5985, 2660, 1182, 525, 233, 103, 46, 20, 9, 4, 1])  # tokuda

shellarray.append([149109795, 66271020, 29453787, 13090572, 5818032, 2585792, 1149241, 510774, 227011,
                  100894, 44842, 19930, 8858, 3937, 1750, 701, 301, 132, 57, 23, 10, 4, 1])  # ciura extinssa

f = open('teste.in')
for i in range(int(f.readline().split()[2])):
    c = f.readline().split()
    maxim = int(c[5])
    l = [maxim]
    for _ in range(int(c[2])-1):
        l.append(random.randrange(maxim))
    k = 0
    for gg in [RadixSort, RadixSortShift,RadixSortdivide, MergeSort, ShellSort, InsertionSort, CountingSort, -1]:
        hh = l[:]
        if gg == -1:

            print('tim ---->>>test:', i, end='-->')
            start = time.time()
            hh.sort()
            end = time.time()
            print(end - start if check(hh) else 'nu am putut sorta (v-v)')
        elif gg == ShellSort:
            for inx, j in enumerate(shellarray):
                print(f'{gg} gap {inx}  ---->>>test:', i, end='-->')
                start = time.time()
                ShellSort(hh, j)
                end = time.time()
                print(end - start if check(hh) else 'nu am putut sorta (v-v)')
                hh = l[:]
        else:
            print(f'{gg}  ---->>>test:', i, end='-->')
            start = time.time()
            gg(hh)
            end = time.time()
            print(end - start if check(hh) else 'nu am putut sorta (v-v)')
        k += 1

import random
import time


def InsertionSort(l):
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


def RadixSort2(l, baza=65536):
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
        exp += (10)


def ShellSort(l):

    gaps = [1750,701, 301, 132, 57, 23, 10, 4, 1]  # ciura

    n = len(l)
    for gap in gaps:
        for i in range(gap, n):
            aux = l[i]
            j = i
            while j - gap >= 0 and l[j - gap] > aux:
                l[j] = l[j - gap]
                j -= gap

            l[j] = aux


def ShellSort2(l):


    gaps = [44782196, 19903198, 8845866, 3931496, 1747331, 776591, 345152, 153401,
            68178, 30301, 13467, 5985, 2660, 1182, 525, 233, 103, 46, 20, 9, 4, 1]#tokuda

    n = len(l)
    for gap in gaps:
        for i in range(gap, n):
            aux = l[i]
            j = i
            while j - gap >= 0 and l[j - gap] > aux:
                l[j] = l[j - gap]
                j -= gap

            l[j] = aux


f = open('sortari/teste.in')
# dd = open('struc/sortari/asd.in','w')
for i in range(int(f.readline().split()[2])):
    c = f.readline().split()
    maxim = int(c[5])
    l = [[maxim]for _ in range(6)]
    for _ in range(int(c[2])-1):
        l[0].append(random.randrange(maxim))
        l[1].append(random.randrange(maxim))
        l[2].append(random.randrange(maxim))
        # l[3].append(random.randrange(maxim))
        # l[4].append(random.randrange(maxim))
        # l[5].append(random.randrange(maxim))
        k = 0
    for gg in [ShellSort,ShellSort2]:
        if gg == -1:
            print('tim ---->>>test:', i, end='-->')
            # dd.write('itmsort--->>test '+str(i)+'-->>')
            start = time.time()
            l[k].sort()
            end = time.time()
            # if check(l[k]):
            #     dd.write(str(end - start )+'\n')
            # else:

            #     dd.write('eroare'+'\n')
            print(end - start if check(l[k]) else 'eroare')
        else:
            print(f'{gg}  ---->>>test:', i, end='-->')
            # dd.write(str(gg)+'--->>test '+str(i)+'-->>')
            start = time.time()
            gg(l[k])
            end = time.time()
            print(end - start if check(l[k]) else 'eroare')
            # if check(l[k]):
            #     dd.write(str(end - start )+'\n')
            # else:

            #     dd.write('eroare'+'\n')

        k += 1

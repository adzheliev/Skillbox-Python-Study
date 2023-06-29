from collections.abc import Iterable

def QHofstadter(s: list, N: int) -> Iterable[int]:
        a = s[:]
        for _ in range(N):
            if a[0] == 1 and a[1] == 1:
                q = a[-a[-1]] + a[-a[-2]]
                a.append(q)
                yield q

N = int(input('Сколько чисел последовательности считать? '))

for i in QHofstadter(s=[1, 1], N=N):
    print(i)

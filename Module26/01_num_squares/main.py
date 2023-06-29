from collections.abc import Iterable

class Test:
    def __init__(self, N:int) -> None:
        self.num = N
        self.counter = 1

    def __iter__(self) -> Iterable[int]:
        return self

    def __next__(self) -> Iterable[int]:
        while self.num >= self.counter:
            squares = self.counter ** 2
            self.counter += 1
            return squares
        raise StopIteration


N = int(input('Введите число N: '))
test = Test(N)
for i in test:
    print(i)


N = int(input('Введите число N: '))
squares = (num ** 2 for num in range(1, N+1))
for i in squares:
    print(i)

def squares(N:int) -> Iterable[int]:
    start = 1
    while start <= N:
        yield start ** 2
        start += 1

N = int(input('Введите число N: '))
for i in squares(N=N):
    print(i)


import math
from typing import Union

class MyMath:

    @staticmethod
    def circle_len(radius: Union[int, float]) -> float:
        return math.pi * (radius * 2)

    @staticmethod
    def circle_sq(radius: Union[int, float]) -> float:
        return math.pi * (radius ** 2)

    @staticmethod
    def cubevolume(side: Union[int, float]) -> float:
        return side ** 3

    @staticmethod
    def sfere_sq(radius: Union[int, float]) -> float:
        return 4 * math.pi * (radius ** 2)


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)
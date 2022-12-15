### Giả lập input của bài này :D
from random import randint
_count = 0
_value = 0
def input(txt: str):
    global _count
    global _value
    match _count:
        case 0:
            value = randint(3, 8)
        case 1:
            x = _value // 2
            value = randint(_value - x, _value + x)
        case 2:
            x = _value // 2 - 1
            value = randint(_value - x, _value + x)
        case _:
            return
    _count += 1
    _value = value
    print(txt + str(value))
    return value

### Bài bắt đầu từ đây
from math import sqrt
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Không thỏa mãn bất đẳng thức tam giác.")
else:
    P = a + b + c
    p = P / 2
    S = sqrt(p * (p - a) * (p - b) * (p - c))
    print("Chu vi:", p)
    print("Diện tích:", S)

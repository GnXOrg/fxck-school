### Giả lập input của bài này :D
from random import randint
_count = 0
def input(txt: str):
    global _count
    match _count:
        case 0:
            value = randint(4, 20)
        case 1:
            value = randint(4, 20)
        case 2:
            value = randint(4, 12)
        case _:
            return
    _count += 1
    print(txt + str(value))
    return value

### Bài bắt đầu từ đây
a = int(input("Đáy trên: "))
b = int(input("Đáy dưới: "))
h = int(input("Chiều cao: "))
print("Diện tích hình thang là:", h * (a + b) / 2)

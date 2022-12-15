### Giả lập input của bài này :D
from random import randint
_count = 0
def input(txt: str):
    global _count
    match _count:
        case 0:
            value = randint(0, 31)
        case 1: 
            value = randint(0, 24)
        case 2:
            value = randint(0, 60)
        case 3:
            value = randint(0, 60)
        case _:
            return
    _count += 1
    print(txt + str(value))
    return value

### Bài bắt đầu từ đây
ngay = int(input("Ngày: "))
gio = int(input("Giờ: "))
phut = int(input("Phút: "))
giay = int(input("Giây: "))
print("Thời gian được tính bằng giây là:", ((ngay * 24 + gio)*60 + phut)*60 + giay)
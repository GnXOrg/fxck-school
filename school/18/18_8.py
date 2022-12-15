### Giả lập input của bài này :D
from random import randint
_count = 0
def input(txt: str):
    global _count
    match _count:
        case 0:
            value = randint(0, 3000000)
        case _:
            return
    _count += 1
    print(txt + str(value))
    return value

### Bài bắt đầu từ đây
giay = int(input("Giây: "))
ngay = giay // (60 * 60 * 24)
giay -= ngay * (60 * 60 * 24)
gio = giay // (60 * 60)
giay -= gio * (60 * 60)
phut = giay // 60
giay -= phut * 60
print("Thời gian được tính bằng ngày, giờ, phút, giây là:", str(ngay) + "d", str(gio) + "h", str(phut) + "m", str(giay) + "s")
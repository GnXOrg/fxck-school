### Giả lập input của bài này :D
from random import randint
_count = 0
def input(txt: str):
    global _count
    match _count:
        case 0:
            value = randint(2, 5) * 1000
        case 1: 
            value = randint(3, 10)
        case _:
            return
    _count += 1
    print(txt + str(value))
    return value

### Bài bắt đầu từ đây
gia_tien = int(input("Giá tiền của 1 thiệp: "))
so_thiep = int(input("Số thiệp bạn Lan mua: "))
print("Số tiền bạn Lan phải trả là:", gia_tien * so_thiep)
### Giả lập input của bài này :D
from random import randint
_count = 0
def input(txt: str):
    global _count
    match _count:
        case 0:
            value = randint(7, 15) * 100
        case 1:
            value = randint(100, 200)
        case _:
            return
    _count += 1
    print(txt + str(value))
    return value

### Bài bắt đầu từ đây
don_gia = int(input("Đơn giá: "))
kwh = int(input("Lượng điện tiêu thụ (> 100kW): "))
kwh -= 100
print("Tiền điện:", don_gia * 100 + (don_gia + don_gia * 0.1) * kwh)
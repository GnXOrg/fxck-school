commands = [
    ("a", 'int("5*2")'), 
    ("b", 'float(123)'), 
    ("c", 'str(5)'), 
    ("d", 'float("123 + 5.5")')
]

for i in commands:
    try:
        eval(i[1])
    except:
        print(i[0] + ")", "lỗi")
commands = [
    ("a", int(5 + 3)), 
    ("b", str(5 + 3)), 
    ("c", float(4 + 5)), 
    ("d", int(4.3 + 2))
]

for i in commands:
    print(i[0] + ")", i[1])
    
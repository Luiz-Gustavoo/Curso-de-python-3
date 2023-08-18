x = 1 # está no escopo global

def escopo():
    global x
    x = 10 # 1a mudança de x
    y = 4
    print(x)
    def sub_escopo():
        global z
        z = 2 # está no escopo local de sub_escopo
        global x
        x = 12 # 2a mudança de x
        print(x, y, z)
    sub_escopo()
    x = 6 # 3a mudança de x
    print(z)
    print(x)

print(x)
escopo()
print(x)

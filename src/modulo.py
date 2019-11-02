def func(pedras, joia):
    qt = 0
    for j in joia:
        for p in pedras:
            if p == j:
                qt+=1

    return qt

# Testes
print(func(pedras = "aA", joia = "aAAbbbb"))
print(func(pedras = "z", joia = "ZZ"))

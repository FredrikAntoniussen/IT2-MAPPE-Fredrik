liste = ["Norge","Norge","Sverige","Danmark","Danmark"]

høyeste = ""
høyeste_antall = -1
for land in liste:
    antall = liste.count(land)
    if antall > høyeste_antall:
        høyeste = land
        høyeste_antall = antall
print(høyeste)
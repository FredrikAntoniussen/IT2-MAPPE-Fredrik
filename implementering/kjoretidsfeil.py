while True: 
    try:
        alder = int(input("Alder: "))
        break
    except: print("Alder må være et heltall, prøv igjen")
fodselsaar = 2022 - alder
print(f'fødselsår: {fodselsaar}')
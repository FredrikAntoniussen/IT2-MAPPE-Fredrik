assert 10 > 5 # 10 er større enn 5 , derfor gjør den ingenting 
try:
    assert 10 > 20 # 10 er ikke større en 20, derfor gir denne en feilmelding
except:
    print("Hei på deg")
print("koden er ferdig")

def areal(høyde, bredde):
    return høyde*bredde
def omkrets(høyde, bredde):
    return høyde*2 + bredde*2




try:
    assert areal(5,3) == 15
    assert omkrets(5,5) ==20
except:
    print("koden er feil")
    print("koden er feil")


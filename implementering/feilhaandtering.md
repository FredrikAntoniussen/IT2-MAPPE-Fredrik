# Vern mot kjøretidsfeil og logiske feil i programmer

## Kjøretidsfeil 

Håndtering av kjøretidsfeil i Python gjøres med nøkkelordene try og except.

```python
while True: 
    try:
        alder = int(input("Alder: "))
        break
    except: print("Alder må være et heltall, prøv igjen")
fodselsaar = 2022 - alder
print(f'fødselsår: {fodselsaar}')

```

## Logiske feil i programmer 

For å oppdage logiske feil i python-programmer kan vi bruke nøkkelordet 'assert' for å forsikre oss om at koden gir korrekte resultat.

Eksempel:

```python 

assert 10 > 5 # 10 er større enn 5 , derfor gjør den ingenting 
assert 10 > 20 # 10 er ikke større en 20, derfor gir denne en feilmelding

```

Eksempel test av funksjoner med assert 

```python

def areal(høyde, bredde):
    return høyde * bredde

def omkrets(høyde, bredde):
    return høyde + høyde + bredde + bredde

assert areal(3,2) == 6
assert areal(3,3) == 9
assert areal(3,4) == 12
assert omkrets(3,2) == 10
assert omkrets(3,3) == 12
assert omkrets(3,4) == 14

```

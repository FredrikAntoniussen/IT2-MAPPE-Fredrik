# 3. Bruk filen `List of world cities by population density.csv` og finn ut hvilket land som har flest byer på topp-50 listen av byer med høyest befolkningstetthet.

fil = open("./List of world cities by population density.csv")
data = fil.read()
linjer = data.split("\n")

land = []


for linje in linjer[:-1]:
    splittet_linje = linje.split(",")
    
    land.append(splittet_linje[-1])
    
print(land)

country_counts = {}

# Loop gjennom listen og legg til land og tellere i en dictionary
for country in land:
    if country == 'Country':
        continue
    if country not in country_counts:
        country_counts[country] = 1
    else:
        country_counts[country] += 1

# Finn landet med flest forekomster
most_common_country = max(country_counts, key=country_counts.get)

print("Landet som står mest i listen er", most_common_country, "med", country_counts[most_common_country], "forekomster.")

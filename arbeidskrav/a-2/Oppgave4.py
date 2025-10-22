# Oppgave 4 - A
# Land, og deres hovedsteder og dens befolkning i millioner
data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873],
}

# Oppgave 4 - B

land = input(
    """Velkommen til den store (lille) verden!
Her kan du finne ut hva du enn måtte ønske om et land (ihvertfall så lenge det du ønsker er hovedstad og befolkningstall). \n
Skriv inn navnet på et land som du ønsker å få vite mer om: """)
if land in data.keys():
    hovedstad, befolkning = data[land]
    print(f"Hovedstaden i {land} er {hovedstad} med en befolkning på {befolkning} millioner.")

# Oppgave 4 - C : Løser oppgave 4c ved at brukeren får beskjed hvis landet ikke finnes i databasen og kan legge det til.
else:
    print("Landet finnes ikke i databasen.")
    nytt_land = input("Vil du legge det til? (Ja/Nei) ")
    if nytt_land.lower() == "ja":
        hovedstad = input("Skriv inn hovedstaden: ")
        befolkning = float(input("Skriv inn befolkningen i millioner: "))
        data[land] = [hovedstad, befolkning]
        print(f"{land} er lagt til i databasen.")
        print(f"Oppdatert database: {data}")
    else:
        print("Ok, ha en fin dag!")
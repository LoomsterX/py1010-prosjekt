import numpy as np

# lager en funksjon som beregner arealet og omkretsen av en figur som består av en halvsirkel og en rettvinklet trekant. Denne skal ikke ta noen input eller printe not til konsollen, det gjøres utenfor funksjonen.
def areal_figur(diameter, katet) -> float:
    """Beregn arealet av en rektangel eller sirkel basert på input.

    Args:
        diameter (float): Lengde av sirkelens diameter
        katet (float): Kateten in trekanten som ikke sammenfaller med sirkelens diameter.

    Returns:
        None. Programmet printer bare resultatet til konsollen.
    """
    # Beregne arealene til figurene uavhengig av hverandre
    areal_halvsirkel = 0.5 * np.pi * (diameter/2)**2
    areal_trekant = 0.5 * diameter * katet
    # Sette sammen arealene til figurene
    areal_figur = areal_halvsirkel + areal_trekant

    # Beregne omkretsene på figurene uavhengig av hverandre 
    omkrets_halvsirkel = 0.5 * np.pi * diameter/2 + diameter
    omkrets_trekant = diameter + katet + np.sqrt(diameter**2 + katet**2)
    # Slå sammen figurene og fjerne sidene som er inne i figuren
    omkrets_figur = omkrets_halvsirkel + omkrets_trekant - 2*diameter 
    
    return areal_figur, omkrets_figur



# Kjør funksjonen med eksempelverdier
if __name__ == "__main__":
    diameter = float(input("Skriv inn diameter: "))
    katet = float(input("Skriv inn lengde på katet: "))
    areal_figur, omkrets_figur = areal_figur(diameter, katet)

    # Print resultatet og formatere beregningene til to desimaler
    print(f"Arealet av figuren er: {areal_figur:.2f} og omkretsen er: {omkrets_figur:.2f}")
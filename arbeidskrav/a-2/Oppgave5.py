import numpy as np

def areal_figur(a, b) -> None:
    """Beregn arealet av en rektangel eller sirkel basert på input.

    Args:
        a (float): Lengde av sirkelens diameter
        b (float): Kateten in trekanten som ikke sammenfaller med sirkelens diameter.

    Returns:
        float: Arealet av figuren.
    """

    areal_halvsirkel = 0.5 * np.pi * (a/2)**2
    areal_trekant = 0.5 * a * b
    areal_figur = areal_halvsirkel + areal_trekant

    omkrets_halvsirkel = 0.5 * np.pi * a/2 + a
    omkrets_trekant = a + b + np.sqrt(a**2 + b**2)
    omkrets_figur = omkrets_halvsirkel + omkrets_trekant - 2*a

    print(
        f"Arealet av figuren er: {areal_figur:.2f} og omkretsen er: {omkrets_figur:.2f}")

if __name__ == "__main__":
    areal_figur(2, 1)
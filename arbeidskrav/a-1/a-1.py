### Definerer variabler

forsikring_el:int = 5000                # kr/år
forsikring_bensin: int = 7500           # kr/år
trafikkforsikringsavgift:float = 8.38   # kr/dag
forbruk_el: float = 0.2                 # kWh/km
strompris: float  = 2.00                # kr/kWh
forbruk_bensin: float = 1.0             # kr/km
bomavgift_el: float = 0.1               # kr/km
bomavgift_bensin: float = 0.3           # kr/km
std_kjorelengde: int = 10000            # km

def vurdering(kjorelengde: int):
    # Beregner kostnad for elbil
    kostnad_el_fast = forsikring_el + trafikkforsikringsavgift*365
    kostnad_el_variabel = forbruk_el * strompris * kjorelengde
    kostnad_el_total = kostnad_el_fast + kostnad_el_variabel

    # Beregner kostand for bensinbil
    kostnad_bensin_fast = forsikring_bensin + trafikkforsikringsavgift*365
    kostnad_bensin_variabel = forbruk_bensin * strompris * kjorelengde
    kostnad_bensin_total = kostnad_bensin_fast + kostnad_bensin_variabel

    # Vurdering
    differanse = kostnad_bensin_total - kostnad_el_total
    
    print(
        f"De årlige kostnadene basert på kjørelengde: {kjorelengde:,}km er: \
        \n \U0001F50B Elbil: {kostnad_el_total:,} kr \
        \n \U0001F6E2 Bensinbil: {kostnad_bensin_total:,} kr"
        )

    if kostnad_el_total > kostnad_bensin_total:
        print(f"Du bør kjøpe bensinbil \U0001F6E2 Den er {abs(differanse):,} kr billigere i drift per år \U0001F4B0")
    else:
        print(f"Du bør kjøpe elbil \U0001F50B Den er {abs(differanse):,} kr billigere i drift per år \U0001F4B0")

# Run if directly run
if __name__ == "__main__":
    vurdering(std_kjorelengde)


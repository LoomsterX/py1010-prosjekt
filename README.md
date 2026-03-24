# Til studieveilederene

OBS: Kjøring av kode krever at man enten har installert UV og kjører koden via "uv run main_prosjektoppgave.py" eller at man aktiverer .venv (".\.venv\Scripts\Activate.ps1") og så kjører "pyhton main_prosjektoppgave.py".

### Arbeidskrav

Arbeidskrav finnes i mappen arbeidskrav i tilhorende undermappe (Arbeidskrav 1 = a-1).

Selve **besvarelsen** finnes i .py filen i denne mappen. (Arbeidskrav 1 --> "a-1.py")

### Prosjekt

Prosjekter legges ogsa i egne folders. Struktur TBD.

Prosjektoppgaven kan kjorres fra `main_prosjektoppgave.py` i rot ved å kjøre "uv run main_prosjektoppgave.py".
Den henter egendefinerte funksjoner og klasser fra `Prosjektoppgave/utils`.
En alternativ inngang er `energi_analyse_mal.py`, som bare kaller samme pipeline.

### Tester

Tester for prosjektoppgaven ligger i `Prosjektoppgave/tests`.
Kjor testene med:

- `pytest`
- `python -m Prosjektoppgave.tests`

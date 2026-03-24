# Prosjektoppgave - Energi- og forbruksanalyse

## Problemformulering
Et kontorbygg samler inn energiforbruk hver 15. minutt. Målet med prosjektet er å bygge en enkel datapipeline som leser rå måledata fra fil, renser og beriker dataene, beregner nøkkelindikatorer, og visualiserer forbruksmønstre. Prosjektet skal gi innsikt i når og hvor forbruket er høyest, hvordan temperatur påvirker forbruket, og hvordan forbruk varierer mellom avdelinger og tidsperioder.

## Datasett
Du har fått en rå loggfil `energi_logg.csv` med følgende kolonner:
- `timestamp` (YYYY-MM-DD HH:MM)
- `kwh` (energiforbruk)
- `temp_c` (utetemperatur i grader celsius)
- `avdeling` (f.eks. A, B, C)

## Delmål
1. Les inn `energi_logg.csv` og lag arrays for `timestamp`, `kwh`, `temp_c`, `avdeling`.
2. Data engineering:
- Rens bort rader med manglende eller ugyldige verdier.
- Konverter `timestamp` til dato og ukedag.
- Lag ny kolonne `periode` (08-12, 12-16, 16-20) basert på klokkeslett.
- Skriv et renset og beriket datasett til `energi_logg_clean.csv`.
3. Data analytics:
- Finn topp 5 tidsstempler med høyest forbruk.
- Beregn gjennomsnitt og median forbruk per ukedag.
- Finn sammenheng mellom temperatur og forbruk (korrelasjon).
- Klassifiser hver maaling som `lav`, `normal` eller `hoy` basert paa terskler.
4. Datavisualisering:
- Linjeplot av forbruk over tid for en valgt avdeling.
- Stolpediagram av gjennomsnittlig forbruk per ukedag.
- Scatterplot av temperatur vs forbruk, fargekodet etter `periode`.

## Krav som maa oppfylles
Oppgaven skal inneholde:
- arrays
- vektoriserte beregninger
- if/else-tester
- for- eller while-lokke
- lese data fra fil
- skrive data til fil
- plotting
- egendefinerte funksjoner

## Leveranse
- En kort beskrivelse av problemet du oensker aa loese
- Kjorbar kode (py-fil eller JNB) med korte, informative kommentarer
- Tilleggsfiler (datasettet)
- Koden skal vaere grundig testet og kjoerbar for mottaker

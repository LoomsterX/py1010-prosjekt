import csv
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "energi_logg.csv"
CLEAN_FILE = BASE_DIR / "energi_logg_clean.csv"


def load_data(path: Path):
    """Les data fra CSV til lister og numpy-arrays."""
    timestamps = []
    kwh = []
    temp_c = []
    avdeling = []

    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            timestamps.append(row["timestamp"].strip())
            kwh.append(row["kwh"].strip())
            temp_c.append(row["temp_c"].strip())
            avdeling.append(row["avdeling"].strip())

    # arrays (forelopig som object, renses senere)
    return (
        np.array(timestamps),
        np.array(kwh, dtype=object),
        np.array(temp_c, dtype=object),
        np.array(avdeling),
    )


def clean_data(ts, kwh_raw, temp_raw, dept):
    """Rens bort rader med manglende/ugyldige verdier."""
    good_idx = []
    for i in range(len(ts)):
        if ts[i] == "" or dept[i] == "":
            continue
        # if/else-test for gyldige tall
        try:
            k = float(kwh_raw[i])
            t = float(temp_raw[i])
            if np.isnan(k) or np.isnan(t):
                continue
        except ValueError:
            continue
        good_idx.append(i)

    # vektoriserte uttrekk
    ts = ts[good_idx]
    kwh = kwh_raw[good_idx].astype(float)
    temp = temp_raw[good_idx].astype(float)
    dept = dept[good_idx]
    return ts, kwh, temp, dept


def to_weekday_and_period(ts_arr):
    """Lag ukedag og periode (08-12, 12-16, 16-20)."""
    weekdays = []
    periods = []
    for ts in ts_arr:  # for-lokke
        dt = datetime.strptime(ts, "%Y-%m-%d %H:%M")
        weekdays.append(dt.strftime("%A"))

        h = dt.hour + dt.minute / 60.0
        if 8 <= h < 12:
            periods.append("08-12")
        elif 12 <= h < 16:
            periods.append("12-16")
        else:
            periods.append("16-20")

    return np.array(weekdays), np.array(periods)


def classify_usage(kwh):
    """Klassifiser forbruk etter terskler (vektorisert)."""
    # terskler kan justeres
    low = 14
    high = 20
    labels = np.where(kwh < low, "lav", np.where(kwh > high, "hoy", "normal"))
    return labels


def save_clean(path, ts, kwh, temp, dept, weekday, period, label):
    """Skriv renset og beriket datasett til fil."""
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(
            ["timestamp", "kwh", "temp_c", "avdeling", "ukedag", "periode", "klasse"]
        )
        for i in range(len(ts)):
            w.writerow(
                [ts[i], kwh[i], temp[i], dept[i], weekday[i], period[i], label[i]]
            )


def analyze(ts, kwh, temp, weekday):
    """Enkle analyser og utskrift."""
    # topp 5
    top_idx = np.argsort(kwh)[-5:][::-1]
    print("Topp 5 forbruk:")
    for i in top_idx:
        print(f"{ts[i]} -> {kwh[i]:.2f} kWh")

    # gjennomsnitt og median per ukedag
    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print("\nGjennomsnitt og median per ukedag:")
    for day in sorted(np.unique(weekday), key=lambda d: day_order.index(d) if d in day_order else 99):
        mask = weekday == day
        print(f"{day}: snitt={kwh[mask].mean():.2f}, median={np.median(kwh[mask]):.2f}")

    # korrelasjon temperatur vs forbruk
    corr = np.corrcoef(temp, kwh)[0, 1]
    print(f"\nKorrelasjon temp vs forbruk: {corr:.3f}")


def plot_all(ts, kwh, temp, weekday, period, dept):
    """Lag plottene."""
    # linjeplot for valgt avdeling
    chosen = "A"
    mask = dept == chosen
    plt.figure(f"Forbruk over tid (avdeling {chosen})")
    plt.plot(ts[mask], kwh[mask])
    plt.title(f"Forbruk over tid (avdeling {chosen})")
    plt.xlabel("Tid")
    plt.ylabel("kWh")
    tick_indices = range(0, mask.sum(), 5)
    plt.xticks(ticks=list(tick_indices), labels=ts[mask][list(tick_indices)], rotation=45, ha="right")
    plt.tight_layout()

    # stolpediagram snitt per ukedag
    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    days = sorted(np.unique(weekday), key=lambda d: day_order.index(d) if d in day_order else 99)
    means = [kwh[weekday == d].mean() for d in days]
    plt.figure("Gjennomsnittlig forbruk per ukedag")
    plt.bar(days, means)
    plt.title("Gjennomsnittlig forbruk per ukedag")
    plt.ylabel("kWh")
    plt.tight_layout()

    # scatter temperatur vs forbruk, farge etter periode
    plt.figure("Temperatur vs forbruk")
    colors = {"08-12": "tab:blue", "12-16": "tab:orange", "16-20": "tab:green"}
    for p in np.unique(period):
        m = period == p
        plt.scatter(temp[m], kwh[m], label=p, alpha=0.7, c=colors.get(p, "gray"))
    plt.title("Temperatur vs forbruk")
    plt.xlabel("Temp (C)")
    plt.ylabel("kWh")
    plt.legend()
    plt.tight_layout()

    plt.show()


def run_pipeline(data_file: Path = DATA_FILE, clean_file: Path = CLEAN_FILE):
    ts, kwh_raw, temp_raw, dept = load_data(data_file)
    ts, kwh, temp, dept = clean_data(ts, kwh_raw, temp_raw, dept)
    weekday, period = to_weekday_and_period(ts)
    label = classify_usage(kwh)
    save_clean(clean_file, ts, kwh, temp, dept, weekday, period, label)
    analyze(ts, kwh, temp, weekday)
    plot_all(ts, kwh, temp, weekday, period, dept)

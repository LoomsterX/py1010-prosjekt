from pathlib import Path

from utils.energi_analyse import run_pipeline
from utils.functions import log_decorator

DATA_FILE = Path(__file__).parent / "energi_logg.csv"
CLEAN_FILE = Path(__file__).parent / "energi_logg_clean.csv"


@log_decorator
def main():
    run_pipeline(DATA_FILE, CLEAN_FILE)


if __name__ == "__main__":
    main()

from Oppgave5 import areal_figur

# Test
def test_areal_figur():
    areal, omkrets = areal_figur(2, 1)
    errors = []
    try:
        assert round(areal, 2) == 2.57, "Test feilet, Arealet er beregnet feil"
    except AssertionError as e:
        errors.append(e)
    try:    
        assert round(omkrets, 2) == 4.81, "Test feilet, Omkretsen er beregnet feil"
    except AssertionError as e:
        errors.append(e)
    if errors:
        [print(error) for error in errors]
    else:
        print("Alle tester bestått!")

if __name__ == "__main__":
    test_areal_figur()
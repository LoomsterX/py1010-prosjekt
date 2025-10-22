import datetime

Fødselsår: int = int(input('Hvilket år er du født? ') )
nåværende_år: int = datetime.datetime.now().year

alder = nåværende_år - Fødselsår

print(f'Du blir {alder} år gammel i løpet av {nåværende_år}.')

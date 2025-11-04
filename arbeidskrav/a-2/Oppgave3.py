### Imports ###
import numpy as np  

### Input fra bruker ###
v_grad = float(input('Skriv inn gradtallet:' ))

### Regner om fra grader til radianer ###
grad_til_rad = v_grad*np.pi/180

### Alternativ måte for å regne om fra grader til radianer ved bruk av numpy ###
# grad_til_rad = np.radians(v_grad)

### Printer ut resultatet og presenterer det med to desimaler ###
print(f'Gradtallet {v_grad} i radianer er {grad_til_rad:.2f}')
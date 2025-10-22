import matplotlib.pyplot as plt
import numpy as np

def funksjon(x):
    return -x**2 - 5

intervall = np.linspace(-10, 10, 200)
y = funksjon(intervall)
plt.plot(intervall, y)

if __name__ == "__main__":
    plt.title("Plot av funksjonen f(x) = -x^2 - 5")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.show()

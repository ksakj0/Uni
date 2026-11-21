import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 3, figsize=(12, 4))

# Gráfica 1
x1 = np.linspace(0, 10, 400)
ax[0].plot(x1, np.sqrt(x1), label=r'$f(x) = \sqrt{x}$', color='blue')
ax[0].set_title("1. $f(x) = \sqrt{x}$")
ax[0].grid(True)
ax[0].axhline(0, color='black', linewidth=0.5)
ax[0].axvline(0, color='black', linewidth=0.5)

# Gráfica 2
x2 = np.linspace(2, 10, 400)
ax[1].plot(x2, np.sqrt(x2 - 2), label=r'$f(x) = \sqrt{x - 2}$', color='green')
ax[1].set_title("2. $f(x) = \sqrt{x - 2}$")
ax[1].grid(True)
ax[1].axhline(0, color='black', linewidth=0.5)
ax[1].axvline(0, color='black', linewidth=0.5)

# Gráfica 3
x3 = np.linspace(0, 10, 400)
ax[2].plot(x3, np.sqrt(x3) + 3, label=r'$f(x) = \sqrt{x} + 3$', color='red')
ax[2].set_title("3. $f(x) = \sqrt{x} + 3$")
ax[2].grid(True)
ax[2].axhline(0, color='black', linewidth=0.5)
ax[2].axvline(0, color='black', linewidth=0.5)

plt.tight_layout()
plt.savefig("funciones_radicales_combinadas.png", dpi=300)
plt.show()
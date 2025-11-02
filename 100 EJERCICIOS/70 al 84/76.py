
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 2, 8, 7]

plt.plot(x, y, 'o-', color='b') 
plt.title("Gráfica de ejemplo")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.savefig("grafica.png")
plt.show()

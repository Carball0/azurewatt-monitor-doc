import matplotlib.pyplot as plt
import numpy as np

# Datos
pruebas = ['Prueba 1', 'Prueba 2', 'Prueba 3', 'Prueba 4', 'Prueba 5', 'Prueba 6']
grupos = ['Grupo 1', 'Grupo 2', 'Grupo 3']
n_pruebas = len(pruebas)
n_grupos = len(grupos)

# Tasa de superación (Grupo 1 falló en Prueba 2)
# Todos 100% excepto el grupo 1, que falla una persona en la prueba 2
data = np.full((n_grupos, n_pruebas), 100)
data[0, 1] = 66.7

colors = ['#a6bddb', '#d0d1e6', '#bcbddc']
bar_width = 0.25
x = np.arange(n_pruebas)

plt.figure(figsize=(12, 6))
for i in range(n_grupos):
    plt.bar(x + i * bar_width, data[i], width=bar_width, label=grupos[i], edgecolor='black', color=colors[i])

plt.xticks(x + bar_width, pruebas)
plt.ylim(0, 110)
plt.title('Tasa de Superación de Pruebas Cognitivas por Grupo', fontsize=14)
plt.xlabel('Pruebas')
plt.ylabel('Porcentaje de Superación')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i in range(n_grupos):
    for j in range(n_pruebas):
        valor = data[i, j]
        plt.text(x[j] + i * bar_width, valor - 5 if valor > 10 else valor + 2,
                 f'{valor:.1f}%', ha='center', va='bottom', fontsize=10, color='black')

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Pruebas y grupos
pruebas = ['Prueba 1', 'Prueba 2', 'Prueba 3', 'Prueba 4', 'Prueba 5', 'Prueba 6']
grupos = ['Grupo 1', 'Grupo 2', 'Grupo 3']
n_pruebas = len(pruebas)
n_grupos = len(grupos)

grupo3 = [
    [1, 4, 3, 2, 2, 3],     # Persona 1 - R.B.
    [1, 4, 1, 1, 3, 2],     # Persona 2 - D.C.
    [2, 5, 1, 2, 1, 2]      # Persona 3 - A.C.
]

grupo2 = [
    [5, 7, 4, 5, 4, 5],     # Persona 1 - D.C.
    [3, 7, 3, 4, 2, 3],     # Persona 2 - J.M.
    [4, 9, 5, 4, 5, 3]      # Persona 3 - D.M
]

grupo1 = [
    [5, 9, 5, 7, 6, 5],     # Persona 1 - C.C.
    [4, 10, 5, 4, 4, 4],    # Persona 2 - J.C
    [5, 10, 6, 4, 4, 4]     # Persona 1 - A.C.
]

data = np.array([   # Medias
    np.mean(grupo1, axis=0),
    np.mean(grupo2, axis=0),
    np.mean(grupo3, axis=0)
])

colors = ['#a6bddb', '#d0d1e6', '#bcbddc']
bar_width = 0.25
x = np.arange(n_pruebas)

plt.figure(figsize=(12, 6))

for i in range(n_grupos):
    plt.bar(x + i * bar_width, data[i], width=bar_width, label=grupos[i], edgecolor='black', color=colors[i])

plt.xticks(x + bar_width, pruebas)
plt.ylim(0, 11)
plt.title('Media de Dificultad Percibida por Prueba', fontsize=14)
plt.xlabel('Pruebas Cognitivas')
plt.ylabel('Dificultad Media')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)

for i in range(n_grupos):
    for j in range(n_pruebas):
        valor = data[i, j]
        plt.text(x[j] + i * bar_width, valor + 0.2, f'{valor:.1f}', ha='center', fontsize=9)

plt.tight_layout()
plt.show()

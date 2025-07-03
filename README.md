# azurewatt-monitor-doc

# Visualización de Evaluación de Pruebas Cognitivas

Este repositorio contiene dos gráficos representados en scripts Python que representan la evaluación de una serie de pruebas de recorrido cognitivo aplicadas a tres grupos de usuarios. 

Esto se realiza en el contexto del desarrollo de Trabajo de Fin de Grado, que corresponde al desarrollo del sistema "AzureWatt Smart Monitor".

## Gráfico 1 (1.py): Tasa de Superación por Prueba

Muestra el porcentaje de personas que lograron completar con éxito seis pruebas distintas. Los resultados están divididos por grupo:

- **Grupo 1**: 3 personas con ciertos fallos (una de ellas no superó la prueba 2, lo que da un 66% de éxito en esa prueba).
- **Grupo 2** y **Grupo 3**: Completaron todas las pruebas con un 100% de éxito en cada una.

Este gráfico permite visualizar el desempeño global de cada grupo por prueba.

## Gráfico 2 (2.py): Dificultad Percibida (Escala 0–10)

Representa la media de dificultad percibida (de 0 a 10, de menor a mayor dificultad) en cada una de las seis pruebas, según la opinión de los participantes:

- **Grupo 1**: Grupo con menor conocimiento técnico, encuentras las pruebas algo más difíciles aunque no les presenta mayor problema .
- **Grupo 2**: Evaluó las pruebas con una dificultad media (entre 5 y 7).
- **Grupo 3**: Grupo con mayor conocimiento técnico, las pruebas resultan sencillas.

Ambos gráficos se han generado usando Python y Matplotlib, y están pensados para apoyar un análisis de usabilidad mediante pruebas de recorrido cognitivo.


## Requisitos de ejecución

Para ejecutar los gráficos necesitas tener Python y pip instalados, y a mayores las siguientes librerías:

```bash
pip install matplotlib numpy

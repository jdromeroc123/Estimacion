# Estimación de parámetros de una distribución normal a partir de datos muestrales

Este proyecto tiene como objetivo estimar los parámetros de una distribución normal —la **media** y la **varianza**— a partir de un conjunto de 28 datos muestrales.  
Se presentan además intervalos de confianza, análisis de convergencia de los estimadores y representaciones gráficas comparando los datos con la distribución normal ajustada.

---

## Contenido del proyecto

- Cálculo de estimaciones puntuales de:
  - Media muestral
  - Varianza muestral (corregida)
- Construcción de intervalos de confianza para:
  - Media poblacional (usando distribución *t*)
  - Varianza poblacional (usando distribución *χ²*)
- Visualizaciones:
  - Evolución de las estimaciones a medida que aumenta el número de datos
  - Histograma de los datos vs. densidad de la normal estimada
  - Gráfica de la densidad teórica comparada con los puntos muestrales
- Código Python totalmente reproducible

---

# Estimación puntual

- Media estimada: promedio de los datos.
- Varianza estimada (corregida): varianza muestral con divisor n−1.

---

## Intervalos de confianza

### Media
Basado en la distribución t de Student.

### Varianza
Basado en la distribución chi-cuadrado.

---
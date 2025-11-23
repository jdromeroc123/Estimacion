# Estimación de parámetros de una distribución normal a partir de datos muestrales

Este proyecto tiene como objetivo estimar los parámetros de una distribución normal —la **media** y la **varianza**— a partir de un conjunto de 28 datos muestrales.  
Se presentan además intervalos de confianza, análisis de convergencia de los estimadores y representaciones gráficas comparando los datos con la distribución normal ajustada.

---

## 📌 Contenido del proyecto

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

## 📊 Metodología estadística

### Estimación de parámetros

Para una muestra \( X_1, X_2, \dots, X_n \):

- **Media estimada:**

\[
\hat{\mu} = \frac{1}{n}\sum_{i=1}^{n} X_i
\]

- **Varianza estimada (corregida):**

\[
\hat{\sigma}^2 = \frac{1}{n-1}\sum_{i=1}^{n} (X_i - \hat{\mu})^2
\]

***

### Intervalo de confianza para la media

\[
IC_\mu = \hat{\mu} \pm t_{1-\alpha/2,\; n-1}\;\frac{\hat{\sigma}}{\sqrt{n}}
\]

### Intervalo de confianza para la varianza

\[
IC_{\sigma^2} = 
\left(
\frac{(n-1)\hat{\sigma}^2}{\chi^2_{1-\alpha/2,n-1}},
\;
\frac{(n-1)\hat{\sigma}^2}{\chi^2_{\alpha/2,n-1}}
\right)
\]

---

## Ejecución del código

### 1. Clonar o descargar este repositorio

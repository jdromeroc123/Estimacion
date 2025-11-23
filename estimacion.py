"""
Estimación de parámetros y construcción de intervalos de confianza para la media y varianza de los datos proporcionados.
Este script utiliza las librerías NumPy, Matplotlib y SciPy para realizar cálculos estadísticos.
Los datos son una muestra de 28 observaciones y se asume que siguen una distribución normal 
Para instalar las librerías necesarias, se puede usar el siguiente comando:
pip install -r rquirements.txt

Estudiante: José David Romero Caicedo
Código: 202222606

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t, chi2, norm
import os

def guardar_figura(nombre):
    ruta = os.path.join("imagenes", nombre)
    plt.savefig(ruta, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Figura guardada: {ruta}")

#Datos proporcionados
datos = [16.6114, 11.1941, 12.7406, 16.5992, 11.5618, 15.9377, 20.5315, 8.9843, 18.6348, 11.7442, 16.4094, 15.4836, 18.7936, 9.4448, 10.3349, 10.4214, 13.5888, 15.6584, 13.7008, 12.2002, 18.2335, 12.9852, 10.7033, 10.5753, 15.253, 12.1691, 12.6478, 18.1081]

# Convertir los datos a un array de NumPy para facilitar cálculos con las librerías
datos = np.array(datos)
n = len(datos)
alpha = 0.05

# Estimaciones
mu_hat = np.mean(datos)
sigma2_hat = np.var(datos, ddof=1)
sigma_hat = np.sqrt(sigma2_hat)

print("Media estimada:", mu_hat)
print("Varianza estimada:", sigma2_hat)

# --- Intervalo para la media ---
t_crit = t.ppf(1 - alpha/2, n - 1)
print(t_crit)
IC_mu = (
    mu_hat - t_crit * sigma_hat / np.sqrt(n),
    mu_hat + t_crit * sigma_hat / np.sqrt(n)
)

print("IC para la media:", IC_mu)

# --- Intervalo para la varianza ---
chi2_low = chi2.ppf(alpha/2, n-1)
chi2_high = chi2.ppf(1 - alpha/2, n-1)

IC_sigma2 = (
    (n-1)*sigma2_hat / chi2_high,
    (n-1)*sigma2_hat / chi2_low
)

print("IC para la varianza:", IC_sigma2)


"""
La siguiente sección del código es para graficar la manera cómo varían las estimaciones a medida que aumenta el tamñaño de la muestra.
También se comparan los datos proporcionados con una distribución normal teórica basada en la media y varianza estimadas.    
"""

#Variación de los estimadores con el tamaño de la muestra
mus = [np.mean(datos[:k]) for k in range(2, n+1)]
sigmas = [np.var(datos[:k], ddof=1) for k in range(2, n+1)]

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(range(2,n+1), mus, marker='o')
plt.title("Evolución de la media estimada")
plt.xlabel("Número de datos")
plt.ylabel("Media")
guardar_figura("evolucion_media.png")

plt.subplot(1,2,2)
plt.plot(range(2,n+1), sigmas, marker='o', color='orange')
plt.title("Evolución de la varianza estimada")
plt.xlabel("Número de datos")
plt.ylabel("Varianza")
guardar_figura("evolucion_varianza.png")

# Histograma de los datos y la normal estimada
x = np.linspace(min(datos), max(datos), 200)
pdf = norm.pdf(x, mu_hat, sigma_hat)

plt.figure(figsize=(10,5))
plt.hist(datos, bins=10, density=True, alpha=0.6, label='Datos')
plt.plot(x, pdf, 'r-', label='Normal estimada')
plt.title("Histograma vs Normal estimada")
plt.legend()
guardar_figura("histograma_vs_distribucion.png")

#Puntos en el eje x contra la normal estimada
plt.figure(figsize=(10,5))
plt.plot(x, pdf, 'r-', label='Normal estimada')
plt.scatter(datos, np.zeros_like(datos), marker='x', color='black', label='Datos')
plt.title("Datos en el eje x vs densidad")
plt.legend()
guardar_figura("datos_vs_distribucion.png")



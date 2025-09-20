# Simulación de Concurrencia en el SIGET 🚦

Este proyecto implementa una **simulación del problema Productor–Consumidor** adaptado al contexto de un sistema de gestión de tráfico (SIGET).  

- **Productores** → representan **sensores de tráfico** que generan datos (número de vehículos, detecciones, etc.).
- **Consumidores** → representan **módulos de análisis** que procesan esos datos.
- **Buffer compartido** → funciona como la memoria intermedia donde los productores depositan datos y los consumidores los extraen.

---

##  Objetivo
Demostrar cómo los mecanismos de concurrencia (hilos y exclusión mutua con `Lock`) permiten que varios procesos trabajen **al mismo tiempo** sin que haya pérdida o corrupción de información.  

Esto refleja la importancia de la concurrencia en un sistema de tráfico urbano, donde distintos sensores y módulos deben cooperar de manera sincronizada.

---

##  Tecnologías usadas
- Lenguaje: **Python 3.13.7**
- Librerías estándar: `threading`, `time`, `random`

---

## Ejecución
1. Clona el repositorio:
   ```bash
   git clone https://github.com/TU-USUARIO/siget-concurrencia.git
   cd siget-concurrencia

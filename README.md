# Sistema de Control y Análisis de Producción (Nutrición Animal)

**Integrantes:** Angello Aquino
**Fecha:** Junio 2026

## 🎯 Objetivo del Sistema
Automatizar el registro y análisis de datos en las líneas de producción de nutrición animal. El software elimina el uso de registros manuales en papel, permitiendo a los analistas evaluar en tiempo real si los lotes cumplen con los estándares de calidad establecidos para peso y temperatura de peletizado, reduciendo el margen de error humano.

## ⚙️ Descripción de Funcionalidades
El sistema está estructurado mediante un menú interactivo y cuenta con las siguientes características:
1. **Inicio y Cierre de Turnos:** Bucle principal que permite mantener el sistema en espera o apagarlo de forma segura guardando el estado.
2. **Registro de Lotes:** Permite ingresar el código del lote, seleccionar la línea (Aves o Cerdos), e ingresar datos numéricos de peso (kg) y temperatura (°C).
3. **Validación Automática de Calidad:** Evalúa lógicamente los datos de entrada contra los parámetros de la planta (Batch >= 1000 kg y Temperatura <= 35°C), devolviendo un veredicto inmediato de **Aprobado** o **Rechazado**.
4. **Análisis de Métricas:** Itera sobre la base de datos de la sesión actual para generar estadísticas clave: total de lotes, peso acumulado procesado y porcentaje de efectividad (aprobación) del turno.

## 🛠️ Tecnologías Aplicadas (Unidades 1 a 4)
* **Lenguaje:** Python 3
* **Estructuras de Datos:** Uso de Tuplas para datos inmutables (Líneas de producción), Listas dinámicas para la base de datos principal, y Diccionarios para jerarquizar la información de cada lote.
* **Lógica Computacional:** Implementación de estructuras repetitivas anidadas (`while`, `for`) y sentencias condicionales (`if/elif/else`) apoyadas en operadores lógicos y relacionales.

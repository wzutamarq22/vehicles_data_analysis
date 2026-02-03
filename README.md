# 🚗 Vehicle Data Analysis
Aplicacion web para ver estadisticas de ventas un dataset de vehículos usados y nuevos.
https://vehicles-data-analysis-b8g9.onrender.com
https://github.com/wzutamarq22/vehicles_data_analysis

## 📋 Contenido

- `app.py` - Script principal con todas las funciones
- `EDA.ipynb` - Notebook con el analisis EDA previo
- `requirements.txt` - Dependencias del proyecto
- `vehicles_us.csv` - Dataset original

## 📊 Transformaciones Aplicadas

### 1. Extracción de Marca y Modelo
- Separa la columna `model` en `brand` y `model`
- Ejemplo: "ford f-150" → brand: "ford", model: "f-150"

### 2. Eliminación de Valores Atípicos
- ❌ No se realizo para no sesgar la muestra

### 3. Manejo de Valores Faltantes
- `is_4wd`: 0 para valores faltantes
- `paint_color`: Categoría 'unknown'

### 4. Nuevas Features Creadas (14 total)

#### Métricas de Valor
- `vehicle_age` - Edad del vehículo en años
- `price_per_year` - Precio / edad (retención de valor)
- `price_per_mile` - Precio / odómetro
- `miles_per_year` - Millas promedio por año
- `value_score` - Relación condición/precio

#### Categorías
- `age_category` - new, recent, used, old
- `mileage_category` - low, medium, high, very_high
- `price_category` - budget, affordable, mid_range, premium
- `selling_speed` - fast, normal, slow, very_slow

#### Popularidad
- `is_popular_model` - 1 si está en top 15 modelos

#### Temporales
- `posting_month` - Mes de publicación (1-12)
- `posting_month_name` - Nombre del mes
- `posting_day_of_week` - Día de la semana

#### Scores
- `condition_score` - Score numérico de condición (1-6)

## 📧 Contacto

Para preguntas o sugerencias, contacta al autor del proyecto.

---

**Última actualización**: Enero 2026
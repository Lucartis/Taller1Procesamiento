import pandas as pd

# Cargar el archivo CSV
file_path = r'C:\Users\lucas\Downloads\II trimestre 2024 (1)\DATO_ANONIM_111_IITRIM2024.csv'  # Cambiar ruta
data = pd.read_csv(file_path)

# Verificar la estructura inicial de los datos
print(data.head())

# Filtrar columnas relevantes
columnas_interes = ['DPTO_MPIO', 'PRECIOUNIG', 'PRECIOVTAX']
data_filtrada = data[columnas_interes].dropna()

# Calcular promedios por ciudad
resultados = data_filtrada.groupby('DPTO_MPIO').agg(
    precio_unitario_promedio=('PRECIOUNIG', 'mean'),
    ingresos_estimados_promedio=('PRECIOVTAX', 'mean')
).reset_index()

# Calcular el Score (relación costo-ingreso)
resultados['score'] = resultados['ingresos_estimados_promedio'] / resultados['precio_unitario_promedio']

# Ordenar por los diferentes criterios
ciudades_por_costo = resultados.sort_values(by='precio_unitario_promedio', ascending=True)
ciudades_por_ingresos = resultados.sort_values(by='ingresos_estimados_promedio', ascending=False)
ciudades_por_score = resultados.sort_values(by='score', ascending=False)

# Mostrar las tablas más relevantes
print("Ciudades con menor precio unitario por metro cuadrado:")
print(ciudades_por_costo.head())

print("\nCiudades con mayores ingresos estimados:")
print(ciudades_por_ingresos.head())

print("\nCiudades con mejor relación costo-ingreso (Score):")
print(ciudades_por_score.head())

# Exportar los resultados
ciudades_por_score.to_csv('reporte_ciudades_score.csv', index=False)
ciudades_por_costo.to_csv('reporte_ciudades_costo.csv', index=False)
ciudades_por_ingresos.to_csv('reporte_ciudades_ingresos.csv', index=False)

print("\nReporte generado y datos guardados.")

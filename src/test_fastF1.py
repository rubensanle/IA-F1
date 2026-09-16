import fastf1

# Cargar la carrera del GP de España 2024
session = fastf1.get_session(2024, "Spanish", "R")
session.load()

# Datos de todas las vueltas
laps = session.laps

print("Número de vueltas registradas:", len(laps))
print()
print("Columnas disponibles:")
print(laps.columns.tolist())
print()
print("Primeras 5 vueltas:")
print(laps.head())
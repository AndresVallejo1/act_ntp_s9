import pandas as pd

# Crear DataFrame simple de empleados
data = {
    'nombre': ['Ana', 'Luis', 'Carmen', 'José', 'María', 'Pedro', 'Laura', 'Miguel'],
    'departamento': ['Ventas', 'IT', 'RRHH', 'Ventas', 'IT', 'Marketing', 'RRHH', 'IT'],
    'salario': [45000, 65000, 50000, 48000, 70000, 55000, 52000, 68000],
    'edad': [28, 35, 42, 31, 29, 38, 45, 33]
}

df = pd.DataFrame(data)

print("DataFrame original:")
print(df)
print("\n" + "="*50 + "\n")

# 1. Empleados cuyos nombres empiezan con 'M'
print("1. Empleados cuyos nombres empiezan con 'M':")
nombres_con_m = df[df['nombre'].str.startswith('M')]
print(nombres_con_m)
print("\n" + "-"*30 + "\n")

# 2. Departamentos que contienen 'R'
print("2. Departamentos que contienen 'R':")
departamentos_con_r = df[df['departamento'].str.contains('R')]
print(departamentos_con_r)
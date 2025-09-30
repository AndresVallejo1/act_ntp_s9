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

# 1. Empleados de IT o Ventas
print("1. Empleados de IT o Ventas:")
it_o_ventas = df[df['departamento'].isin(['IT', 'Ventas'])]
print(it_o_ventas)
print("\n" + "-"*30 + "\n")

# 2. Empleados con edad de 28, 35 o 42 años
print("2. Empleados con edad de 28, 35 o 42 años:")
edades_especificas = df[df['edad'].isin([28, 35, 42])]
print(edades_especificas)
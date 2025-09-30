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

# 1. Empleados de IT con más de 30 años Y salario mayor a 60,000
print("1. Empleados de IT con más de 30 años Y salario mayor a 60,000:")
it_mayor_30_salario_alto = df[
    (df['departamento'] == 'IT') & 
    (df['edad'] > 30) & 
    (df['salario'] > 60000)
]
print(it_mayor_30_salario_alto)
print("\n" + "-"*30 + "\n")

# 2. Empleados cuyo nombre empieza con 'L' O son de RRHH
print("2. Empleados cuyo nombre empieza con 'L' O son de RRHH:")
nombre_l_o_rrhh = df[
    (df['nombre'].str.startswith('L')) | 
    (df['departamento'] == 'RRHH')
]
print(nombre_l_o_rrhh)
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

# 1. Empleados con salario mayor a 50,000
print("1. Empleados con salario mayor a 50,000:")
salario_mayor_50k = df[df['salario'] > 50000]
print(salario_mayor_50k)
print("\n" + "-"*30 + "\n")

# 2. Empleados menores de 35 años
print("2. Empleados menores de 35 años:")
menores_35 = df[df['edad'] < 35]
print(menores_35)
print("\n" + "-"*30 + "\n")

# 3. Empleados del departamento 'IT'
print("3. Empleados del departamento 'IT':")
empleados_it = df[df['departamento'] == 'IT']
print(empleados_it)
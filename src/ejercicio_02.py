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

# 1. Empleados de IT Y salario mayor a 60,000
print("1. Empleados de IT Y salario mayor a 60,000:")
it_salario_alto = df[(df['departamento'] == 'IT') & (df['salario'] > 60000)]
print(it_salario_alto)
print("\n" + "-"*30 + "\n")

# 2. Empleados de Ventas O mayores de 40 años
print("2. Empleados de Ventas O mayores de 40 años:")
ventas_o_mayores_40 = df[(df['departamento'] == 'Ventas') | (df['edad'] > 40)]
print(ventas_o_mayores_40)
print("\n" + "-"*30 + "\n")

# 3. Empleados que NO son de Marketing
print("3. Empleados que NO son de Marketing:")
no_marketing = df[~(df['departamento'] == 'Marketing')]
print(no_marketing)
import pandas as pd

df = pd.read_csv('datos.csv')

print("=== 1. INFORMACIÓN GENERAL Y TIPOS DE DATOS ===")
print(df.info())

print("\n=== 2. PRIMERAS FILAS DEL INVENTARIO ===")
print(df.head())

print("\n=== 3. ESTADÍSTICAS BÁSICAS ===")
print(df.describe())

print("\n=== 4. STOCK TOTAL POR SUCURSAL ===")
stock_sucursal = df.groupby('sucursal')['stock'].sum()
print(stock_sucursal)

print("\n=== 5. VALOR TOTAL DEL INVENTARIO POR SUCURSAL ===")
valor_sucursal = df.groupby('sucursal')['valor_total'].sum()
print(valor_sucursal)
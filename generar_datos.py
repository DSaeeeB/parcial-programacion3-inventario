import pandas as pd
import numpy as np

np.random.seed(42)

sucursales = ['San Salvador', 'Santa Ana', 'San Miguel', 'La Libertad', 'Sonsonate']
productos = ['Laptop HP', 'Mouse Inalámbrico', 'Teclado Mecánico', 'Monitor 24"', 'Impresora L3210', 'Silla Ergonómica', 'Audífonos Gamer', 'Disco SSD 1TB']

data = []
for i in range(1, 101):
    producto = np.random.choice(productos)
    sucursal = np.random.choice(sucursales)
    stock = np.random.randint(10, 150)
    precio_unitario = round(np.random.uniform(15.0, 750.0), 2)
    valor_total = round(stock * precio_unitario, 2)
    
    data.append({
        'id_producto': f'PROD-{i:03d}',
        'nombre_producto': producto,
        'sucursal': sucursal,
        'stock': stock,
        'precio_unitario': precio_unitario,
        'valor_total': valor_total
    })

df = pd.DataFrame(data)
df.to_csv('datos.csv', index=False)
print("¡Archivo datos.csv generado con éxito!")
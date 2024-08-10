# PRECIO NETO
# Es el precio sin iva, es quien refleja los impuestos

# Mi función
def precioNeto(iva, precio_bruto):
    resultado = precio_bruto / iva
    return resultado

def calcular_iva(precio_neto, tasa_iva):
    iva = precio_neto * tasa_iva
    return iva

# EJEMPLO
# Datos del producto botella de agua 600ml
producto = "botella de agua 600ml"
precio_bruto = 5 
precio_neto = 1.12
IVA = 0.12

precio_neto = precioNeto(precio_neto, precio_bruto)
iva = calcular_iva(precio_neto, IVA)
print(f"Producto: {producto}\nProducto bruto: Q{precio_bruto} Precio neto: Q{precio_neto} IVA: Q{iva}\n")


# EJEMPLO 2
#Datos del producto jugo de la granja
producto = "jugo de la granja"
precio_bruto = 16
precio_neto = 1.12
IVA = 0.12

precio_neto = precioNeto(precio_neto,precio_bruto)
iva = calcular_iva(precio_neto, IVA)
print(f"Producto: {producto}\nProducto bruto: Q{precio_bruto} Precio neto: Q{precio_neto} IVA: Q{iva}\n")






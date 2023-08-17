'''
producto=input("ingrese el nombre del producto: ")
precio=float(input("ingrese el precio del producto: "))
cantidad=int(input("ingrese la cantidad del producto: "))

def registrar_descuento(producto,cantidad, precio):
    if cantidad >= 1 and cantidad <= 10:
        return f"el producto ${producto} no tiene descuento"
    elif cantidad > 10 and cantidad <= 20:
        Descuento = cantidad * precio - 0.7
        return f"el descuento del producto ${producto} es de $: {Descuento}"
    elif cantidad > 20 and cantidad <= 30:
        Descuento = cantidad * precio - 0.13
        return f"El descuento del producto ${producto} es de $: {Descuento}"
    elif cantidad > 30 and cantidad <= 40:
        Descuento = cantidad * precio - 0.20
        return f"El descuento del producto ${producto} es de $: {Descuento}"
    else:
        Descuento = cantidad * precio - 0.35
        return f"el descuento del producto ${producto} es de $ {Descuento}"
    
    
print(registrar(producto, cantidad,precio))
'''
def calcular_descuento(producto, cantidad, precio):
    descuentos = {
        range(1, 11): 0,
        range(11, 21): 0.7,
        range(21, 31): 0.13,
        range(31, 42): 0.20,  # Cambiado 41 a 42
        range(42, 1000000): 0.35  # Descuento del 35% para cantidades mayores a 41
    }

    subtotal = cantidad * precio
    descuento_aplicado = 0  # Inicializar el descuento en 0
    
    for rango, descuento in descuentos.items():
        if cantidad in rango:
            descuento_aplicado = descuento
            break  # Salir del bucle al encontrar el descuento

    descuento_valor = subtotal * descuento_aplicado  # Aplicar el descuento al subtotal
    subtotal_con_descuento = subtotal - descuento_valor
    subtotal_iva = subtotal_con_descuento * 0.19
    total = subtotal_con_descuento + subtotal_iva

    mensaje_descuento = f"El descuento del producto '{producto}' es de {descuento_aplicado * 100:.2f}%."
    mensaje_descuento_valor = f"El valor del descuento aplicado es de ${descuento_valor:.2f}."
    mensaje_iva = f"El producto '{producto}' tiene un valor de IVA de ${subtotal_iva:.2f}."
    mensaje_subtotal = f"El subtotal del producto '{producto}' es de ${subtotal:.2f}."
    mensaje_total = f"El total a pagar por el producto '{producto}' es de ${total:.2f}."

    return "\n".join([mensaje_descuento, mensaje_descuento_valor, mensaje_iva, mensaje_subtotal, mensaje_total])

producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad del producto: "))

print(calcular_descuento(producto, cantidad, precio))



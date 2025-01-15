# Base de datos simulada
inventario = {
    1: {"nombre": "Producto A", "cantidad": 10},
    2: {"nombre": "Producto B", "cantidad": 20},
}

def consultar_producto(id_producto):
    if not isinstance(id_producto, int) or id_producto <= 0:
        return {"error": "El ID del producto debe ser un entero positivo."}, 400

    producto = inventario.get(id_producto)
    if not producto:
        return {"error": "Producto no encontrado."}, 404

    return {"nombre": producto["nombre"], "cantidad": producto["cantidad"]}, 200

def agregar_producto(id_producto, cantidad):
    if not isinstance(id_producto, int) or id_producto <= 0:
        return {"error": "El ID del producto debe ser un entero positivo."}, 400
    if not isinstance(cantidad, int) or cantidad <= 0:
        return {"error": "La cantidad debe ser un entero positivo."}, 400

    if id_producto in inventario:
        return {"error": "El producto ya existe."}, 400

    inventario[id_producto] = {"nombre": f"Producto {id_producto}", "cantidad": cantidad}
    return {"mensaje": "Producto agregado exitosamente."}, 201

def actualizar_stock(id_producto, nueva_cantidad):
    assert isinstance(id_producto, int) and id_producto > 0, "El ID del producto debe ser un entero positivo."
    assert isinstance(nueva_cantidad, int) and nueva_cantidad >= 0, "La cantidad nueva debe ser un entero no negativa."

    if id_producto not in inventario:
        return {"error": "Producto no encontrado."}, 404

    inventario[id_producto]["cantidad"] = nueva_cantidad
    return {"mensaje": "Stock actualizado exitosamente."}, 200

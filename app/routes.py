from app import app  # Importa el objeto app desde __init__.py
from flask import request, jsonify
from app.services.inventory import consultar_producto, agregar_producto, actualizar_stock

# Consultar producto
@app.route("/producto/<int:id_producto>", methods=["GET"])
def api_consultar_producto(id_producto):
    return consultar_producto(id_producto)

# Agregar producto
@app.route("/producto", methods=["POST"])
def api_agregar_producto():
    data = request.get_json()
    id_producto = data.get("id_producto")
    cantidad = data.get("cantidad")
    return agregar_producto(id_producto, cantidad)

# Actualizar stock
@app.route("/producto/<int:id_producto>", methods=["PUT"])
def api_actualizar_stock(id_producto):
    data = request.get_json()
    nueva_cantidad = data.get("nueva_cantidad")

    try:
        return actualizar_stock(id_producto, nueva_cantidad)
    except AssertionError as e:
        return jsonify({"error": str(e)}), 400

@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensaje": "API de Inventario. Usa los endpoints definidos para interactuar."}), 200

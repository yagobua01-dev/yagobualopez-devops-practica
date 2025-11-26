from __future__ import annotations
from typing import Dict, List, Tuple, Optional
from Tienda_online.models.Producto import Producto, ProductoElectronico, ProductoRopa
from Tienda_online.models.Usuario import Usuario, Cliente, Administrador
from Tienda_online.models.Pedido import Pedido
from datetime import datetime


class TiendaService:
    """
    Servicio central que gestiona usuarios, productos y pedidos.
    """
    def __init__(self) -> None:
        self.usuarios: Dict[str, Usuario] = {}
        self.productos: Dict[str, Producto] = {}
        self.pedidos: List[Pedido] = []

    # ---- Usuarios ----
    def registrar_usuario(self, tipo: str, nombre: str, email: str, direccion: Optional[str] = None) -> Usuario:
        """
        Registra un usuario.
        tipo: 'cliente' o 'admin'
        Devuelve el objeto Usuario creado.
        """
        tipo_lower = tipo.lower()
        if tipo_lower == "cliente":
            user = Cliente(nombre, email, direccion)
        elif tipo_lower in ("admin", "administrador"):
            user = Administrador(nombre, email)
        else:
            raise ValueError("Tipo de usuario no reconocido. Use 'cliente' o 'admin'.")
        self.usuarios[user.id] = user
        return user

    def obtener_usuario(self, user_id: str) -> Optional[Usuario]:
        return self.usuarios.get(user_id)

    # ---- Productos ----
    def añadir_producto(self, producto: Producto) -> None:
        """Añade un objeto Producto al inventario."""
        self.productos[producto.id] = producto

    def eliminar_producto(self, producto_id: str) -> bool:
        """Elimina producto por id. Devuelve True si se eliminó, False si no existía."""
        if producto_id in self.productos:
            del self.productos[producto_id]
            return True
        return False

    def listar_productos(self) -> List[Producto]:
        """Devuelve la lista de productos disponibles (objetos)."""
        return list(self.productos.values())

    def obtener_producto(self, producto_id: str) -> Optional[Producto]:
        return self.productos.get(producto_id)

    # ---- Pedidos ----
    def realizar_pedido(self, user_id: str, items: List[Tuple[str, int]]) -> Pedido:
        """
        items: lista de (producto_id, cantidad)
        Comprueba existencia de usuario (debe ser Cliente) y stock suficiente.
        Si todo ok, crea Pedido, descuenta stock y lo devuelve.
        Lanza ValueError en caso de error.
        """
        user = self.obtener_usuario(user_id)
        if user is None:
            raise ValueError("Usuario no encontrado.")
        # permitimos que administradores no realicen pedidos como clientes,
        # pero la práctica indica que Pedido está vinculado a un usuario tipo Cliente.
        from Tienda_online.models.Usuario import Cliente as ClienteClass
        if not isinstance(user, ClienteClass):
            raise ValueError("Solo clientes pueden realizar pedidos.")

        # Preparar lista de objetos y comprobaciones
        productos_a_incluir: List[Tuple[Producto, int]] = []
        for prod_id, cantidad in items:
            producto = self.obtener_producto(prod_id)
            if producto is None:
                raise ValueError(f"Producto con id {prod_id} no encontrado.")
            if not producto.hay_stock(cantidad):
                raise ValueError(f"No hay suficiente stock del producto {producto.nombre} (id {prod_id}).")
            productos_a_incluir.append((producto, int(cantidad)))

        # Descontar stock
        for producto, cantidad in productos_a_incluir:
            producto.actualizar_stock(-cantidad)

        # Crear pedido
        pedido = Pedido(user, productos_a_incluir)
        self.pedidos.append(pedido)
        return pedido

    def listar_pedidos_por_usuario(self, user_id: str) -> List[Pedido]:
        """Devuelve pedidos de un usuario ordenados por fecha (más reciente primero)."""
        pedidos_usuario = [p for p in self.pedidos if p.cliente.id == user_id]
        pedidos_usuario.sort(key=lambda p: p.fecha, reverse=True)
        return pedidos_usuario
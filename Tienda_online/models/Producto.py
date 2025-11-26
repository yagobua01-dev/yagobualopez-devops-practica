from __future__ import annotations
from typing import Any
import uuid


class Producto:
    """
    Clase base para productos.
    """
    def __init__(self, nombre: str, precio: float, stock: int) -> None:
        self.id: str = str(uuid.uuid4())
        self.nombre: str = nombre
        self.precio: float = float(precio)
        self.stock: int = int(stock)

    def hay_stock(self, cantidad: int) -> bool:
        """Devuelve True si hay al menos 'cantidad' unidades en stock."""
        return self.stock >= int(cantidad)

    def actualizar_stock(self, delta: int) -> None:
        """
        Cambia el stock en 'delta'. Si delta es negativo, baja el stock (compra).
        Lanza ValueError si no hay stock suficiente para una reducción.
        """
        nuevo = self.stock + int(delta)
        if nuevo < 0:
            raise ValueError(f"No hay stock suficiente para reducir {abs(delta)} unidades (actual: {self.stock}).")
        self.stock = nuevo

    def __str__(self) -> str:
        return f"[{self.id}] {self.nombre} - Precio: {self.precio:.2f}€ - Stock: {self.stock}"


class ProductoElectronico(Producto):
    """
    Producto electrónico con meses de garantía.
    """
    def __init__(self, nombre: str, precio: float, stock: int, garantia_meses: int) -> None:
        super().__init__(nombre, precio, stock)
        self.garantia_meses: int = int(garantia_meses)

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} - Garantía: {self.garantia_meses} meses"


class ProductoRopa(Producto):
    """
    Producto de ropa con talla y color.
    """
    def __init__(self, nombre: str, precio: float, stock: int, talla: str, color: str) -> None:
        super().__init__(nombre, precio, stock)
        self.talla: str = talla
        self.color: str = color

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} - Talla: {self.talla} - Color: {self.color}"
from __future__ import annotations
from typing import List, Tuple
from datetime import datetime
import uuid


class Pedido:
    """
    Representa un pedido asociado a un cliente y una lista de (producto, cantidad).
    items: list de tuplas (producto, cantidad)
    """
    def __init__(self, cliente, items: List[Tuple[object, int]]) -> None:
        self.id: str = str(uuid.uuid4())
        self.cliente = cliente
        self.items: List[Tuple[object, int]] = [(p, int(c)) for p, c in items]
        self.fecha: datetime = datetime.now()

    def calcular_total(self) -> float:
        """Calcula el importe total (precio * cantidad)"""
        total: float = 0.0
        for producto, cantidad in self.items:
            total += float(producto.precio) * int(cantidad)
        return total

    def __str__(self) -> str:
        lineas = [f"Pedido [{self.id}] - Fecha: {self.fecha.isoformat()}",
                  f"Cliente: {self.cliente.nombre} ({self.cliente.id})",
                  "Items:"]
        for producto, cantidad in self.items:
            lineas.append(f" - {producto.nombre} x{cantidad} @ {producto.precio:.2f}€ -> {producto.precio * cantidad:.2f}€")
        lineas.append(f"TOTAL: {self.calcular_total():.2f}€")
        return "\n".join(lineas)
from __future__ import annotations
from typing import Optional
import uuid


class Usuario:
    """
    Usuario base con id, nombre y email.
    """
    def __init__(self, nombre: str, email: str) -> None:
        self.id: str = str(uuid.uuid4())
        self.nombre: str = nombre
        self.email: str = email

    def is_admin(self) -> bool:
        """Por defecto, no es admin."""
        return False

    def __str__(self) -> str:
        role = "Administrador" if self.is_admin() else "Cliente/Usuario"
        return f"[{self.id}] {self.nombre} <{self.email}> ({role})"


class Cliente(Usuario):
    """
    Cliente con dirección postal.
    """
    def __init__(self, nombre: str, email: str, direccion: Optional[str] = None) -> None:
        super().__init__(nombre, email)
        self.direccion: Optional[str] = direccion

    def __str__(self) -> str:
        dir_text = f" - Dirección: {self.direccion}" if self.direccion else ""
        return f"{super().__str__()}{dir_text}"


class Administrador(Usuario):
    """
    Administrador: is_admin() -> True.
    """
    def is_admin(self) -> bool:
        return True
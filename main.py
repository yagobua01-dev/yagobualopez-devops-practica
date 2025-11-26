from Tienda_online.Services.Tienda_service import TiendaService
from Tienda_online.models.Producto import ProductoElectronico, ProductoRopa
from Tienda_online.models.Usuario import Cliente

def main() -> None:
    tienda = TiendaService()

    # Registrar usuarios: 3 clientes y 1 administrador
    c1 = tienda.registrar_usuario("cliente", "Ana Pérez", "ana@example.com", direccion="C/ Falsa 123")
    c2 = tienda.registrar_usuario("cliente", "Luis Gómez", "luis@example.com", direccion="Av. Siempreviva 5")
    c3 = tienda.registrar_usuario("cliente", "María Ruiz", "maria@example.com")  # sin dirección
    admin = tienda.registrar_usuario("admin", "Manager", "admin@tienda.com")

    print("Usuarios registrados:")
    for u in [c1, c2, c3, admin]:
        print(u)
    print()

    # Crear 5 productos y añadirlos al inventario
    p1 = ProductoElectronico("Auriculares Bluetooth", 59.99, 10, garantia_meses=24)
    p2 = ProductoElectronico("Smartphone X", 399.99, 5, garantia_meses=12)
    p3 = ProductoRopa("Camiseta Básica", 9.99, 30, talla="M", color="Blanco")
    p4 = ProductoRopa("Chaqueta Invierno", 79.95, 7, talla="L", color="Negro")
    p5 = ProductoRopa("Pantalón vaquero", 39.50, 12, talla="32", color="Azul")

    for p in [p1, p2, p3, p4, p5]:
        tienda.añadir_producto(p)

    print("Inventario inicial:")
    for prod in tienda.listar_productos():
        print(prod)
    print()

    # Simular 3 pedidos por distintos clientes
    # Pedido 1: Ana compra auriculares (2) y camiseta (3)
    pedido1 = tienda.realizar_pedido(c1.id, [(p1.id, 2), (p3.id, 3)])
    print("Pedido 1 realizado:")
    print(pedido1)
    print()

    # Pedido 2: Luis compra smartphone (1)
    pedido2 = tienda.realizar_pedido(c2.id, [(p2.id, 1)])
    print("Pedido 2 realizado:")
    print(pedido2)
    print()

    # Pedido 3: María compra chaqueta (1) y pantalón (2)
    pedido3 = tienda.realizar_pedido(c3.id, [(p4.id, 1), (p5.id, 2)])
    print("Pedido 3 realizado:")
    print(pedido3)
    print()

    # Comprobar histórico de pedidos de Ana
    pedidos_ana = tienda.listar_pedidos_por_usuario(c1.id)
    print(f"Histórico de pedidos de {c1.nombre}:")
    for p in pedidos_ana:
        print(f"- {p.id} ({p.fecha.isoformat()}) Total: {p.calcular_total():.2f}€")
    print()

    # Mostrar stock actualizado
    print("Stock actualizado tras pedidos:")
    for prod in tienda.listar_productos():
        print(prod)

if __name__ == "__main__":
    main()
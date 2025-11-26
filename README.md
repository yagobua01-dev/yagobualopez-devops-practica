# Práctica 2.1: Gestión de Tienda Online

## Información del Proyecto
* **Nombre del alumno:** Yago Bua Lopez
* **Asignatura:** Arquitectura del Software
* **Universidad:** Universidad Intercontinental de la Empresa

## Descripción de la Aplicación
Este proyecto consiste en una aplicación desarrollada en Python para la simulación y gestión de una tienda online. El software utiliza Programación Orientada a Objetos (POO) para administrar el flujo de comercio electrónico.

### Funcionalidades Principales:
* **Gestión de Usuarios:** Registro de usuarios diferenciando entre `Cliente` (con dirección de envío) y `Administrador`.
* **Catálogo de Productos:** Soporte para diferentes categorías de productos mediante herencia (`ProductoRopa` y `ProductoElectronico`), gestionando atributos como tallas, colores y garantías.
* **Sistema de Pedidos:**
    * Generación de pedidos únicos vinculados a clientes.
    * Cálculo automático de importes totales.
    * **Control de Stock:** Validación de disponibilidad y actualización automática del inventario tras cada compra.
* **Historial:** Consulta de pedidos realizados por cada usuario.

## Estructura del Repositorio
El código se organiza de manera modular para facilitar su mantenimiento:

* `main.py`: Script principal que ejecuta la simulación de compras y gestión.
* `Tienda_online/`: Paquete principal.
    * `models/`: Contiene las clases `Usuario`, `Producto` y `Pedido`.
    * `Services/`: Contiene `TiendaService`, encargado de la lógica de negocio.

## Ejecución
Para iniciar la aplicación, ejecuta el siguiente comando desde la raíz del proyecto:

```bash
python main.py

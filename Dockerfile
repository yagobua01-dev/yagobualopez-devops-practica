# 1. Usar la imagen base python:3.12-slim (Punto 2.a)
FROM python:3.12-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 2. Copiar el archivo de dependencias (Punto 2.b)
COPY requirements.txt .

# 3. Instalar las dependencias (Punto 2.c)
# Usamos --no-cache-dir para mantener la imagen ligera
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar el resto del código fuente (Punto 2.d)
COPY . .

# 5. Cambiar permisos para ejecución (Punto 2.e)
# Esto da permisos de ejecución al archivo principal
RUN chmod +x main.py

# 6. Comando de inicio (Punto 2.f)
CMD ["python", "main.py"] 
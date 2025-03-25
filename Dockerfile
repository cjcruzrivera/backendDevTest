# Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copiar requirements e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY app.py .

# Puerto donde corre la app (5000 según tu prueba)
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
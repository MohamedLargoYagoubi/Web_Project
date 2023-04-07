# Imagen base de Python
FROM python:3.11

# Directorio de trabajo
WORKDIR /code

# Copiar los archivos requerimientos y el proyecto a la imagen
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Comando para ejecutar el proyecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

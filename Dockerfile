FROM python:3.10.0
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /opt/back_end
COPY . /opt/back_end
# Agrego variables de entorno personalizadas
# en este caso correspondientes a la Base de Datos.
ENV POSTGRES_DB=cocoche_db
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_HOST=db
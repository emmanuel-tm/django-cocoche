# Django Dev

## Pasos para poder utilizar y ejecutar el proyecto:

- En la Consola o Terminal ejecutar el siguiente comando: 

**$** `git clone https://github.com/emmanuel-tm/django-cocoche.git`

- Una vez clonado el repositorio se deben seguir los siguientes pasos:

### 1. Correr el proyecto
Siempre en el mismo directorio del archivo *docker-compose.yml*
**$** `docker-compose up`

### 2. Correr la línea de comandos dentro del contenedor

**$** `docker exec -i -t cocoche_django bash`

Nos va a devolver a nuestra consola, una consola dentro del contenedor de software.


Una vez dentro ejecutamos el comando:

**$** `cd /opt/back_end/my_project` 

### 3. Iniciar el servidor

**NOTA:** Se actualizó el archivo docker-compose.yml, de esta manera, ya no se
requiere iniciar el servidor (se inicia automáticamente al levantar el contenedor).
De todas formas, en caso de que no suceda así o haya algún error que impida que iniciar
el servidor, se deja a continuación el comado para hacerlo:

(Siempre dentro de nuestro contenedor de software - Comando N°2)  
Tenemos que ir a la carpeta donde se encuentra el archivo *manage.py*  

**$** `python manage.py runserver 0.0.0.0:8000`  

### 4. Ejecutar los siguientes comandos para realizar la primera migración:  

**$** `python manage.py makemigrations`

**$** `python manage.py migrate` 

### 5. Creamos un super usuario:  

**$** `python manage.py createsuperuser`

### 6. Detener la ejecución de nuestro contenedor y nuestro servidor
Tenemos que estar en la terminal que nos muestra los mensajes del servidor, tomada por el contenedor.
Tan solo con el comando `ctrl + c`  se detiene la ejecución de nuestro contenedor.  

Una forma alternativa es con el siguiente comando en la terminal del host:

**$** `docker stop django_dev`  

O también puede ser con docker-compose:
Tenemos que estar en la carpeta que contiene el archivo *docker-compose.yml* y hacer:


**$** `docker-compose down`  

- Una vez clonado el repositorio se debe ingresar a la carpeta del respositorio, y estar en la misma dirección/path que los archivos "Dockerfile" y "docker-compose.yml". Una vez ubicado allí, ejecutar los siguientes comandos (**NOTA**: se debe tener instalado docker y docker-compose en tu sistema):

    - *docker-compose up*

- Con el comando anterior ya tenemos nuestra imagen creada y el contenedor corriendo, por lo cual queda tomada la terminal. Lo siguiente es abrir una nueva terminal (sin cerrar la anterior) y entrar dentro del container(contenedor) por lo que se debe ejecutar el siguiente comando:

    - *docker exec -i -t "nombre_del_contenedor" bash*

- Ya estamos dentro del contenedor, entonces procedemos.


## Endpoint disponibles:

    - http://localhost:8000/cocoche/create_user --> Se realiza un POST para registrar un nuevo usuario en formato JSON.

    - http://localhost:8000/cocoche/get_cars/list --> Devuelve una lista de todos los vehículos.

    - http://localhost:8000/cocoche/get_ford_cars --> Devuelve una lista de todos los vehículos cuya marca(brand) es "FORD".

    - http://localhost:8000/admin/ --> Acceso al Administrador de Django (Django Admin).

    - http://localhost:8080/ --> Acceso al Servicio de Adminer para poder visualizar las distintas tablas de la base de datos.

    - http://localhost:8000/api-docs --> Devuelve un template con la documentación de todos los endpoints disponibles y sus APIs.


**NOTA:** Para este proyecto no se requiere de ningún tipo de permisos para acceder a los *recursos* a través de los ENDPOINTS.


---
# Autor
Emmanuel Torres Molina

# Consultas
eotorresmolina@gmail.com
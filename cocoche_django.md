# **cocoche-django**

# **Ejercicio API REST**
Desarrollar una API en Python (utilizando el framework Django) que exponga los siguientes endpoints:

## **GET /get_ford_cars**
Devuelve una lista de autos cuya marca es "FORD". Para obtener la lista de autos completa, consumir el endpoint /car_listing_presentation?list_length (pasar 100 como parámetro). La API a consumir tiene la siguiente URL de base: http://server.cocoche.com.ar.

**Aclaración**: El sistema de donde se obtiene la lista de autos, Cocoche, actualiza su base de autos todos los lunes a las 3am (tenerlo en cuenta).

## **POST /create_user**
El endpoint recibe como parámetro un JSON con el siguiente formato: {"name": "string", "phone": "string", "email": "string"} y devuelva otro JSON: {"id": "string", "createdAt": "dd-mm-AAAA"}

El sistema deberá persistir los 5 campos (3 del request + id random + fecha de creación). Si el request intenta registrar un email existente, el sistema debe arrojar el error correspondiente. Los usuarios creados deben ser guardados en una base de datos. Especificar las credenciales de acceso a la base en este mismo archivo. **Usuario:** *admin* ; **Contraseña:** *admin* ; **Nombre de la DB:** *cocoche_db*.

**ACLARACIÓN:** Todo el código debe ser desarrollado en una rama aparte. Cuando se considere terminado, realizar un Merge Request (también llamado PR) sobre la rama Master.
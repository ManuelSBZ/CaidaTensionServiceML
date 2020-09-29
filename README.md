# CaidaTensionServiceML
COMPONENTE API - Modelo predictivo de caída de Tensión en Linea de Cobre

El presente proyecto anexa un modelo predictivo que estima el porcentaje de caida de tensión de un cable de cobre de calibre 1/0 AWG
de 100mt de longitud, tensionada con 240V ac.

- Tecnologias principales:
  1. Sklearn
  2. Pandas
  3. Scipy
  3. Gunicorn 20.0.4
  4. Django
  5. Django-RestFramework
  6. Sqlite
  7. Docker 19.03.12 
  8. Python 3.6
  
- Para explorar la solucion se debe:
  1. Clonar el repositorio.
  2. Abrir simbolo del sistema.
  3. Ubicarse desde la consola en la carpeta que contiene el docker-compose.yaml dentro del proyecto.
  4. Ejecutar " docker-compose up --build ".
  5. Para explorar la solucion se debe ingresar el siguiente link en el cliente para probar apis(ej: postman) de su preferencia.
  
- Para probar la api se recomienda hacer uso de postman, cliente en el cual se tiene una coleccion de 6 endpoints para las distintas operaciones CRUD. Para acceder a la colección usar el siguiente url Postman https://www.getpostman.com/collections/c71ce12bab9a14ebb0ea .

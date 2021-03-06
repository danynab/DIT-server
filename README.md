# DIT-server

Servidor web encargado del procesamiento de datos y gestión de la aplicación Do It Together.

## API

A continuación se muestra una pequeña descripción de los *endpoints* existentes en la API.

HTTP Method | Ruta | Descripción
:----------:|------|-------------
GET | /events?lat=\_&lng=\_&radius=\_ | Listado con todos los eventos cercanos en funcion de una latitud, logitud y radio de proximidad.
GET | /events/**X** | Detalle del evento con id **X**.
POST | /events | Crea un nuevo evento.
PUT | /events/**X** | Actualiza los datos del evento con id **X** con los datos recibidos en el cuerpo de la petición.
DELETE | /events/**X** | Elimina el evento con id **X**.
GET | /events/**X**/attendees | Listado con los asistentes al evento con id **X**.
POST | /events/**X**/attendees | Añade un asistente cuyos datos están en el cuerpo de la petición al evento con id **X**.
DELETE | /events/**X**/attendess/**Y** | Elimina un asistente cuyo usuario asociado tiene el id **Y** del evento con id **X**.
GET | /categories | Listado con todos las categorías de eventos.
GET | /categories/**X** | Detalle de la categoría con id **X**.
GET | /categories/**X**/events?lat=\_&lng=\_&radius=\_ | Listado con todos los eventos cercanos de la categoría con id **X** en funcion de una latitud, logitud y radio de proximidad.
GET | /categories/**X**/places?lat=\_&lng=\_&radius=\_&elements=\_ | Listado con los lugares cercanos recomendados de la categoría con id **X** en función de una latitud, longitud y radio de proximidad. El atributo elements indica el número de resultados a devolver.
GET | /users/**X**/events | Listado con todos los eventos creados por el usuario con id **X**.
GET | /users/**X**/attendees/events | Listado con todos los eventos a los que el usuario con id **X** va a asistir.

Todas las peticiones que devuelvan varios eventos se pueden particionar indicando el id del último evento devuelto en la consulta anterior y el número de elementos a devolver. 
Ejemplo: 
```
/events?fromId=5&elements=10
```

##  INSTALACIÓN

La API ha sido testeada baja Python3. A continuación se detallan los pasos para su instalación en Ubuntu y Mac OS X y ejecución.

Instalar las herramientas de Python3:

* Ubuntu:
```bash
sudo apt-get update
sudo apt-get -y install python3 python3-pip
sudo pip3 install virtualenv
```

* Mac OS X (requiere [brew](http://brew.sh)):
```bash
sudo brew update
brew install python3
sudo pip3 install virtualenv
```

Clonar el repositorio y acceder a él:

```bash
git clone https://github.com/danynab/DIT-server.git
cd DIT-server
```

Crear el entorno virtual:

```bash
virtualenv venv
```

Activamos el entorno virtual:

```bash
. venv/bin/activate
```

Instalar las dependencias:

```bash
pip3 install -r dependencies
```

Desactivamos el entorno virtual:

```bash
deactivate
```

## Ejecución

A continuación se detallan los pasos a seguir para ejecutar el servidor web.

Activamos el entorno virtual:

```bash
. venv/bin/activate
```

Ejecutar el servidor:
```bash
python3 run.py
```

La activación del entorno virtual será necesaria cada vez que se quiera ejecutar el servidor. Para desactivar el entorno virtual puede utilizarse el comando:

```bash
deactivate
```

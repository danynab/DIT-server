# DIT-server

Servidor web encargado del procesamiento de datos y gestión de la aplicación Do It Together.

## API

A continuación se muestra una pequeña descripción de los *endpoints* existentes en la API.

HTTP Method | Ruta | Descripción
:----------:|------|-------------
GET | /events?lat=\_&lng=\_&radius=\_ | Listado con todos los eventos cercanos en funcion de una latitud, logitud y radio de proximidad.
GET | /events/**X** | Detalle del evento con id **X**
POST | /events | Crea un nuevo evento.
PUT | /events/**X** | Actualiza los datos del evento con id **X**
DELETE | /events/**X** | Elimina el evento con id **X**.
GET | /categories | Listado con todos las categorías de eventos.
GET | /categories/**X**/events?lat=\_&lng=\_&radius=\_ | Listado con todos los eventos cercanos de la categoría con id **X** en funcion de una latitud, logitud y radio de proximidad.


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

Activamos el entorno virtual:

```bash
. venv/bin/activate
```

Ejecutar el servidor:
```bash
python run.py
```

La activación del entorno virtual será necesaria cada vez que se quiera ejecutar el servidor. Para desactivar el entorno virtual puede utilizarse el comando:

```bash
deactivate
```

fondosMutuosData
================

script que permite obtener el valor diario de las cuotas de distintos fondos mutuos, luego esta informaci√n es enviada a una base de datos mongo via un servidor API creado en nodejs

### CONFIGURACION ###

Configurar informacion de los fondos mutuos a buscar, editar el archivo fm_names.xml

Configurar las credenciales de la base de datos mongo, editar el archivo ~/.bash_profile

```sh 
cat ~/.bash_profile
export MONGO_DEV_HOST=hostname_server
export MONGO_DEV_PORT=port_server
export MONGO_DEV_DB=collection
export MONGO_DEV_USERNAME=user
export MONGO_DEV_PASSWORD=password
export MONGO_DEV_URI=mongodb://${MONGO_DEV_USERNAME}:${MONGO_DEV_PASSWORD}@${MONGO_DEV_HOST}:${MONGO_DEV_PORT}/${MONGO_DEV_DB}
```

Instalar dependencias para servidor nodejs

```sh
cd server
npm install
```

Iniciar servidor 

```sh
cd server
node server.js
```

Ejecutar el script

```sh
python main.py "2013-10-28"
```

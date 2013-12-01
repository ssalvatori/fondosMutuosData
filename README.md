fondosMutuosData
================

get daily quote value for specific "fondos mutuos" using http://www.aafm.cl/

ugly working code =)

### USAGE ###

1. edit fm_names.xml 
2. python main.py "2013-10-28"

### SERVER ###
set mongo credentials in bash_profile

```sh
export MONGO_DEV_HOST=hostname_server
export MONGO_DEV_PORT=port_server
export MONGO_DEV_DB=collection
export MONGO_DEV_USERNAME=user
export MONGO_DEV_PASSWORD=password
export MONGO_DEV_URI=mongodb://${MONGO_DEV_USERNAME}:${MONGO_DEV_PASSWORD}@${MONGO_DEV_HOST}:${MONGO_DEV_PORT}/${MONGO_DEV_DB}
```

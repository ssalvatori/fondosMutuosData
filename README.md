fondosMutuosData
================

script que permite obtener el valor diario de las cuotas de distintos fondos mutuos, luego esta información es enviada a una base de datos mongo via un servidor API creado en nodejs

### Instacion dependencias

```sh 
easy_install httplib2
easy_install BeautifulSoup4
easy_install urllib2
´´´

### Modificacion de endpoint

Editar el archivo main.py y cambiar la url que aparece como http://192.168.33.10

### Ejectutar script

```sh
python main.py 2013-10-28
```
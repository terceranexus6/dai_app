# Desarrollo de Aplicaciones de Internet
## 4º GII

## Asignatura

Este repositorio es de la asignatura de DAI, de 4º de GII. Tiene una licencia libre GNU, el objetivo del repositorio es guardar las prácticas de 2017-2018. Aunque la práctica original habla de restaurantes, he aplicado los mismos procedimientos para una web sobre HAMLET.

## Desarrollo

Para organizar correctamente Modelo-Vista-Controlador he utilizado **Django**, migrando el contenido original de **Flask**. Todas las prácticas las he realizado usando virtualización, con `source bin/activate`.

Para demostrar el uso de la vista con `views.py` he utilizado contexto y etiquetas `{{contenido}}` dentro del html. Por otro lado he hecho uso de `static` para dinamizar las plantillas. Para ello he usado la etiqueta `{% load staticfiles %}` al inicio del html, y he incluído imágenes `{% static "images/blade-runner-1982-10-g.jpg" %}`, contenido de estilo css `{% static "css/style.css" %}` y jquery `{% static "js/funcion.js" %}`.

He encontrado, sin embargo, algunos problemas con la base de datos porque no consigo que la versión de Mongo sea la correcta.

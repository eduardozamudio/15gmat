# Programación III: Bases de datos y Programación

Este repositorio contiene recursos asociados a las actividades prácticas de la asignatura Programación III. Bases de Datos y Programación, correspondiente al Grado en Matemáticas de la VIU

Los recursos asociados se organizan en 

*  **notebooks** -- libretas Jupyter 
* **sql** -- rutinas SQL
* **scripts** -- rutinas Python
* **src** -- módulo Python con una capa de persistencia para el modelo contenido en sql

## Requerimientos
Las dependencias son gestionadas mediante Conda, las cuales se encuentran definidas en el archivo de configuración `environment.yml`

El ambiente 15gmat puede ser creado a partir de
`conda env create -f environment.yml`


Las variables de ambiente se encuentan definida en archivos **.env** como .env-example, los cuales deben ser instanciados con el nombre predeterminado .env


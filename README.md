# AirBnB clone - The console

Holberton Peru
(logo.png')

## Índice
1. [Descripción del Proyecto]
2. [Instalación y Compilación]
3. [Modos de Ejecución]
4. [Uso]
5. [Comandos]
6. [Pruebas]
7. [Colaboradores]

### Descripción del Proyecto:

Este proyecto es la primera fase de las 4 que componen el proyecto total "AirBnB clone".
## La consola:

Es un intérprete de línea de comandos que te permite gestionar y administrar los objetos
entre las clases utilizadas y su almacenamiento dentro de la aplicación.

### ¿Qué puede hacer la consola?

La consola permite mostrar, crear, destruir y actualizar los objetos.

## Instalación y Compilación:

Para empezar, clona el repositorio:

```bash
https://github.com/Eduarvallejos/holbertonschool-AirBnB_clone

```
Ingrese al directorio holbertonschool-AirBnB_clone y ejecute el comando:

```bash
./console.py

```
### Modos de ejecución:

```bash
./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

```
## Modo no interactivo:

```bash
echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
=======================================
EOF  help  quit
(hbnb) 
$

```
###Uso:
## Comandos:
##Comandos basicos:

ayuda: muestra la ayuda de la consola.

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)

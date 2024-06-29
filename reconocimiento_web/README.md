```sh
# Reconocimiento Web con Python

Este proyecto es un script de Python que utiliza la biblioteca `requests`
para realizar fuerza bruta de directorios en un sitio web específico. Utiliza una lista de palabras
(`common.txt`) para intentar descubrir archivos o directorios en el servidor web.

## Requisitos

- Python 3.x
- Biblioteca `requests`

Puedes instalar la biblioteca `requests` usando pip:


pip install requests

Uso:
Asegúrate de que el archivo common.txt se encuentra en el directorio adecuado. En este caso, el archivo debe 
estar un nivel por encima del directorio del script.

Descarga una wordlist adecuada desde fuentes como SecLists u otras fuentes relevantes y sustitúyela por common.txt.
Edita el script para cambiar el parámetro url según sea necesario.

Ejecuta el script:
python recon.py

Estructura del Proyecto
reconocimiento_web/
├── recon.py
└── ../common.txt

Script
El script recon.py realiza las siguientes tareas:

Lee la lista de palabras del archivo common.txt.
Intenta acceder a cada URL formada por la combinación del dominio base y cada palabra de la lista.
Imprime un mensaje si encuentra un archivo o directorio en el servidor web.

Notas
Asegúrate de que el archivo common.txt está correctamente ubicado en la ruta especificada.
Puedes modificar el parámetro url en el script para adaptarlo a tus necesidades.
El script maneja errores de conexión y responde adecuadamente a diferentes códigos de estado HTTP.

Contribución
Si deseas contribuir a este proyecto, por favor crea un fork del repositorio,
realiza tus cambios y envía un pull request. Todas las contribuciones son bienvenidas.


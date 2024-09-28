# Converter_MKV_to_MP4

## Descripción
Script en Python para convertir archivos .MKV a .MP4 utilizando FFMPEG.

## Instalación
Es necesario contar con [FFMPEG](https://ffmpeg.org/download.html) en el sistema. En Windows se debe agregar en el PATH.

Siga las intrucciones de la página oficial.

### Instalación del Script

Debe contar con Python 3.12 o superior y Poetry como gestor de dependencias.

Utilizando pip instale Poetry `pip install poetry`. Ingrese a la carpeta del proyecto y ejecute los siguientes comandos: `poetry install` y `poetry shell`.

## Exportación a PIP

En el archivo `pyproject.toml` realice las siguientes modificaciones:
* `name = "app" -> "wololo"`
*  en [tool.poetry.scripts] agregue `wololo = "wololo.main:main"`. Además cambie el nombre de la carpeta "app" por "wololo".

Utilice el comando `poetry build`.

Finalmente, instale el archivo .whl de la carpeta dist utilizando pip.
EJ: `pip install wololo-0.2.0-py3-none-any.whl`.

## Iniciar Script

Tras la configuración e instalación, para correr el script ejecute `poetry run start {Ruta que contiene los archivos .mkv}`

Si exportó mediante PIP el programa, ejecutelo de esta manera: `wololo {Ruta que contiene los archivos .mkv}`

# Generador de Diagramas PERT y cálculo de información relevante

Este proyecto consiste en un script de Python que permite generar un Diagrama PERT (Program Evaluation and Review Technique) y calcular información relevante sobre las actividades que lo conforman, tales como inicio más pronto, terminación más pronto, inicio más lejano, terminación más lejana, holgura y ruta crítica.

## Cómo utilizar el script

Para utilizar el script, es necesario contar con Python instalado en su sistema. Una vez instalado, debe seguir los siguientes pasos:

1. Clonar el repositorio en su máquina local.
2. Se debe insertar la list con el nombre de las actividades duración y precedencias. (name, time, pre) 
3. Abrir una terminal o consola de comandos y ubicarse en el directorio raíz del proyecto.
4. Ejecutar el comando `python -m pip install -r requirements.txt` para instalar las librerias requeridas.
4. Ejecutar el script con el siguiente comando: `python app.py`.
5. Al finalizar, el script generará el Diagrama PERT y mostrará información relevante sobre las actividades ingresadas en un archivo PDF en la carpeta *export*.

## Dependencias

El script usa solo usa Digraph como dependencia externa y fue probado en Python 3.9.6.
@echo off

REM ============================================================================
REM Script de conveniencia SOLO PARA WINDOWS.
REM Ejecuta una unica vez el recolector crudo, activando el venv local con
REM rutas de Windows (..\..\.venv\Scripts\activate.bat).
REM
REM Para ejecucion programada multiplataforma (Windows/Linux/Mac/Docker), usa
REM en su lugar: python src/etl/ejecutar_programador.py
REM Ese script hace lo mismo (recolector cada 5 min + agregador cada hora)
REM sin depender del sistema operativo, y es el que corre dentro de Docker.
REM
REM Este .bat se mantiene solo como atajo manual local en Windows.
REM ============================================================================


cd /d "%~dp0"

echo Carpeta actual:
cd

echo Activando entorno virtual...
call ..\..\.venv\Scripts\activate.bat

echo Ejecutando recolector...

python recolector_crudo.py >> ..\..\logs\recolector.log 2>&1

echo Codigo salida: %errorlevel%
@echo off

REM ============================================================================
REM Script de conveniencia SOLO PARA WINDOWS.
REM Ejecuta una unica vez el agregador horario, activando el venv local con
REM rutas de Windows (..\..\.venv\Scripts\activate.bat).
REM
REM Para ejecucion programada multiplataforma (Windows/Linux/Mac/Docker), usa
REM en su lugar: python src/etl/ejecutar_programador.py
REM Ese script hace lo mismo (agregador cada hora + recolector cada 5 min)
REM sin depender del sistema operativo, y es el que corre dentro de Docker.
REM
REM Este .bat se mantiene solo como atajo manual local en Windows.
REM ============================================================================

cd /d "%~dp0"

call ..\..\.venv\Scripts\activate.bat

python agregador_horario.py >> ..\..\logs\agregador.log 2>&1

exit /b %errorlevel%
@echo off
@echo "Enter Proyect name"
set /p proj_name=
set building="Building django project %proj_name%"
@echo %building%
python c:/Python27/Scripts/django-admin.py startproject %proj_name%
pause
@echo off
cd ./backend
call python -m venv macrocounter-env
call ./macrocounter-env/Scripts/activate
call pip install -r requirements.txt

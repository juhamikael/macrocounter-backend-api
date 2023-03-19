@echo on
cd ./backend
call ./macrocounter-env/Scripts/activate
call uvicorn main:app --reload
@pause



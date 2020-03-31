@echo off

title Run application batch

set "current_path=%CD%"
for %%a in ("%current_path%") do set "parent_path=%%~dpa"
set "data_path=%parent_dir%data\"
set "def_data_file=sample.txt"
set "data_file=%data_path%%def_data_file%"

if "%1" == ""   goto run
    
set "file_input=%1"

rem pathname
if exist %file_input% (

    set "data_file=%file_input%"
    goto run
)

if exist "%data_path%%file_input%" (

    set "data_file=%data_path%%file_input%" 
    goto run
)

if exist "%file_input%" (

    set "data_file=%parent_path%%file_input%"
    goto run
)

   
:run 
php "%current_path%\app.php" < "%data_file%"  


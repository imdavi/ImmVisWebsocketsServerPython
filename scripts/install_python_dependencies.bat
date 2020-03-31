@ECHO OFF

SET SCRIPT_DIR=%~dp0

SET ROOT_DIR=%SCRIPT_DIR%..

WHERE python >nul 2>nul
if %ERRORLEVEL% EQU 0  (
    WHERE pip >nul 2>nul
    if %ERRORLEVEL% EQU 0  (
        pip install -r %ROOT_DIR%/requirements.txt
        echo Success! You are able to use ImmVis Websocket server now!
    ) else (
        echo It seems that pip is not installed. Please install Python and PIP to run this script.
    )
) else (
    echo It seems that Python is not installed. Please install Python to run this script.
)

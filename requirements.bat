@echo off
setlocal

REM Function to check and handle errors
:check_error
if %errorlevel% neq 0 (
    echo Error occurred: %1
    call :cleanup
    exit /b %errorlevel%
)

REM Function to clean up in case of failure
:cleanup
if exist venv (
    echo Cleaning up...
    rmdir /s /q venv
)
goto :EOF

REM Check if Python is installed
echo Checking for Python installation...
python --version >nul 2>&1
call :check_error "Python is not installed. Please install Python before running this script."

REM Check for pip installation
echo Checking for pip installation...
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Pip is not installed. Installing pip...
    python -m ensurepip --upgrade
    call :check_error "Failed to install pip."
)

REM Install pygame and pyarmor
echo Installing pygame==2.4.0...
pip install pygame==2.4.0
call :check_error "Failed to install pygame."

echo Installing pyarmor...
pip install pyarmor
call :check_error "Failed to install pyarmor."

echo Installation complete.
pause

endlocal
exit /b 0

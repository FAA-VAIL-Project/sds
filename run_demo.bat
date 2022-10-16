@echo off

rem --------------------------------------------------------------------------------
rem
rem run_demo.bat: Demo project polynomial multiplication.
rem
rem --------------------------------------------------------------------------------

setlocal EnableDelayedExpansion

set POLYNOMIAL_CHOICE_ACTION_DEFAULT=data
set POLYNOMIAL_CHOICE_METHOD_DEFAULT=fft
set POLYNOMIAL_CHOICE_SETUP_DEFAULT=no
set POLYNOMIAL_FILE_NAME=..\polynom_data.json

set "POLYNOMIAL_BENCHMARK_VCVARSALL=C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Auxiliary\Build\vcvarsall.bat"

if ["%1"] EQU [""] (
    echo ===============================================================================
    echo complete             - All implemented programming languages.
    echo data                 - Create task data.
    echo -------------------------------------------------------------------------------
    echo c                    - C++
    echo python               - Python 3
    echo rust                 - Rust
    echo -------------------------------------------------------------------------------
    set /P POLYNOMIAL_CHOICE_ACTION="Enter the desired action [default: %POLYNOMIAL_CHOICE_ACTION_DEFAULT%] "

    if ["!POLYNOMIAL_CHOICE_ACTION!"] EQU [""] (
        set POLYNOMIAL_CHOICE_ACTION=%POLYNOMIAL_CHOICE_ACTION_DEFAULT%
    )
) else (
    set POLYNOMIAL_CHOICE_ACTION=%1
)

if ["%POLYNOMIAL_CHOICE_ACTION%"] NEQ ["data"] (
    if ["%2"] EQU [""] (
        echo ===============================================================================
        echo fft                  - Fast Fourier Transform      - Python
        echo numpy                - NumPy                       - Python
        echo simple               - Simple multiplication       - Python
        echo -------------------------------------------------------------------------------
        set /P POLYNOMIAL_CHOICE_METHOD="Enter the desired action [default: %POLYNOMIAL_CHOICE_METHOD_DEFAULT%] "

        if ["!POLYNOMIAL_CHOICE_METHOD!"] EQU [""] (
            set POLYNOMIAL_CHOICE_METHOD=%POLYNOMIAL_CHOICE_METHOD_DEFAULT%
        )
    ) else (
        set POLYNOMIAL_CHOICE_METHOD=%2
    )
)

if ["%3"] EQU [""] (
    echo ===============================================================================
    echo Setup Environment    - yes / no.
    echo -------------------------------------------------------------------------------
    set /P POLYNOMIAL_CHOICE_SETUP="Enter the desired action [default: %POLYNOMIAL_CHOICE_SETUP_DEFAULT%] "

    if ["!POLYNOMIAL_CHOICE_SETUP!"] EQU [""] (
        set POLYNOMIAL_CHOICE_SETUP=%POLYNOMIAL_CHOICE_SETUP_DEFAULT%
    )
) else (
    set POLYNOMIAL_CHOICE_SETUP=%3
)

set POLYNOMIAL_IS_CPP=no
set POLYNOMIAL_IS_DATA=no
set POLYNOMIAL_IS_PYTHON=no
set POLYNOMIAL_IS_RUST=no

if ["%POLYNOMIAL_CHOICE_ACTION%"] EQU ["complete"] (
    set POLYNOMIAL_IS_CPP=yes
    set POLYNOMIAL_IS_PYTHON=yes
    set POLYNOMIAL_IS_RUST=yes
)

if ["%POLYNOMIAL_CHOICE_ACTION%"] EQU ["c++"] (
    set POLYNOMIAL_IS_CPP=yes
)

if ["%POLYNOMIAL_CHOICE_ACTION%"] EQU ["data"] (
    set POLYNOMIAL_IS_DATA=yes
)

if ["%POLYNOMIAL_CHOICE_ACTION%"] EQU ["python"] (
    set POLYNOMIAL_IS_PYTHON=yes
)

if ["%POLYNOMIAL_CHOICE_ACTION%"] EQU ["rust"] (
    set POLYNOMIAL_IS_RUST=yes
)

set ERRORLEVEL=0

echo ===============================================================================
echo Start %0
echo -------------------------------------------------------------------------------
echo Polynomial Multiplication.
echo -------------------------------------------------------------------------------
echo CHOICE_ACTION        : %POLYNOMIAL_CHOICE_ACTION%
if ["%POLYNOMIAL_CHOICE_ACTION%"] NEQ ["data"] (
    echo CHOICE_METHOD        : %POLYNOMIAL_CHOICE_METHOD%
)
if ["%POLYNOMIAL_IS_DATA%"] EQU ["yes"] (
    echo CHOICE_SETUP         : %POLYNOMIAL_CHOICE_SETUP%
)
echo -------------------------------------------------------------------------------
echo C++                  : %POLYNOMIAL_IS_CPP%
echo Data                 : %POLYNOMIAL_IS_DATA%
echo Python               : %POLYNOMIAL_IS_PYTHON%
echo Rust                 : %POLYNOMIAL_IS_RUST%
echo -------------------------------------------------------------------------------
echo:| TIME
echo ===============================================================================

if ["%POLYNOMIAL_IS_DATA%"] EQU ["yes"] (
    cd lang\python
    if ["%POLYNOMIAL_CHOICE_SETUP%"] EQU ["yes"] (
        make pipenv
    )
    echo -------------------------------------------------------------------------------
    set PYTHONPATH=src\polynomial
    pipenv run python src\polynomial\launcher.py -a generate
    if ERRORLEVEL 1 (
        cd ..\..
        echo -------------------------------------------------------------------------------
        echo Processing of the script: %0 - step: 'python src\polynomial\launcher.py -a generate
    )
    cd ..\..
)

if ["%POLYNOMIAL_IS_PYTHON%"] EQU ["yes"] (
    cd lang\python
    if ["%POLYNOMIAL_CHOICE_SETUP%"] EQU ["yes"] (
        make pipenv
    )
    echo -------------------------------------------------------------------------------
    set PYTHONPATH=src\polynomial
    pipenv run python src\polynomial\launcher.py -a multiply -m %POLYNOMIAL_CHOICE_METHOD%
    if ERRORLEVEL 1 (
        cd ..\..
        echo -------------------------------------------------------------------------------
        echo Processing of the script: %0 - step: 'python src\polynomial\launcher.py -a multiply -m %POLYNOMIAL_CHOICE_METHOD%
    )
    cd ..\..
)

echo -------------------------------------------------------------------------------
echo:| TIME
echo -------------------------------------------------------------------------------
echo End   %0
echo ===============================================================================

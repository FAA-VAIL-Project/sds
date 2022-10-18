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

set POLYNOMIAL_IS_CPP=no
set POLYNOMIAL_IS_DATA=no
set POLYNOMIAL_IS_PYTHON_FFT=no
set POLYNOMIAL_IS_PYTHON_NUMPY=no
set POLYNOMIAL_IS_PYTHON_SIMPLE=no
set POLYNOMIAL_IS_RUST=no

if ["%1"] EQU [""] (
    echo ===============================================================================
    echo complete             - All implemented programming languages.
    echo complete_python      - All Python related methods (fft, numpy and simple.
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

if ["%POLYNOMIAL_CHOICE_ACTION%"] EQU ["python"] (
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

if ["%POLYNOMIAL_CHOICE_ACTION%"] EQU ["complete"] (
    set POLYNOMIAL_IS_CPP=yes
    set POLYNOMIAL_IS_DATA=yes
    set POLYNOMIAL_IS_PYTHON_FFT=yes
    set POLYNOMIAL_IS_PYTHON_NUMPY=yes
    set POLYNOMIAL_IS_PYTHON_SIMPLE=yes
    set POLYNOMIAL_IS_RUST=yes
)

if ["%POLYNOMIAL_CHOICE_ACTION%"] EQU ["complete_python"] (
    set POLYNOMIAL_IS_DATA=yes
    set POLYNOMIAL_IS_PYTHON_FFT=yes
    set POLYNOMIAL_IS_PYTHON_NUMPY=yes
    set POLYNOMIAL_IS_PYTHON_SIMPLE=yes
)

if ["%POLYNOMIAL_CHOICE_ACTION%"] EQU ["c++"] (
    set POLYNOMIAL_IS_CPP=yes
)

if ["%POLYNOMIAL_CHOICE_ACTION%"] EQU ["data"] (
    set POLYNOMIAL_IS_DATA=yes
)

if ["%POLYNOMIAL_CHOICE_ACTION%"] EQU ["python"] (
    if ["%POLYNOMIAL_CHOICE_METHOD%"] EQU ["fft"] (
        set POLYNOMIAL_IS_PYTHON_FFT=yes
    )
    if ["%POLYNOMIAL_CHOICE_METHOD%"] EQU ["numpy"] (
        set POLYNOMIAL_IS_PYTHON_NUMPY=yes
    )
    if ["%POLYNOMIAL_CHOICE_METHOD%"] EQU ["simple"] (
        set POLYNOMIAL_IS_PYTHON_SIMPLE=yes
    )
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
echo CHOICE_SETUP         : %POLYNOMIAL_CHOICE_SETUP%
echo -------------------------------------------------------------------------------
echo C++                  : %POLYNOMIAL_IS_CPP%
echo Data                 : %POLYNOMIAL_IS_DATA%
echo Python fft           : %POLYNOMIAL_IS_PYTHON_FFT%
echo Python numpy         : %POLYNOMIAL_IS_PYTHON_NUMPY%
echo Python simple        : %POLYNOMIAL_IS_PYTHON_SIMPLE%
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

if ["%POLYNOMIAL_IS_PYTHON_FFT%"] EQU ["yes"] (
    cd lang\python
    if ["%POLYNOMIAL_CHOICE_SETUP%"] EQU ["yes"] (
        make pipenv
    )
    echo -------------------------------------------------------------------------------
    set PYTHONPATH=src\polynomial
    pipenv run python src\polynomial\launcher.py -a multiply -m fft
    if ERRORLEVEL 1 (
        cd ..\..
        echo -------------------------------------------------------------------------------
        echo Processing of the script: %0 - step: 'python src\polynomial\launcher.py -a multiply -m fft
    )
    cd ..\..
)

if ["%POLYNOMIAL_IS_PYTHON_NUMPY%"] EQU ["yes"] (
    cd lang\python
    if ["%POLYNOMIAL_CHOICE_SETUP%"] EQU ["yes"] (
        make pipenv
    )
    echo -------------------------------------------------------------------------------
    set PYTHONPATH=src\polynomial
    pipenv run python src\polynomial\launcher.py -a multiply -m numpy
    if ERRORLEVEL 1 (
        cd ..\..
        echo -------------------------------------------------------------------------------
        echo Processing of the script: %0 - step: 'python src\polynomial\launcher.py -a multiply -m numpy
    )
    cd ..\..
)

if ["%POLYNOMIAL_IS_PYTHON_SIMPLE%"] EQU ["yes"] (
    cd lang\python
    if ["%POLYNOMIAL_CHOICE_SETUP%"] EQU ["yes"] (
        make pipenv
    )
    echo -------------------------------------------------------------------------------
    set PYTHONPATH=src\polynomial
    pipenv run python src\polynomial\launcher.py -a multiply -m simple
    if ERRORLEVEL 1 (
        cd ..\..
        echo -------------------------------------------------------------------------------
        echo Processing of the script: %0 - step: 'python src\polynomial\launcher.py -a multiply -m simple
    )
    cd ..\..
)

echo -------------------------------------------------------------------------------
echo:| TIME
echo -------------------------------------------------------------------------------
echo End   %0
echo ===============================================================================

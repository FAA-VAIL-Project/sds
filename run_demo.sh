#!/bin/bash

set -e

# ----------------------------------------------------------------------------------
#
# run_demo.sh: Demo project polynomial multiplication.
#
# ----------------------------------------------------------------------------------

export POLYNOMIAL_CHOICE_ACTION_DEFAULT=data
export POLYNOMIAL_CHOICE_METHOD_DEFAULT=fft
export POLYNOMIAL_CHOICE_SETUP_DEFAULT=no
export POLYNOMIAL_FILE_NAME=lang/polynom_data.json

rm -f run_demo.log

if [ -z "$1" ]; then
    echo "=============================================================================="
    echo "complete             - All implemented programming languages."
    echo "data                 - Create task data."
    echo "-------------------------------------------------------------------------------"
    echo "c                    - C++"
    echo "python               - Python 3"
    echo "rust                 - Rust"
    echo "------------------------------------------------------------------------------"
    read -rp "Enter the desired action [default: ${POLYNOMIAL_CHOICE_ACTION_DEFAULT}] " POLYNOMIAL_CHOICE_ACTION
    export POLYNOMIAL_CHOICE_ACTION=${POLYNOMIAL_CHOICE_ACTION}

    if [ -z "${POLYNOMIAL_CHOICE_ACTION}" ]; then
        export POLYNOMIAL_CHOICE_ACTION=${POLYNOMIAL_CHOICE_ACTION_DEFAULT}
    fi
else
    export POLYNOMIAL_CHOICE_ACTION=$1
fi

if [ "${POLYNOMIAL_CHOICE_ACTION}" != "data" ]; then
    if [ -z "$2" ]; then
        echo "=============================================================================="
        echo "fft                  - Fast Fourier Transform      - Python"
        echo "numpy                - NumPy                       - Python"
        echo "simple               - Simple multiplication       - Python"
        echo "------------------------------------------------------------------------------"
        read -rp "Enter the desired action [default: ${POLYNOMIAL_CHOICE_METHOD_DEFAULT}] " POLYNOMIAL_CHOICE_METHOD
        export POLYNOMIAL_CHOICE_METHOD=${POLYNOMIAL_CHOICE_METHOD}

        if [ -z "${POLYNOMIAL_CHOICE_METHOD}" ]; then
            export POLYNOMIAL_CHOICE_METHOD=${POLYNOMIAL_CHOICE_METHOD_DEFAULT}
        fi
    else
        export POLYNOMIAL_CHOICE_METHOD=$2
    fi
fi

if [ -z "$3" ]; then
    echo "=============================================================================="
    echo "Setup Environment    - yes / no."
    echo "------------------------------------------------------------------------------"
    read -rp "Enter the desired action [default: ${POLYNOMIAL_CHOICE_SETUP_DEFAULT}] " POLYNOMIAL_CHOICE_SETUP
    export POLYNOMIAL_CHOICE_SETUP=${POLYNOMIAL_CHOICE_SETUP}

    if [ -z "${POLYNOMIAL_CHOICE_SETUP}" ]; then
        export POLYNOMIAL_CHOICE_SETUP=${POLYNOMIAL_CHOICE_SETUP_DEFAULT}
    fi
else
    export POLYNOMIAL_CHOICE_SETUP=$3
fi

export POLYNOMIAL_IS_CPP=false
export POLYNOMIAL_IS_DATA=false
export POLYNOMIAL_IS_PYTHON=false
export POLYNOMIAL_IS_RUST=false

if [ "${POLYNOMIAL_CHOICE_ACTION}" = "complete" ]; then
    export POLYNOMIAL_IS_CPP=true
    export POLYNOMIAL_IS_PYTHON=true
    export POLYNOMIAL_IS_RUST=true
elif [ "${POLYNOMIAL_CHOICE_ACTION}" = "c++" ]; then
    export POLYNOMIAL_IS_CPP=true
elif [ "${POLYNOMIAL_CHOICE_ACTION}" = "data" ]; then
    export POLYNOMIAL_IS_DATA=true
elif [ "${POLYNOMIAL_CHOICE_ACTION}" = "python" ]; then
    export POLYNOMIAL_IS_PYTHON=true
elif [ "${POLYNOMIAL_CHOICE_ACTION}" = "rust" ]; then
    export POLYNOMIAL_IS_RUST=true
fi

echo ""
echo "Script $0 is now running"

export LOG_FILE=run_demo.log

echo ""
echo "You can find the run log in the file $LOG_FILE"
echo ""

exec &> >(tee -i $LOG_FILE) 2>&1
sleep .1

echo "=============================================================================="
echo "Start $0"
echo "------------------------------------------------------------------------------"
echo "Polynomial Multiplication."
echo "------------------------------------------------------------------------------"
echo "CHOICE_ACTION        : ${POLYNOMIAL_CHOICE_ACTION}"
if [ "${POLYNOMIAL_IS_DATA}" != "true" ]; then
    echo "SETUP_METHOD         : ${POLYNOMIAL_CHOICE_METHOD}"
fi
if [ "${POLYNOMIAL_IS_DATA}" = "true" ]; then
    echo "SETUP_ENVIRONMENT    : ${POLYNOMIAL_CHOICE_SETUP}"
fi
echo "------------------------------------------------------------------------------"
echo "C++                  : ${POLYNOMIAL_IS_CPP}"
echo "Data                 : ${POLYNOMIAL_IS_DATA}"
echo "Python               : ${POLYNOMIAL_IS_PYTHON}"
echo "Rust                 : ${POLYNOMIAL_IS_RUST}"
echo "------------------------------------------------------------------------------"
date +"DATE TIME : %d.%m.%Y %H:%M:%S"
echo "=============================================================================="

if [ "${POLYNOMIAL_IS_DATA}" = "true" ]; then
    cd lang/python
    if [ "${POLYNOMIAL_CHOICE_SETUP}" = "true" ]; then
        make -f lang/python\Makefile pipenv
    fi
    echo -------------------------------------------------------------------------------
    export PYTHONPATH=lang\python\src\polynomial
    if ! { pipenv run python lang\python\src\launcher.py -a generate; }; then
        exit 255
    fi
    cd ../..
fi

if [ "${POLYNOMIAL_IS_PYTHON}" = "true" ]; then
    cd lang/python
    if [ "${POLYNOMIAL_CHOICE_SETUP}" = "true" ]; then
        make -f lang/python\Makefile pipenv
    fi
    echo -------------------------------------------------------------------------------
    export PYTHONPATH=lang\python\src\polynomial
    if ! { pipenv run python lang\python\src\launcher.py -a multiply - m ${POLYNOMIAL_CHOICE_METHOD}; }; then
        exit 255
    fi
    cd ../..
fi

echo ""
echo "------------------------------------------------------------------------------"
date +"DATE TIME : %d.%m.%Y %H:%M:%S"
echo "------------------------------------------------------------------------------"
echo "End   $0"
echo "=============================================================================="

# SDS - Python - Implementation Example

The Python implementation example is located in the file directory **`lang/python`**.

Three different computational methods for polynomial multiplication are provided:

1. **fft**: Fast Fourier transform,
2. **numpy**:  **`numpy.polynomial`** package,
3. **simple**: simple multiplication of all monomials.

For Python, the **`run_demo`** script supports the following processing variants:

| Action          | Method | Setup    | Remark                            |
|-----------------|--------|----------|-----------------------------------|
| complete        |        | yes / no | data & fft & numpy & simple & ... |
| complete_python |        | yes / no | data & fft & numpy & simple       |
| data            |        | yes / no |                                   |
| python          | fft    | yes / no |                                   |
| python          | numpy  | yes / no |                                   |
| python          | simple | yes / no |                                   |

The setup parameter controls the creation of a virtual environment.
# sds - Polynomial Multiplication

For each of the programming languages used in the FAA-VAIL project, the required standards are demonstrated in an implementation example based on the following specification.   
The implemented examples can be found in the file directory **`lang`**.

## 1. Task

Multiply two polynomials of any degree with integer coefficients using a `Fast Fourier Transform.

## 2. Mathematical background

A **monomial** is an expression of the type **ax<sup>n</sup>**, where **a** is a real number constant - called a **coefficient** - and **n** is a nonnegative integer - called the **degree**.

A **polynomial** is a monomial or a combination of sums and / or differences of monomials.

When monomials have the same degree we say that they are **like terms**. 
Polynomials can be simplified by collecting and combining like terms.

A polynomial is arranged in **descending order** if the largest degree is first.

The **degree of a polynomial** is the largest of the degrees of the monomials unless it is the polynomial 0.

To find an equivalent expression for the **product of two monomials**, multiply the coefficients and add the degrees based on the product rule for exponents.

To **multiply two polynomials** `P` and `Q` select one of the polynomials - say `P`. 
Then multiply each monomial of `P` by every monomial of `Q` and collect the like terms.

## 3. Fast Fourier Transform (FFT)

A FFT is an algorithm that computes the discrete Fourier transform of a sequence, or its inverse.
For a more detailed discussion, see Wikipedia at [Fast Fourier transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform){:target="_blank"}. 

The following contributions in YouTube illustrate the thoughts behind FFT very clearly:

- [But what is the Fourier Transform? A visual introduction.](https://www.youtube.com/watch?v=spUNpyF58BY){:target="_blank"}
- [The Fast Fourier Transform (FFT): Most Ingenious Algorithm Ever?](https://www.youtube.com/watch?v=h7apO7q16V0){:target="_blank"}
- [FFT Example: Unraveling the Recursion](https://www.youtube.com/watch?v=Ty0JcR6Dvis){:target="_blank"}

Detailed descriptions of the implementation of an FFT can be found in the following two books:

- **Cormen, T. H. et al. (2009) Introduction to Algorithms, 3rd edn. Camebridge, Ma, The MIT Press**.

    Particularly interesting: Chapter 30 - Polynomials and the FFT. pp. 898-925.

- **Kong, Q. et al. (2021) Python Programming and Numerical Methods: A Guide for Engineers and Scientists. London, Academic Press**.

    Particularly interesting: Chapter 24 - Fourier Transform. pp. 415-444.

## 4. Detailed Requirements

a) The FFT algorithm must be implemented in its own source code and not via prefabricated libraries.

b) The polynomials to be multiplied and the resulting product are available in the JSON file **`lang/polynom_data.json`**:

    {
        "moTasks": 9,
        "tasks": [
            {
                "taskNo": 9,
                "polynom1": {
                    "degree": 9,
                    "coefficients": [
                        9,
                        ...,
                    ]
                },
                "polynom2": {
                    "degree": 9,
                    "coefficients": [
                        9,
                        ...,
                    ]
                },
                "product": {
                    "degree": 9,
                    "coefficients": [
                        9,
                        ...,
                    ]
                }
            },
            ...


c) The coefficients are given in ascending order, that is coefficients go from degree zero upward. 

d) The required CPU time must be determined as accurately as possible, i.e. the time measurement always starts first and is measured in the smallest available time unit. 

e) The time measurement for a polynomial multiplication must include the required time for the verification of the computed product. 

f) At the end of the processing a statistic must be displayed as follows (**`degrees: polynomial1 - polynomial2 - product`**):

     3,946,000,300 ns - Total time task no.  1 (degrees:  5114 -  4807 -  9921) executed.
     3,998,500,500 ns - Total time task no.  2 (degrees:  4859 -  5136 -  9995) executed.
     4,032,999,500 ns - Total time task no.  3 (degrees:  5091 -  4888 -  9979) executed.
     4,092,500,700 ns - Total time task no.  4 (degrees:  5003 -  5032 - 10035) executed.
     3,955,000,000 ns - Total time task no.  5 (degrees:  5010 -  4947 -  9957) executed.
     3,959,000,000 ns - Total time task no.  6 (degrees:  5089 -  4820 -  9909) executed.
     4,078,498,900 ns - Total time task no.  7 (degrees:  4844 -  5189 - 10033) executed.
     4,088,999,900 ns - Total time task no.  8 (degrees:  4980 -  5098 - 10078) executed.
     4,090,001,700 ns - Total time task no.  9 (degrees:  5050 -  4979 - 10029) executed.
     3,960,999,100 ns - Total time task no. 10 (degrees:  4879 -  5026 -  9905) executed.
    40,224,500,900 ns - Total time Python.

g) The execution of the programming specific solution must be done via the **`run_demo`** script.

## 5. Task Generation

The generation of polynomial multiplication tasks is part of the Python implementation.
For this purpose the script **`run_demo`** with the parameter **`data`** can be used.
The parameters for the generation are stored as configuration parameters and can be modified via the file **`lang/python/setup.cfg`** in the **`polynomial`** section.
The possible parameters and their default values are as follows:

| Parameter  | Default | Remarks                     |
|------------|---------|-----------------------------|
| coef_max   | 9999    | largest coeefficient        |
| coef_min   | -9999   | smallest coeefficient       |
| degree_max | 5200    | largest degree              |
| degree_min | 4800    | smallest degree             |
| no_tasks   | 10      | number of tasks to generate |
| verbose    | true    | display progress messages   |

The coefficients of the monomials and the degrees of the polynomials are determined randomly in the given intervals.

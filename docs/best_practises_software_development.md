# sds - Programming Language Independent Standards

Here are all the cross-programming language standards and best practices to be followed in software development for the FAA-VAIL project.

## 1. Documentation

- the documentation in the repository is usually created using the GitHub variant of Markdown - [see here](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax){:target="_blank"}

- the top directory of a repository generally contains the following documentation files:
  - **LICENSE** - the legal instrument governing the use or redistribution of the software
  - **README.md** - typically includes information on:
    - What the project does
    - Why the project is useful
    - How users can get started with the project
    - Where users can get help with the project
    - Who maintains and contributes to the project

- all subdirectories must contain a file called **README**.md, which briefly describes what is contained in this directory
 
- the rest of the project documentation files are located in the `docs` subdirectory
  - **code_of_conduct.md** - defines standards for how to engage in the project
  - **contributing.md** - guidelines to communicate how people should contribute to the project
  - **index.md** - home page of the more detailed project description
  - **license.md** - the same 
 
- the project documentation is created with the tool [MkDocs](https://www.mkdocs.org){:target="_blank"}:  `make [-f MakefileOrig] docs`

## 2. Git & GitHub


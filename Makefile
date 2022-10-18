.DEFAULT_GOAL := help

ifeq ($(OS),Windows_NT)
	export DEMONSTRATION_PYTHON=copy /Y lang\\python\\docs\\index.md docs\\implementation_python.md
	export PIPENV=python -m pipenv
	export PYTHON=python
else
	export DEMONSTRATION_PYTHON=cp -i lang/python/docs/index.md docs/implementation_python.md
	export PIPENV=python3 -m pipenv
	export PYTHON=python3
endif

##                                                                            .
## ============================================================================
## sds - Software Development Standards.
##       ---------------------------------------------------------------
##       The purpose of this Makefile is to support the software
##       development process for sds.
##       ---------------------------------------------------------------
##       The available make commands are:
## ----------------------------------------------------------------------------
## help:               Show this help.
## docs:               Create and upload the user documentation with MkDocs.
## ----------------------------------------------------------------------------

docs: mkdocs
help:
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

# Project documentation with Markdown.
# https://github.com/mkdocs/mkdocs/
# Configuration file: none
mkdocs:
	@echo "Info **********  Start: MkDocs **************************************"
	${PYTHON} -m pip install --upgrade pip
	${PYTHON} -m pip install --upgrade pipenv
	${PYTHON} -m pipenv install --dev
	${PYTHON} -m pipenv update --dev
	${PIPENV} run pip freeze
	@echo ---------------------------------------------------------------------
	@echo PYTHON    =${PYTHON}
	${PIPENV} run mkdocs --version
	@echo ---------------------------------------------------------------------
	${DEMONSTRATION_PYTHON}
	${PIPENV} run mkdocs gh-deploy --force
	@echo "Info **********  End:   MkDocs **************************************"

## ============================================================================

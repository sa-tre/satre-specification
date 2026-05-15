# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile cleanall check-satrecsv

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# satrecsv is written to build/satrecsv and not READTHEDOCS_OUTPUT
# because it's run by us in build.jobs.pre_build, not by readthedocs
satrecsv:
	mkdir -p build/satrecsv
	python3 scripts/satrecsv.py --output-dir build/satrecsv --input-file source/spec/specification.yaml

satrecsv-copy: satrecsv
	mkdir -p generated
	cp -f build/satrecsv/satre.xlsx build/satrecsv/satre.csv generated/

html: Makefile satrecsv-copy
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# If READTHEDOCS_OUTPUT is not set default to build
OUTPUT_DIR := $(if $(READTHEDOCS_OUTPUT),$(READTHEDOCS_OUTPUT),build)
# satre.xls is excluded from linkcheck, so check that it was copied to build/html
check-satrecsv:
	@FILE="$(OUTPUT_DIR)/html/satre.xlsx"; \
	if [ ! -f "$$FILE" ]; then \
		echo "ERROR: $$FILE does not exist"; \
		exit 1; \
	fi; \
	SIZE=$$(stat -f %z "$$FILE"); \
	if [ "$$SIZE" -lt 10000 ]; then \
		echo "ERROR: $$FILE is too small ($$SIZE bytes)"; \
		exit 1; \
	fi

clean-all: clean
	rm -f generated/*

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
satrecsv-copy: satrecsv
	cp -f build/satrecsv/satre.xlsx generated/

html: Makefile satrecsv-copy
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# If READTHEDOCS_OUTPUT is not set default to build
OUTPUT_DIR := $(if $(READTHEDOCS_OUTPUT),$(READTHEDOCS_OUTPUT),build)
# satre.xls is excluded from linkcheck, so check that it was copied to build/html
check-satrecsv:
	if [ ! -f "$(OUTPUT_DIR)/html/satre.xlsx" ]; then echo "ERROR: $(OUTPUT_DIR)/html/satre.xlsx not found"; exit 1; fi

clean-all: clean
	rm -f generated/*

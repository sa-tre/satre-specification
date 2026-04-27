# 1. Force the default goal to be 'help' (from the parent)
.DEFAULT_GOAL := help

# 2. Set your specific paths
SOURCEDIR = ./source
BUILDDIR  = ../_build

# 3. Prevent the catch-all loop
Makefile: ;
../Makefile: ;

# 4. Include the logic from the parent
include ../Makefile

# The Specification Document

The specification document is built using [Sphinx](https://www.sphinx-doc.org/) from Markdown files through [MyST](https://myst-parser.readthedocs.io/).

## Building the Specification Document

Building the document requires Python 3.

Clone this repository

```console
$ git clone https://github.com/sa-tre/satre-specification
```

Change to the `docs` directory

```console
$ cd docs
```

Create a virtual environment to hold the Python dependencies

```console
$ python3 -m venv ./venv
$ source ./venv/bin/activate
```

Install the python dependencies (specified in [`requirements.txt`](./requirements.txt)

```console
$ pip install -r requirements.txt
```

Use the [`Makefile`](./Makefile) to build the document site

```console
$ make html
```

The generated documents will be placed under `build/html/`.
To view the documents open `build/html/index.html` in your browser.
For example

```console
$ firefox build/html/index.html
```

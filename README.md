# bbc

## Synopsis

`bbc` is a tiny utility that checks some basic properties of you bibtex
files, orders the entries in an alphabetical order and style them in a uniform
way.

## Usage

```bash
./bbc.py <bib_file> --output=<out_file>
```

The formated bibtex is printed in the `<out_file>` file, while error messages on the standard error output.

Add the flag `--add-todo` to assign a `TODO` value to missing fields which are required for the particular types of entries:

```bash
./bbc.py <bib_file> --output=<out_file> --add-todo
```

If you toggle option `--try-fix`, it will try to find missing ISSN and other
informations about journals (from [DBpedia](http://wiki.dbpedia.org/)) or ISBN
and other information for books (from [Google Books](books.google.com)).

## Prerequisities

All prerequisities are listed in the `requirements.txt` file.

- [`bibtexparser`](https://github.com/sciunto-org/python-bibtexparser) to parse and print bibtex
- [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/) to scrape web pages
- [`libisbn`](https://github.com/xlcnd/isbnlib) to work ISBNs and Google Books
- [`SPARQLWrapper`](https://github.com/RDFLib/sparqlwrapper) to query DBpedia
- [`termcolor`](https://pypi.python.org/pypi/termcolor) to have colored error messages
- [`pycountry`](https://pypi.org/project/pycountry/) to query countries

## License

The software is distributed under the [BSD
License](https://opensource.org/licenses/BSD-3-Clause).

## Acknowledgments

This project is based on [prettybib](https://github.com/jlibovicky/prettybib).

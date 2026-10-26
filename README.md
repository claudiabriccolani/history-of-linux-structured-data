# History of Linux: a LODLAM project

Project for the course **Information Science and Cultural Heritage**, a.y. 2025-2026.

**Author:** [Your name]

**Source:** [History of Linux](https://en.wikipedia.org/wiki/History_of_Linux), English Wikipedia.

## Repository structure

- `index.html` and `css/` hold the project report, published as the GitHub Pages home.
- `img/` holds the theoretical and conceptual model diagrams.
- `tei/` holds the TEI P5 encoding of the source text, and `xslt/` the stylesheet that turns it into HTML.
- `scripts/` holds the Python script that extracts RDF from the TEI file.
- `html/` and `rdf/` hold the generated outputs: the HTML edition and the Turtle dataset.

## Usage (to be completed)

```
pip install -r scripts/requirements.txt
python scripts/tei2rdf.py
```

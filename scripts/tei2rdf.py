"""Convert the TEI encoding of "History of Linux" into an RDF dataset.

This script will read tei/history_of_linux.xml, extract the encoded
entities (people, organisations, places, software, events, dates) and
their relations, and serialise them as Turtle in rdf/dataset.ttl.

For now it only parses the TEI file and prints a TODO message; it does
not write any output yet.

Usage (from the repository root):
    python scripts/tei2rdf.py
"""

from pathlib import Path

from lxml import etree

ROOT = Path(__file__).resolve().parent.parent
TEI_FILE = ROOT / "tei" / "history_of_linux.xml"
RDF_FILE = ROOT / "rdf" / "dataset.ttl"

TEI_NS = {"tei": "http://www.tei-c.org/ns/1.0"}


def main():
    tree = etree.parse(str(TEI_FILE))
    title = tree.findtext(".//tei:titleStmt/tei:title", namespaces=TEI_NS)
    print(f"Parsed {TEI_FILE.relative_to(ROOT)} (title: {title})")
    print(f"TODO: extract entities and write RDF to {RDF_FILE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

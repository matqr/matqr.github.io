import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
import yaml
from pathlib import Path


def parse_authors(author_field):
    """
    Convert BibTeX author field to a YAML-friendly list
    """
    authors = []
    for author in author_field.replace("\n", " ").split(" and "):
        author = author.strip()
        if "," in author:
            last, first = author.split(",", 1)
            authors.append(f"{first.strip()} {last.strip()}")
        else:
            authors.append(author)
    return authors


def bib_to_yaml(bib_path, output_path):
    parser = BibTexParser(common_strings=True)
    parser.customization = convert_to_unicode

    with open(bib_path) as bib_file:
        bib_db = bibtexparser.load(bib_file, parser=parser)

    publications = []

    for entry in bib_db.entries:
        pub = {}

        pub["title"] = entry.get("title", "").strip("{}")
        pub["authors"] = parse_authors(entry.get("author", ""))

        # Journal / venue
        pub["conference"] = entry.get(
            "journal",
            entry.get("booktitle", "")
        )

        # Year
        if "year" in entry:
            pub["year"] = int(entry["year"])

        # Optional links
        if "url" in entry:
            pub["page"] = entry["url"]

        if "doi" in entry:
            pub["page"] = f"https://doi.org/{entry['doi']}"

        if "pdf" in entry:
            pub["pdf"] = entry["pdf"]

        if "code" in entry:
            pub["code"] = entry["code"]

        # BibTeX link (self-reference or external)
        pub["bibtex"] = entry.get("bibtex_url", "")

        # Forced type
        pub["type"] = "journal"
        # pub["type"] = "conference"
        # pub["type"] = "preprint"
        #
        publications.append(pub)

    with open(output_path, "w") as f:
        yaml.dump(
            publications,
            f,
            allow_unicode=True,
            sort_keys=False,
            width=1000,
        )


if __name__ == "__main__":
    bib_file = Path("bib/Journals.bib")
    output_file = Path("publications.yml")

    bib_to_yaml(bib_file, output_file)
    print(f"Saved {output_file}")

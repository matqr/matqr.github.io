import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
import yaml
from pathlib import Path

# CONFIG
YOUR_NAME = "Matias Quintana"
FORCED_TYPE = "journal"


def parse_authors(author_field):
    """
    Convert BibTeX authors into a list of strings, bolding YOUR_NAME.
    Handles "Last, First" -> "First Last" conversion.
    """
    authors = []
    for author in author_field.replace("\n", " ").split(" and "):
        author = author.strip()
        # Convert "Last, First" to "First Last"
        if "," in author:
            last, first = author.split(",", 1)
            name = f"{first.strip()} {last.strip()}"
        else:
            name = author
        # Bold YOUR_NAME exactly
        if name.strip().lower() == YOUR_NAME.lower():
            name = f"<strong>{name.strip()}</strong>"
        authors.append(name)
    return authors


def bib_to_yaml(bib_path, output_path):
    parser = BibTexParser(common_strings=True)
    parser.customization = convert_to_unicode

    with open(bib_path, encoding="utf-8") as bib_file:
        bib_db = bibtexparser.load(bib_file, parser=parser)

    publications = []

    for entry in bib_db.entries:
        if "year" not in entry:
            continue

        pub = {}
        pub["title"] = entry.get("title", "").strip("{}")
        pub["authors"] = parse_authors(entry.get("author", ""))
        pub["conference"] = entry.get("journal", entry.get("booktitle", ""))
        pub["year"] = int(entry["year"])
        pub["type"] = FORCED_TYPE

        # Highlight if YOUR_NAME is first author
        first_author = entry.get("author", "").split(" and ")[0].strip()
        pub["highlight"] = first_author.lower() == YOUR_NAME.lower()

        # Links
        if "url" in entry:
            pub["url"] = entry["url"]
        elif "doi" in entry:
            pub["url"] = f"https://doi.org/{entry['doi']}"

        if "pdf" in entry:
            pub["pdf"] = entry["pdf"]
        if "code" in entry:
            pub["code"] = entry["code"]
        if "bibtex_url" in entry:
            pub["bibtex"] = entry["bibtex_url"]

        publications.append(pub)

    # Sort by year descending
    publications = sorted(publications, key=lambda x: x["year"], reverse=True)

    # Write YAML
    with open(output_path, "w", encoding="utf-8") as f:
        yaml.dump(publications, f, allow_unicode=True,
                  sort_keys=False, width=1000)

    print(f"Saved {output_path}")


if __name__ == "__main__":
    bib_to_yaml(Path("bib/Journals.bib"), Path("_data/publications.yml"))

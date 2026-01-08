import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import convert_to_unicode
import yaml
from pathlib import Path

# =========================
# CONFIG
# =========================
YOUR_NAME = "Matias Quintana"
FORCED_TYPE = "journal"
HIGHLIGHT_IF_FIRST_AUTHOR = True

# =========================
# HELPERS
# =========================


def normalize_name(name):
    return " ".join(name.lower().replace(",", "").split())


def bold_if_self(name):
    if normalize_name(name) == normalize_name(YOUR_NAME):
        return f"<strong>{name}</strong>"
    return name


def parse_authors(author_field):
    authors = []
    for author in author_field.replace("\n", " ").split(" and "):
        author = author.strip()
        if "," in author:
            last, first = author.split(",", 1)
            name = f"{first.strip()} {last.strip()}"
        else:
            name = author
        authors.append(bold_if_self(name))
    return authors


def should_highlight(authors):
    if not HIGHLIGHT_IF_FIRST_AUTHOR or not authors:
        return False
    first = authors[0].replace("<strong>", "").replace("</strong>", "")
    return normalize_name(first) == normalize_name(YOUR_NAME)

# =========================
# MAIN
# =========================


def bib_to_yaml(bib_path, output_path):
    parser = BibTexParser(common_strings=True)
    parser.customization = convert_to_unicode

    with open(bib_path) as bib_file:
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

        # URL (link for title)
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

        if should_highlight(pub["authors"]):
            pub["highlight"] = True

        publications.append(pub)

    # Sort by year descending
    publications = sorted(publications, key=lambda x: x["year"], reverse=True)

    with open(output_path, "w") as f:
        yaml.dump(
            publications,
            f,
            allow_unicode=True,
            sort_keys=False,
            width=1000,
        )

    print(f"Saved {output_path}")


if __name__ == "__main__":
    bib_to_yaml(Path("bib/Journals.bib"), Path("_data/publications.yml"))

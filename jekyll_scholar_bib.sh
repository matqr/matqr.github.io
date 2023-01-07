#! /bin/bash

# all publications
bibble bib/Conferences.bib bib/conferences.tmpl > _pages/pubs_conferences.html
bibble bib/Journals.bib bib/journals.tmpl > _pages/pubs_journals.html
bibble bib/Preprints.bib bib/theses_arxiv.tmpl > _pages/pubs_theses_arxiv.html
# insert the appropiate header into the original html and make it a markdown file

cat _layouts/publications_header.txt _pages/pubs_conferences.html _pages/pubs_journals.html _pages/pubs_theses_arxiv.html > temp && mv temp _pages/publications.md
# bold author name on final file (OS X needs sed -i '', ubuntu needs sed -i)

sed -i '' 's+Matias Quintana+<strong>Matias Quintana</strong>+g' _pages/publications.md

# Fix for Mario's name, replace  {\'{e}}
sed -i "" "s+{\\'{e}}+AA+g" _pages/publications.md

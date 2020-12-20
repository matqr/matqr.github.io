#! /bin/bash

bibble bib/Publications.bib bib/publications.tmpl > _pages/pubs.html 
# insert the appropiate header into the original html and make it a markdown file
cat ~/Dropbox/MendeleyBibTeX/publications_header.txt _pages/pubs.html > temp && mv temp _pages/publications.md
# TODO: insert one blank line before appending the files
# bold author name on final file (OS X needs sed -i '', ubuntu needs sed -i)
sed -i '' 's+Matias Quintana+<strong>Matias Quintana</strong>+g' _pages/publications.md

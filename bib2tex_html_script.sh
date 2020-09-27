#! /bin/bash

clear
# generate the bibliography from bibtex into an html file. File location depends on folder structure
bibtex2html --revkeys --sort-by-date -r --no-abstract --no-keywords -o _pages/publications ~/Dropbox/MendeleyBibTeX/Publications.bib
# get rid of the first line of the html file
tail -n +2 "_pages/publications.html" > "_pages/publications.tmp" && mv "_pages/publications.tmp" "_pages/publications.html"
# insert the appropiate header into the original html and make it a markdown file
cat ~/Dropbox/MendeleyBibTeX/publications_header.txt _pages/publications.html > temp && mv temp _pages/publications.md
# remove the extra files that got generated
rm _pages/publications.html
# bold author name on final file (OS X needs sed -i '', ubuntu needs sed -i)
sed -i '' 's+Matias Quintana+<strong>Matias Quintana</strong>+g' _pages/publications.md
# update link of bib links and move to correct folder
sed -i '' 's+_pages/publications_bib.html+publications_bib/+g' _pages/publications.md
mv _pages/publications_bib.html _site/publications/publications_bib.html

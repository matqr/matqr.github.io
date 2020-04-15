#! /bin/bash

clear
# generate the bibliography from bibtex into an html file. File location depend on folder structure
bibtex2html --revkeys --sort-by-date -r --no-abstract --no-keywords -o _pages/publications ~/Dropbox/MendeleyBibTeX/Publications.bib
# get rid of the first line of the html file
tail -n +2 "_pages/publications.html" > "_pages/publications.tmp" && mv "_pages/publications.tmp" "_pages/publications.html"
# insert the appropiate header into the original html and make it a markdown file
cat ~/Dropbox/MendeleyBibTeX/publications_header.txt _pages/publications.html > temp && mv temp _pages/publications.md
# remove the extra files that got generated
rm _pages/publications_bib.html _pages/publications.html
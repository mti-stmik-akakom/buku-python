pdf:
	pandoc --pdf-engine=xelatex -o hasil/pemrograman-python.pdf --toc --from markdown --template eisvogel --listings --top-level-division=chapter isi/*

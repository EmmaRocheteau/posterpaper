from doc_parse import *
import ranking


src = "paper2/2015mt-its.tex"
# Create object model of the document
doc = Document(src)
# Decide which sections and figures to include in the poster
ranking.rankFigures(doc)
ranking.rankSections(doc)
# Decide the layout of the poster

# Summarise some of the sections if needed

# Generate Poster to ./poster.tex
#generatePoster(doc)

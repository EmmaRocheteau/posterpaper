from doc_parse import *
import ranking
from generate_latex import *
from poster_layout import *
import summarise

src = "paper2/2015mt-its.tex"
# Create object model of the document
doc = Document(src)

# Decide which sections and figures to include in the poster
ranking.rankFigures(doc)
ranking.rankSections(doc)

# Decide the layout of the poster
poster = Poster(doc)

# Summarise sections such that each column height is ~632
DESIRED_HEIGHT = 632
for i, col in enumerate(poster.columns):
    col_fig_size = 0
    for box in col.boxes:
        col_fig_size += box.size_without_text
    text_reduction_percent = ((DESIRED_HEIGHT - col_fig_size)/col.column_size)*100
    for j, box in enumerate(col.boxes):
        shortened_content = summarise.summarise(box.content, box.title, int(text_reduction_percent))
        print(shortened_content['text'])
        poster.columns[i].boxes[j].content = shortened_content['text']

# Generate Poster to poster.tex
generate_latex(poster, 'paper2/poster.tex')


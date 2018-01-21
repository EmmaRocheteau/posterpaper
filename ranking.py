from doc_parse import *

DESIRED_NUM_FIGURES = 3

def rankFigures(doc):
    # Count the number of refernces to each figure
    labels = []
    for i, sec in enumerate(doc.sections):
        for j, fig in enumerate(sec.figures):
            labels.append([(i, j), fig.label])
    for lab in labels:
        ref = "\\ref{" + lab[1] + "}"
        for i, sec in enumerate(doc.sections):
            doc.sections[lab[0][0]].figures[lab[0][1]].ref_count += sec.content.count(ref)
            for j, subsec in enumerate(sec.subsections):
                doc.sections[lab[0][0]].figures[lab[0][1]].ref_count += subsec.content.count(ref)
    # Look through the figures and determine the relative importance of each one.
    measures = []
    for i, sec in enumerate(doc.sections):
        for j, fig in enumerate(sec.figures):
            measures.append([(i, j), fig.label, fig.ref_count, fig.char_count])
    # Process the measures
    max_count = 0
    max_chars = 0
    for measure in measures:
        if measure[2] > max_count:
            max_count = measure[2]
        if measure[3] > max_chars:
            max_chars = measure[3]
    results = []
    for measure in measures:
        result = (measure[2]/max_count) + (measure[3]/max_chars)
        results.append([measure[0], measure[1], result])
    # Find the top 3
    results.sort(key=lambda x: x[2], reverse=True)
    if len(results) > 3:
        losers = results[3:]
        for loser in losers:
            doc.sections[loser[0][0]].figures[loser[0][1]].include = False
            print(loser[1] + " excluded")
            # We want to delete any sentences with reference to this figure
            ref = "\\ref{" + loser[1] + "}"
            for i, sec in enumerate(doc.sections):
                while doc.sections[i].content.count(ref) > 0:
                    start = sec.content.find(ref)
                    end = start + len(ref)
                    sentence_end = sec.content.find(".", end)
                    sentence_start = sec.content.rfind(".", 0, start)
                    doc.sections[i].content = doc.sections[i].content[0:sentence_start] + doc.sections[i].content[sentence_end:]
                for j, subsec in enumerate(sec.subsections):
                    while doc.sections[i].subsections[j].content.count(ref) > 0:
                        start = subsec.content.find(ref)
                        end = start + len(ref)
                        sentence_end = subsec.content.find(".", end)
                        sentence_start = subsec.content.rfind(".", 0, start)
                        doc.sections[i].subsections[j].content = doc.sections[i].subsections[j].content[0:sentence_start] + \
                                                                 doc.sections[i].subsection[j].content[sentence_end:]
    return


def rankSections(doc):
    for i, sec in enumerate(doc.sections):
        # Approximately what percentage of the total document is made up by this section
        perc = sec.char_count/doc.total_char_count
        if perc < 0.1:
            doc.sections[i].include = False
    return
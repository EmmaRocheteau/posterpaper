from doc_parse import *

from aylienapiclient import textapi

f = open("key")
key = f.readline()
key = key.strip()
f.close()

f = open("app_id")
app_id = f.readline()
app_id = key.strip()
f.close()

client = textapi.Client(app_id, key)

sentiment = client.Sentiment({'text': 'John is a very good football player!'})

test_doc = Document("")
test_doc.abstract = "Nowadays, universities and companies have a huge need for simulation and modelling methodologies. In the particular case of traffic and transportation, making physical modifications to the real traffic networks could be highly expensive, dependent on political decisions and could be highly disruptive to the environment." + \
"However, while studying a specific domain or problem, analysing a problem through simulation may not be trivial and may need several simulation tools, hence raising interoperability issues." + \
"To overcome these problems, we propose an agent-directed transportation simulation platform, through the cloud, by means of services. We intend to use the IEEE standard HLA (High Level Architecture) for simulators interoperability and agents for controlling and coordination. Our motivations are to allow multiresolution analysis of complex domains, to allow experts to collaborate on the analysis of a common problem and to allow co-simulation and synergy of different application domains." + \
"This paper will start by presenting some preliminary background concepts to help better understand the scope of this work. After that, the results of a literature review is shown. Finally, the general architecture of a transportation simulation platform is proposed."
test_doc.authors = "Tiago Azevedo, Rosaldo J. F. Rossetti, Jorge G. Barbosa\\\\" + \
    "Artificial Intelligence and Computer Science Lab\\\\" + \
    "Department of Informatics Engineering\\\\" + \
    "Faculty of Engineering, University of Porto, Portugal\\\\"
test_doc.title = ""

sections = []
sec1 = Section("")
sec1.content = ""
sec1.name = ""
sec1.subsections.append()

def summarise(test_doc.abstract):
    summary = client.Summarize({'url': url, 'sentences_number': 3})
    for sentence in summary['sentences']:
        print
        sentence
    tex = ""
    return tex
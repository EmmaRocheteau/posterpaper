abstract_100 = client.summarize({'title': 'Abstract', 'text': doc.abstract, 'sentences_number': 6})
f.write("}\n\n\headerbox{Abstract}{name=section0,span=1,column=0,row=0}\n{")
f.write(abstract_100)
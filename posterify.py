from summarise import summarise

#Code to decide how many sections to include and how to arrange them
#For sections other than the abstract and last section
#If section is less than 10% of the total content get rid of it from the section list
#Ideal poster length: 700 words or ~4750 characters (lets say 4000 minus the abstract), ideal length for abstract 100 words/750 characters/6 sentences. Shorten the other sections by a factor of totalchar_count/4000
#Calculate what the section length would be with and without it's figure. If number of images is 4 or less, keep all images. Try all combinations untill best is found
#If number of images is more than 4 then try different combinations

abstract_100 = client.summarize({'title': 'Abstract', 'text': doc.abstract, 'sentences_number': 6})
f.write("}\n\n\headerbox{Abstract}{name=section0,span=1,column=0,row=0}\n{")
f.write(abstract_100)

#Create variable called aspect which equals the height of the columns with respect to the width

#Work out what the reduced approximate character count would be if the sections were kept
for i in range(len(doc.sections)):
    ratio = doc.sections[i].char_count / doc.total_char_count
    if ratio < 0.1 and i !=number_of_sections: #We always want to keep the conclusion otherwise the poster appears unfinished!
        doc.sections[i].include = False #The default flag is True

#Calculate an approximation for the reduced_char_counts after summarising
new_total_char_count = sum(section.char_count for section in doc.sections if section.include is True)

#Calculate estimates on new character counts
section.reduced_char_count = section.char_count/new_total_char_count for section in doc.sections if section.include is True

#Work out an amount of space relative to the abstract + it's image space


for i in range(len(doc.sections)):
    #Section start
    if i == 0:
        f.write("}\n\n\headerbox{Abstract}{name=section0,span=1,column=0,row=0}\n{")
    else:
        f.write("}\n\n\headerbox{" + doc.sections[i].name + "}{name=section" + str(i) + ",column=0,span=1,below=section" + str(i-1) + "}\n{")
    #Summarise section1



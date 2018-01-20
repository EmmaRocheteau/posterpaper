from summarise import summarise

title = "A State-of-the-art Integrated Transportation Simulation Platform"
imagefile = "eyecatcher.png"
authors = "Emma Rocheteau$^{1,2}$\\\\[-0.5em]\n \t{\small $^1$School of Clinical Medicine, University of Cambridge}\\\\[-0.5em]\n \t{\small {\\tt ecr38@cam.ac.uk}"
abstract = "Nowadays, universities and companies have a huge need for simulation and modelling methodologies. In the particular case of traffic and transportation, making physical modifications to the real traffic networks could be highly expensive, dependent on political decisions and could be highly disruptive to the environment. " + \
"However, while studying a specific domain or problem, analysing a problem through simulation may not be trivial and may need several simulation tools, hence raising interoperability issues. " + \
"To overcome these problems, we propose an agent-directed transportation simulation platform, through the cloud, by means of services. We intend to use the IEEE standard HLA (High Level Architecture) for simulators interoperability and agents for controlling and coordination. Our motivations are to allow multiresolution analysis of complex domains, to allow experts to collaborate on the analysis of a common problem and to allow co-simulation and synergy of different application domains. " + \
"This paper will start by presenting some preliminary background concepts to help better understand the scope of this work. After that, the results of a literature review is shown. Finally, the general architecture of a transportation simulation platform is proposed. "


f = open('poster_tex.txt','w+')
g = open('poster_preamble.txt', 'r')
h = open('logos.txt', 'r')

#Insert preamble
f.write(g.read())

#Insert title
f.write(title)

#Tex bable
f.write("} \n %%% Authors %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n { \n \\vspace{0.4em} \n \t{\n \t")

#Insert authors
f.write(authors)

#Insert logos text, can be edited in the text file
f.write(h.read())

#Add the headerbox tex stuff
f.write("\headerbox{Abstract}{name=abstract,span=1,column=0,row=0}\n{")

#Summarise the abstract to a given percentage of the length of the original text
f.write(summarise(abstract, title, 60))

#Code to decide how many sections to include and how to arrange them
#For sections other than the abstract and last section
#If section is less than 10% of the total content get rid of it
#Ideal poster length: 700 words or 4750 characters, ideal length for abstract 100 words or 670 characters. Shorten the other sections by 4750/totalchar_count
#Calculate what the section length would be with and without it's figure. If number of images is 4 or less, keep all images. Try all combinations untill best is found
#If number of images is more than 4 then try different combinations
abstract_100 = summarise(abstract, title, abstract.)




for i in range(len(doc.sections)):
    #Section start
    if i == 0:
        f.write("}\n\n\headerbox{Abstract}{name=section0,span=1,column=0,row=0}\n{")
    else:
        f.write("}\n\n\headerbox{" + doc.sections[i].name + "}{name=section" + str(i) + ",column=0,span=1,below=section" + str(i-1) + "}\n{")
    #Summarise section1



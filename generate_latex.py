def generate_latex(poster, filepath):

    f = open(filepath,'w+')
    g = open('poster_preamble.txt', 'r')
    h = open('logos.txt', 'r')

    #Add preamble from document
    f.write(poster.preamble)

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

    #Creates each box, indicates the position of the box with respect to the others and puts the content of the box inside
    for i in len(poster.columns):
        for j in len(poster.columns[i].boxes):

            #Create headerbox
            f.write("\headerbox{" + poster.column[i].box[j].title + "}{name=")
            f.write(poster.column[i].box[j].reference + ",span=1,column=" + str(i))

            #Indicate which box it lies beneath (if not the first box)
            if j == 1:
                f.write(",below=" + poster.column[i].box[0].reference)
            elif j == 2:
                f.write(",below=" + poster.column[i].box[1].reference)

            #Fill the box to the bottom of the page if it is the last box in the column
            if j == len(poster.columns[i].boxes):
                f.write(",above=bottom")

            #Finish headerbox
            f.write("}\n {")

            #Add content
            f.write(poster.columns[i].box[j].content)

            #Add images to the section


            #Add some new lines for prettiness
            f.write("\n}\n\n")

    f.write("\end{poster}\n\end{document}")

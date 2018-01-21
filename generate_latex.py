def generate_latex(poster, filepath):

    f = open(filepath,'w+')
    g = open('poster_preamble.txt', 'r')
    h = open('logos.txt', 'r')

    f.write("\documentclass[a0paper,fontscale=0.4125,landscape]{baposter} %landscape\n")

    #Add preamble from document
    f.write(poster.preamble)

    #Insert preamble
    f.write(g.read())

    #Insert title
    f.write(poster.title)

    #Tex bable
    f.write("} \n %%% Authors %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n { \n \\vspace{2.2em} \n \t{\small \n \t")

    #Insert authors
    f.write(poster.author)

    #Insert logos text, can be edited in the text file
    f.write(h.read())

    #Creates each box, indicates the position of the box with respect to the others and puts the content of the box inside
    for i in range(len(poster.columns)):
        for j in range(len(poster.columns[i].boxes)):

            #Create headerbox
            f.write("\headerbox{" + poster.columns[i].boxes[j].title + "}{name=")
            f.write(poster.columns[i].boxes[j].reference + ",span=1,column=" + str(i))

            #Indicate which box it lies beneath (if not the first box)
            if j == 1:
                f.write(",below=" + poster.columns[i].boxes[0].reference)
            elif j == 2:
                f.write(",below=" + poster.columns[i].boxes[1].reference)

            #Fill the box to the bottom of the page if it is the last box in the column
            if j == len(poster.columns[i].boxes):
                f.write(",above=bottom")

            #Finish headerbox
            f.write("}\n {")

            # Add images to the section
            for figure in poster.columns[i].boxes[j].figures:
                f.write("\n\\begin{center}\n\\includegraphics[width = 0.9\\linewidth]{")
                f.write(figure.image_path)
                f.write("}\n\\begin{minipage}{1\\linewidth}\n\\textbf{Figure ??:}")
                f.write(figure.caption)
                f.write("\n\\end{minipage}\n\\end{center}\n")

            #Add content
            f.write(poster.columns[i].boxes[j].content)

            #Add some new lines for prettiness
            f.write("\n}\n\n")

    f.write("\end{poster}\n\end{document}")

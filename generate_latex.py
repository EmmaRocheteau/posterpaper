def generate_latex(poster):

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

    f.write("\headerbox{" + poster.column[i].box[j].title + "}{name=" + poster.column[i].box[j].reference + ",span")

    #Add the headerbox tex stuff
    f.write("\headerbox{Abstract}{name=abstract,span=1,column=0,row=0}\n{")

    f.write(poster.)
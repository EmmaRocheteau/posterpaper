# Class definitions for the document model. The document class must be article
class Document:
    def __init__(self, src):
        self.src = src
        self.sections = []
        self.graphics = []
        self.preamble = ""
        self.title = ""
        self.author = ""
        self.abstract = ""
        self._cleanInput()
        self._extractMetaData()
        self._extractAbstract()
        self._parseSource()
        return

    def _parseSource(self):
        # Break up the document into raw sections
        fin = open("clean.txt", "r")
        line = fin.readline()
        while line.startswith("\\end{document}") is False:
            if line.startswith("\section"):
                sec = Section()
                # Get the name of the section
                start = line.find("{")
                end = line.find("}", start)
                sec.name = line[start+1:end]
                line =  fin.readline()
                while line.startswith("\section") is False and line.startswith("\\end{document}") is False:
                    # While we are in this same section
                    if line.startswith("\\bibliography") is False:
                        sec.raw += line
                    line = fin.readline()
                self.sections.append(sec)
                print(sec.raw)
            else:
                line = fin.readline()
        return

    def _cleanInput(self):
        # Remove comments, citations, maketitle and appendices
        fin = open(self.src, "r")
        fout = open("clean.txt", "w+")
        for line in fin:
            # Clear opening whitespace and trailing whitespace.
            line = line.strip() + "\n"
            # Check if line is a comment
            if line.startswith("%") is False and line.isspace() is False:
                # Remove maketitle command
                start = line.find("\maketitle")
                if start != -1:
                    line = line[0:start] + line[start + 10:]
                # Remove citations like this: ~\cite{robinson2008conceptual}
                while line.find("~\\cite{") != -1:
                    start = line.find("~\\cite{")
                    end = line.find("}", start)
                    line = line[0:start] + line[end+1:]
                # Write the cleaned up line to the file
                fout.write(line)
        fin.close()
        fout.close()
        return

    def _extractMetaData(self):
        # Title, author and preamble
        fin = open("clean.txt", "r")
        for line in fin:
            if line.startswith("\\usepackage") or line.startswith("\\graphicspath") or \
                line.startswith("\\if") or line.startswith("\\fi") or line.startswith("\\else"):
                self.preamble += line
            if line.startswith("\\title{"):
                self.title += line
            if line.startswith("\\author"):
                self.author += line
        fin.close()
        print(self.title)
        print(self.author)
        print(self.preamble)
        return

    def _extractAbstract(self):
        fin = open("clean.txt", "r")
        abstract_found = False
        for line in fin:
            if line.startswith("\\begin{abstract}"):
                abstract_found = True
                continue
            if abstract_found is True:
                if line.startswith("\\end{abstract}"):
                    abstract_found = False
                    continue
                else:
                    self.abstract += line
        fin.close()
        print(self.abstract)
        return

class Section:
    def __init__(self):
        self.subsections = []
        self.content = ""
        self.name = ""
        self.raw = ""
        return

class Subsection:
    def __init__(self):
        self.subsubsections = []
        self.content = ""
        self.name = ""
        self.raw = ""

class Subsubsection:
    def __init__(self):
        self.content = ""
        self.name = ""

class Graphic:
    def __init__(self):
        self.content = ""
        self.section_name = ""
        self.name = ""